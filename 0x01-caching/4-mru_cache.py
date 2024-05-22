#!/usr/bin/env python3
"""MRUCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Method initializer/constructor"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method that assigns to the dictionary self.cache the item value for the key key."""

        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = self.order.pop()
            print("DISCARD: {}".format(last_item))
            del self.cache_data[last_item]
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Method that returns the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
