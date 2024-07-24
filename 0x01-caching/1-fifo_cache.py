#!/usr/bin/env python3
"""
If the number of items in self.cache_data is
higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache
(FIFO algorithm)
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """_summary_
    """

    def __init__(self):
        """_summ
        """
        super().__init__()

    def put(self, key, item):
        """ Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
