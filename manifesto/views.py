# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.core.signing import Signer

from manifesto import manifest, UnifiedManifest


class ManifestView(TemplateView):
    template_name = "manifesto/manifest.appcache"

    def dispatch(self, request, *args, **kwargs):
        # Get and unsign the key if we have one
        key = kwargs.get('key', None)
        if key:
            signer = Signer(sep='_', salt='manifesto')
            key = signer.unsign(key)
        self.key = key
        return super(ManifestView, self).dispatch(request, *args, **kwargs)

    def render_to_response(self, context, **kwargs):
        kwargs['content_type'] = 'text/cache-manifest'
        return super(ManifestView, self).render_to_response(context, **kwargs)

    def get_context_data(self, **kwargs):
        # If we have a key they do not rely on the
        # globally cached manifest
        if self.key:
            man = UnifiedManifest(key=self.key)
        else:
            man = manifest

        kwargs.update({
            'revision': man.revision,
            'cache_list': man.cache,
            'network_list': man.network,
            'fallback_list': man.fallback,
        })
        return kwargs
