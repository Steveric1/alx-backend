#!/usr/bin/env python3

"""
BasicCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache define:
     - self.cache_data - {'key': 'value'} from BaseCaching
     - self.put() that save arguments to self.cache_data
     - self.get() that return arguments from self.cache_data
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""

        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data"""

        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
