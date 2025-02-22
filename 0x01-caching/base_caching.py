#!/usr/bin/env python3
""" BaseCaching module """


class BaseCaching:
    """ BaseCaching defines:"""
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        msg = "put must be implemented in your cache class"
        raise NotImplementedError(msg)

    def get(self, key):
        """ Get an item by key """
        msg = "get must be implemented in your cache class"
        raise NotImplementedError(msg)
