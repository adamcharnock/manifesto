# -*- coding: utf-8 -*-


class Manifest(object):
    def __init__(self, *args, **kwargs):
        super(Manifest, self).__init__(*args, **kwargs)
        self.key = None

    def fallback(self):
        return []

    def network(self):
        return ['*']

    def cache(self):
        return []

    def set_key(self, key):
        self.key = key
