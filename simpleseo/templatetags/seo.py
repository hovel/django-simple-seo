from django.conf import settings
from django.forms.models import model_to_dict
from django.template import Library
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

from simpleseo.models import SeoMetadata
from simpleseo.utils import get_generic_lang_code

register = Library()


def get_seo(context, **kwargs):
    path = context['request'].path

    metadata = SeoMetadata.objects.filter(
        path=path, lang_code__in=[get_language(), get_generic_lang_code()]
    ).order_by('-lang_code').first()  # lang_code: if en-gb not found, try en
    metadata = model_to_dict(metadata) if metadata is not None else {}
    result = {}
    for seo in ['title', 'description', 'keywords', 'text']:
        result[seo] = (
            metadata.get(seo) or kwargs.get(seo) or
            getattr(settings, 'SEO_DEFAULT_{0}'.format(seo.upper()), '')
        )
    return result


@register.simple_tag(takes_context=True)
def get_seo_title(context, default=''):
    return escape(get_seo(context, title=default).get('title'))


@register.simple_tag(takes_context=True)
def get_seo_description(context, default=''):
    return escape(get_seo(context, description=default).get('description'))


@register.simple_tag(takes_context=True)
def get_seo_keywords(context, default=''):
    return escape(get_seo(context, description=default).get('keywords'))


@register.simple_tag(takes_context=True)
def get_seo_text(context, default=''):
    return mark_safe(get_seo(context, description=default).get('text'))
