from django.conf import settings

MANIFESTO_VERSIONER = getattr(settings, 'MANIFESTO_VERSIONER', 'manifesto.versioners.FileNameVersioner')
MANIFESTO_FILTER = getattr(settings, 'MANIFESTO_FILTER', 'manifesto.filters.AllFilter')
