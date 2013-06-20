import os.path

from bencode import bencode

try:
    from hashlib import sha1
except ImportError:
    from django.utils.hashcompat import sha_constructor as sha1

from django.contrib.staticfiles.finders import find
from django.conf import settings

class AbstractVersioner(object):
    def get_version(self, files):
        raise NotImplemented('Implement this method in a child class')


class AbstractCachedVersioner(AbstractVersioner):
    cache = {}

    def get_version(self, files):
        hash_ = sha1()
        for v in self.get_versions(files):
            hash_.update(str(v))
        return hash_.hexdigest()[:7]

    def get_versions(self, files):
        for f in files:
            if f in AbstractCachedVersioner.cache and not settings.DEBUG:
                yield AbstractCachedVersioner.cache[f]
            else:
                version = self.get_file_version(f)
                AbstractCachedVersioner.cache[f] = version
                yield version

    def get_file_version(self, file_name):
        pass


class FileNameVersioner(AbstractVersioner):
    def get_version(self, files):
        return sha1(bencode(list(files))).hexdigest()[:7]


class LastModifiedVersioner(AbstractCachedVersioner):
    def get_file_version(self, file_name):
        absolute_name = file_name.replace(settings.STATIC_URL, '', 1).lstrip('/')
        absolute_name = find(absolute_name)
        if absolute_name:
            version = os.path.getmtime(absolute_name)
        else:
            version = file_name
        return version
