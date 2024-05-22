#!/usr/bin/env python3
"""LFUCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Method initializer/constructor"""
        super().__init__()
        self.freq = defaultdict(int)  # Frequency of access for each key
        self.keys_by_freq = defaultdict(list)  # Keys grouped by frequency
        self.min_freq = 0  # Minimum frequency of the current keys

    def _update_freq(self, key):
        """Update frequency of a key and reassign its position in keys_by_freq"""
        freq = self.freq[key]
        self.keys_by_freq[freq].remove(key)
        if not self.keys_by_freq[freq]:
            del self.keys_by_freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.freq[key] += 1
        freq = self.freq[key]
        self.keys_by_freq[freq].append(key)

    def put(self, key, item):
        """Method that assigns to the dictionary self.cache_data the item value for the key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_freq(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = self.keys_by_freq[self.min_freq].pop(0)
                if not self.keys_by_freq[self.min_freq]:
                    del self.keys_by_freq[self.min_freq]
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                print("DISCARD: {}".format(lfu_key))

            self.cache_data[key] = item
            self.freq[key] = 1
            self.keys_by_freq[1].append(key)
            self.min_freq = 1

    def get(self, key):
        """Method that returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self._update_freq(key)
        return self.cache_data[key]
