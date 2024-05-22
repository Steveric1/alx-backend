#!/usr/bin/env python3
""" LRUCache that inherits from BaseCaching and is a caching system:"""
from base_caching import BaseCaching


class Node:
    """Node class for doubly linked list"""

    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        super().__init__()
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache_data = {}

    def _remove(self, node):
        """Remove node from doubly linked list"""
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _insert(self, node):
        """Insert node to doubly linked list"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def put(self, key, item):
        """Add item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self._remove(self.cache_data[key])
        self.cache_data[key] = Node(key, item)
        self._insert(self.cache_data[key])
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = self.tail.prev
            self._remove(lru)
            print("DISCARD:", lru.key)
            del self.cache_data[lru.key]

    def get(self, key):
        """Get item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        node = self.cache_data[key]
        self._remove(node)
        self._insert(node)
        return node.value
