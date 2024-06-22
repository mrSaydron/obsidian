Получение скриншота
adb connect 192.168.0.100:5555
adb shell screencap /mnt/sdcard/Download/test.png
adb pull /mnt/sdcard/Download/test.png test.png