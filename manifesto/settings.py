from django.conf import settings

MANIFESTO_VERSIONER = getattr(settings, 'MANIFESTO_VERSIONER', 'manifesto.versioners.FileNameVersionerN')