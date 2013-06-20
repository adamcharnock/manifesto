from django import template
from django.core.urlresolvers import reverse
from django.core.signing import Signer

register = template.Library()


@register.simple_tag
def manifest_url(key=None):
    if not key:
        return reverse('cache_manifest')
    else:
        signer = Signer(sep='_', salt='manifesto')
        signed_key = signer.sign(key)
        return reverse('cache_manifest_keyed', args=[signed_key])
