#!/usr/bin/env python3
"""FIFOCache that inherit from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache define:
     - self.cache_data - {'key': 'value'} from BaseCaching
     - self.put() that save arguments to self.cache_data
     - self.get() that return arguments from self.cache_data
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""

        if key is None or item is None:
            return
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first_key))
            del self.cache_data[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
