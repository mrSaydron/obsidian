#!/usr/bin/env python3
"""Analyze city infrastructure around an address using OpenStreetMap data."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
USER_AGENT = "perm-home-location-analyzer/1.0"


@dataclass
class GeocodeResult:
    lat: float
    lon: float
    display_name: str
    house_number: str | None
    osm_type: str | None
    osm_id: int | None


@dataclass
class Place:
    name: str
    category: str
    lat: float
    lon: float
    distance_m: int
    source: str
    osm_type: str | None = None
    osm_id: int | None = None


CATEGORIES = {
    "schools": "Школы",
    "kindergartens": "Детские сады",
    "other_education": "Другое образование",
    "medicine": "Медицина",
    "transport": "Остановки транспорта",
}


def http_get_json(url: str, params: dict[str, str], timeout: int = 30) -> Any:
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"{url}?{query}",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def http_post_json(url: str, data: str, timeout: int = 60) -> Any:
    body = urllib.parse.urlencode({"data": data}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def geocode(address: str) -> GeocodeResult:
    results = http_get_json(
        NOMINATIM_URL,
        {
            "q": address,
            "format": "jsonv2",
            "limit": "1",
            "addressdetails": "1",
        },
    )
    if not results:
        raise RuntimeError(f"Адрес не найден: {address}")
    item = results[0]
    address_details = item.get("address", {})
    osm_id = item.get("osm_id")
    return GeocodeResult(
        lat=float(item["lat"]),
        lon=float(item["lon"]),
        display_name=item.get("display_name", address),
        house_number=address_details.get("house_number"),
        osm_type=item.get("osm_type"),
        osm_id=int(osm_id) if osm_id is not None else None,
    )


def overpass_query(lat: float, lon: float, radius_m: int) -> str:
    around = f"(around:{radius_m},{lat:.7f},{lon:.7f})"
    return f"""
