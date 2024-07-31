#!/usr/bin/env python3
"""C
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache
(LIFO algorithm)
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """_summ
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_ Args:
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Args:
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
