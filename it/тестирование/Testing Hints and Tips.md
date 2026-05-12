whenever(swiftCacheManager.getCache(any())).thenThrow(RuntimeException())
doThrow(RuntimeException()).`when`(swiftCacheManager).getCache(any())