import re

from django.conf import settings

class AbstractFilter(object):
    def filter_files(self, files):
        out = []
        for f in files:
            filtered = self.filter_file(f)
            if filtered:
                out.append(f)
        return out

    def filter_file(self, file):
        raise NotImplemented()


class AllFilter(AbstractFilter):
    """Default filter which does nothing"""
    def filter_files(self, files):
        return files


class ExcludePatternFilter(AbstractFilter):
    """Ignore files with specified prefixes"""
    def filter_file(self, file):
        for pattern in settings.MANIFESTO_FILTER_EXCLUDE_PATTERNS:
            if re.search(pattern, file):
                return None
        return file
