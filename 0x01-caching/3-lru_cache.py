#!/usr/bin/env python3
"""
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS:
you must discard the least recently used item
(LRU algorithm)
you must print DISCARD: with the key discarded
and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
You must use self.cache_data - dictionary from the parent class
You can overload def __init__(self): but don’t call the paret
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """If the number of items in self.cache_data is higher that
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """ Args:
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Args:
                        key (_type_): _des
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