[out:json][timeout:45];
(
  node["amenity"~"^(school|kindergarten|college|university)$"]{around};
  way["amenity"~"^(school|kindergarten|college|university)$"]{around};
  relation["amenity"~"^(school|kindergarten|college|university)$"]{around};

  node["amenity"~"^(hospital|clinic|doctors|dentist|pharmacy)$"]{around};
  way["amenity"~"^(hospital|clinic|doctors|dentist|pharmacy)$"]{around};
  relation["amenity"~"^(hospital|clinic|doctors|dentist|pharmacy)$"]{around};

  node["public_transport"~"^(platform|stop_position|station)$"]{around};
  way["public_transport"~"^(platform|stop_position|station)$"]{around};
  relation["public_transport"~"^(platform|stop_position|station)$"]{around};
  node["highway"="bus_stop"]{around};
  node["railway"~"^(tram_stop|halt|station)$"]{around};
);
out center tags;
"""


def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> int:
    radius = 6_371_000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )
    return round(radius * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))


def element_coordinates(element: dict[str, Any]) -> tuple[float, float] | None:
    if "lat" in element and "lon" in element:
        return float(element["lat"]), float(element["lon"])
    center = element.get("center")
    if center and "lat" in center and "lon" in center:
        return float(center["lat"]), float(center["lon"])
    return None


def category_for(tags: dict[str, str]) -> str | None:
    amenity = tags.get("amenity")
    if amenity == "school":
        return "schools"
    if amenity == "kindergarten":
        return "kindergartens"
    if amenity in {"college", "university"}:
        return "other_education"
    if amenity in {"hospital", "clinic", "doctors", "dentist", "pharmacy"}:
        return "medicine"
    if tags.get("public_transport") in {"platform", "stop_position", "station"}:
        return "transport"
    if tags.get("highway") == "bus_stop":
        return "transport"
    if tags.get("railway") in {"tram_stop", "halt", "station"}:
        return "transport"
    return None


def place_name(tags: dict[str, str], category: str, osm_id: int) -> str:
    for key in ("name", "official_name", "short_name", "operator"):
        value = tags.get(key)
        if value:
            return value
    if category == "transport":
        return f"Остановка OSM {osm_id}"
    return f"Объект OSM {osm_id}"


def fetch_osm_places(lat: float, lon: float, radius_m: int) -> list[Place]:
    data = http_post_json(OVERPASS_URL, overpass_query(lat, lon, radius_m))
    places: list[Place] = []
    seen: set[tuple[str, int]] = set()

    for element in data.get("elements", []):
        osm_type = element.get("type")
        osm_id = element.get("id")
        if not osm_type or not osm_id or (osm_type, osm_id) in seen:
            continue
        seen.add((osm_type, osm_id))

        tags = element.get("tags", {})
        category = category_for(tags)
        coords = element_coordinates(element)
        if not category or not coords:
            continue

        item_lat, item_lon = coords
        places.append(
            Place(
                name=place_name(tags, category, osm_id),
                category=category,
                lat=item_lat,
                lon=item_lon,
                distance_m=haversine_m(lat, lon, item_lat, item_lon),
                source="osm",
                osm_type=osm_type,
                osm_id=int(osm_id),
            )
        )

    return [place for place in places if place.distance_m <= radius_m]


def load_custom_places(path: Path, lat: float, lon: float) -> list[Place]:
    if not path.exists():
        raise RuntimeError(f"Файл с пользовательскими местами не найден: {path}")
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise RuntimeError("Файл пользовательских мест должен содержать JSON-массив.")

    places: list[Place] = []
    for index, item in enumerate(raw, start=1):
        try:
            name = str(item["name"])
            category = str(item.get("category", "custom"))
            item_lat = float(item["lat"])
            item_lon = float(item["lon"])
        except (KeyError, TypeError, ValueError) as exc:
            raise RuntimeError(f"Некорректное место #{index} в {path}: {item}") from exc

        places.append(
            Place(
                name=name,
                category=category,
                lat=item_lat,
                lon=item_lon,
                distance_m=haversine_m(lat, lon, item_lat, item_lon),
                source="custom",
            )
        )
    return places


def format_distance(meters: int) -> str:
    if meters < 1000:
        return f"{meters} м"
    return f"{meters / 1000:.2f} км"


def print_category(title: str, places: list[Place], limit: int) -> None:
    print(f"\n{title}: {len(places)} в радиусе поиска")
    if not places:
        print("  Нет объектов.")
        return

    for place in sorted(places, key=lambda item: item.distance_m)[:limit]:
        osm_ref = ""
        if place.osm_type and place.osm_id:
            osm_ref = f" | OSM: {place.osm_type}/{place.osm_id}"
        print(
            f"  - {format_distance(place.distance_m):>7} | "
            f"{place.name} | {place.lat:.6f}, {place.lon:.6f}{osm_ref}"
        )


def print_summary(places: list[Place], radius_m: int) -> None:
    thresholds = [500, 1000, radius_m]
    thresholds = sorted(set(threshold for threshold in thresholds if threshold <= radius_m))

    print("\nСводка:")
    for category, title in CATEGORIES.items():
        category_places = [place for place in places if place.category == category]
        nearest = min((place.distance_m for place in category_places), default=None)
        counts = ", ".join(
            f"до {format_distance(threshold)}: "
            f"{sum(1 for place in category_places if place.distance_m <= threshold)}"
            for threshold in thresholds
        )
        nearest_text = format_distance(nearest) if nearest is not None else "нет"
        print(f"  - {title}: ближайший {nearest_text}; {counts}")


def map_url(lat: float, lon: float) -> str:
    return f"https://www.openstreetmap.org/?mlat={lat:.6f}&mlon={lon:.6f}#map=17/{lat:.6f}/{lon:.6f}"


def expected_house_number(address: str) -> str | None:
    for token in address.replace(",", " ").split():
        normalized = token.strip().lower().replace("д.", "")
        if normalized and normalized[0].isdigit():
            return normalized
    return None


def print_location_details(geocoded: GeocodeResult, original_address: str) -> None:
    print(f"Найдено как: {geocoded.display_name}")
    print(f"Координаты: {geocoded.lat:.6f}, {geocoded.lon:.6f}")
    print(f"Карта: {map_url(geocoded.lat, geocoded.lon)}")

    expected_number = expected_house_number(original_address)
    if geocoded.osm_type and expected_number and geocoded.house_number != expected_number:
        actual = geocoded.house_number or "не найден"
        print(
            "Предупреждение: геокодер не подтвердил номер дома "
            f"{expected_number}; найденный номер: {actual}. "
            "Для участков лучше передать координаты вручную через --lat и --lon."
        )


def write_json_report(
    path: Path,
    address: str,
    display_name: str,
    lat: float,
    lon: float,
    radius_m: int,
    places: list[Place],
) -> None:
    geocoded = GeocodeResult(
        lat=lat,
        lon=lon,
        display_name=display_name,
        house_number=None,
        osm_type=None,
        osm_id=None,
    )
    report = build_result(address, geocoded, radius_m, places, warning="", limit=None)
    path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def place_to_json(place: Place) -> dict[str, Any]:
    return {
        "name": place.name,
        "category": place.category,
        "distance_m": place.distance_m,
        "lat": place.lat,
        "lon": place.lon,
        "source": place.source,
        "osm_type": place.osm_type,
        "osm_id": place.osm_id,
    }


def summary_for(places: list[Place], radius_m: int) -> dict[str, Any]:
    thresholds = [500, 1000, radius_m]
    thresholds = sorted(set(threshold for threshold in thresholds if threshold <= radius_m))
    summary: dict[str, Any] = {}

    for category, title in CATEGORIES.items():
        category_places = [place for place in places if place.category == category]
        nearest = min((place.distance_m for place in category_places), default=None)
        summary[category] = {
            "title": title,
            "nearest_distance_m": nearest,
            "count": len(category_places),
            "counts_within_m": {
                str(threshold): sum(
                    1 for place in category_places if place.distance_m <= threshold
                )
                for threshold in thresholds
            },
        }

    for category in sorted({place.category for place in places} - set(CATEGORIES.keys())):
        category_places = [place for place in places if place.category == category]
        nearest = min((place.distance_m for place in category_places), default=None)
        summary[category] = {
            "title": category,
            "nearest_distance_m": nearest,
            "count": len(category_places),
            "counts_within_m": {
                str(threshold): sum(
                    1 for place in category_places if place.distance_m <= threshold
                )
                for threshold in thresholds
            },
        }

    return summary


def limited_places(places: list[Place], limit: int | None) -> list[Place]:
    if limit is None:
        return sorted(places, key=lambda item: item.distance_m)

    selected: list[Place] = []
    for category in list(CATEGORIES.keys()) + sorted(
        {place.category for place in places} - set(CATEGORIES.keys())
    ):
        category_places = [
            place for place in places if place.category == category
        ]
        selected.extend(sorted(category_places, key=lambda item: item.distance_m)[:limit])
    return sorted(selected, key=lambda item: item.distance_m)


def build_result(
    address: str,
    geocoded: GeocodeResult,
    radius_m: int,
    places: list[Place],
    warning: str,
    limit: int | None,
) -> dict[str, Any]:
    warnings = [warning] if warning else []
    return {
        "address": address,
        "resolved_address": geocoded.display_name,
        "location": {
            "lat": geocoded.lat,
            "lon": geocoded.lon,
            "map_url": map_url(geocoded.lat, geocoded.lon),
            "house_number": geocoded.house_number,
            "osm_type": geocoded.osm_type,
            "osm_id": geocoded.osm_id,
        },
        "radius_m": radius_m,
        "distance_mode": "straight_line",
        "warnings": warnings,
        "summary": summary_for(places, radius_m),
        "places_limit_per_category": limit,
        "places": [place_to_json(place) for place in limited_places(places, limit)],
    }


def nearest_distance(places: list[Place], category: str) -> int | None:
    return min((place.distance_m for place in places if place.category == category), default=None)


def geocode_warning(geocoded: GeocodeResult, original_address: str) -> str:
    expected_number = expected_house_number(original_address)
    if expected_number and geocoded.house_number != expected_number:
        actual = geocoded.house_number or "не найден"
        return f"номер дома {expected_number} не подтвержден, найден: {actual}"
    return ""


def analyze_point(
    address: str,
    city: str,
    radius_m: int,
    lat: float | None = None,
    lon: float | None = None,
) -> tuple[GeocodeResult, list[Place], str]:
    if (lat is None) != (lon is None):
        raise RuntimeError("Координаты lat и lon нужно указывать вместе.")

    if lat is not None and lon is not None:
        geocoded = GeocodeResult(
            lat=lat,
            lon=lon,
            display_name=f"координаты из файла для адреса: {address}",
            house_number=None,
            osm_type=None,
            osm_id=None,
        )
        warning = ""
    else:
        geocoded = geocode(normalized_address(address, city))
        warning = geocode_warning(geocoded, address)

    return geocoded, fetch_osm_places(geocoded.lat, geocoded.lon, radius_m), warning


def read_batch_items(path: Path) -> list[dict[str, str]]:
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        if not rows or "address" not in rows[0]:
            raise RuntimeError("CSV-файл должен содержать колонку address. Опционально: lat, lon.")
        return rows

    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            items.append({"address": line})
    return items


def run_batch(args: argparse.Namespace) -> int:
    rows = read_batch_items(args.batch)
    if not rows:
        print(f"В batch-файле нет адресов: {args.batch}", file=sys.stderr)
        return 1

    if args.format == "table":
        print("address\tlat\tlon\tschool\tkindergarten\tmedicine\ttransport\twarning")

    results: list[dict[str, Any]] = []
    for row in rows:
        address = row["address"]
        lat = float(row["lat"]) if row.get("lat") else None
        lon = float(row["lon"]) if row.get("lon") else None
        try:
            geocoded, places, warning = analyze_point(
                address,
                args.city,
                args.radius,
                lat=lat,
                lon=lon,
            )
            result = build_result(address, geocoded, args.radius, places, warning, args.limit)
        except (RuntimeError, urllib.error.URLError, TimeoutError, ValueError) as exc:
            result = {
                "address": address,
                "error": str(exc),
            }

        if args.format == "table":
            if "error" in result:
                values = [address, "", "", "", "", "", "", f"ошибка: {result['error']}"]
            else:
                summary = result["summary"]
                values = [
                    address,
                    f"{result['location']['lat']:.6f}",
                    f"{result['location']['lon']:.6f}",
                    format_distance(summary["schools"]["nearest_distance_m"])
                    if summary["schools"]["nearest_distance_m"] is not None
                    else "нет",
                    format_distance(summary["kindergartens"]["nearest_distance_m"])
                    if summary["kindergartens"]["nearest_distance_m"] is not None
                    else "нет",
                    format_distance(summary["medicine"]["nearest_distance_m"])
                    if summary["medicine"]["nearest_distance_m"] is not None
                    else "нет",
                    format_distance(summary["transport"]["nearest_distance_m"])
                    if summary["transport"]["nearest_distance_m"] is not None
                    else "нет",
                    "; ".join(result["warnings"]),
                ]
            print("\t".join(values))
        else:
            results.append(result)

        time.sleep(1)

    if args.format == "json":
        payload = {
            "mode": "batch",
            "radius_m": args.radius,
            "distance_mode": "straight_line",
            "generated_at_unix": int(time.time()),
            "results": results,
        }
        output = json.dumps(payload, ensure_ascii=False, indent=2)
        print(output)
        if args.json_out:
            args.json_out.write_text(output + "\n", encoding="utf-8")

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Статистика школ, медицины и транспорта рядом с адресом по OpenStreetMap."
    )
    parser.add_argument("address", nargs="?", help="Адрес для проверки.")
    parser.add_argument(
        "--city",
        default="Пермь, Россия",
        help="Город, который будет добавлен к адресу, если он не указан. По умолчанию: Пермь, Россия.",
    )
    parser.add_argument(
        "--lat",
        type=float,
        help="Широта точки. Если указать вместе с --lon, геокодинг адреса не используется.",
    )
    parser.add_argument(
        "--lon",
        type=float,
        help="Долгота точки. Если указать вместе с --lat, геокодинг адреса не используется.",
    )
    parser.add_argument(
        "--radius",
        type=int,
        default=1500,
        help="Радиус поиска в метрах. По умолчанию: 1500.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=7,
        help="Сколько ближайших объектов показывать в каждой категории. По умолчанию: 7.",
    )
    parser.add_argument(
        "--custom",
        type=Path,
        help="JSON-файл с вручную внесенными местами: name, lat, lon, category.",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        help="Куда сохранить полный отчет JSON.",
    )
    parser.add_argument(
        "--batch",
        type=Path,
        help="Файл со списком адресов или CSV с колонками address, lat, lon.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text", "table"),
        default="json",
        help="Формат вывода: json по умолчанию, text для одиночного запуска, table для batch.",
    )
    return parser.parse_args()


def normalized_address(address: str, city: str) -> str:
    lowered = address.lower()
    if "перм" in lowered or "perm" in lowered:
        return address
    return f"{address}, {city}"


def main() -> int:
    args = parse_args()

    if args.batch:
        return run_batch(args)

    if not args.address:
        print("Ошибка: укажите адрес или --batch файл.", file=sys.stderr)
        return 1

    try:
        geocoded, places, warning = analyze_point(
            args.address,
            args.city,
            args.radius,
            lat=args.lat,
            lon=args.lon,
        )
        if args.custom:
            places.extend(load_custom_places(args.custom, geocoded.lat, geocoded.lon))
    except (RuntimeError, urllib.error.URLError, TimeoutError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1

    result = build_result(args.address, geocoded, args.radius, places, warning, args.limit)

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.json_out:
            args.json_out.write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        return 0

    print(f"Адрес: {args.address}")
    print_location_details(geocoded, args.address)
    print(f"Радиус: {args.radius} м")
    print("Расстояния считаются по прямой, не по дорогам и тротуарам.")

    print_summary(places, args.radius)

    for category, title in CATEGORIES.items():
        print_category(
            title,
            [place for place in places if place.category == category],
            args.limit,
        )

    custom_categories = sorted(
        {place.category for place in places}
        - set(CATEGORIES.keys())
    )
    for category in custom_categories:
        print_category(
            f"Пользовательская категория: {category}",
            [place for place in places if place.category == category],
            args.limit,
        )

    if args.json_out:
        args.json_out.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"\nJSON-отчет сохранен: {args.json_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
