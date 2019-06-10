from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from simpleseo.utils import get_generic_lang_code


@python_2_unicode_compatible
class SeoMetadata(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    path = models.CharField(verbose_name=_('Path'), max_length=255, db_index=True,
                            help_text=_("This should be an absolute path, excluding "
                                        "the domain name. Example: '/foo/bar/'."))
    lang_code = models.CharField(verbose_name=_('Language'), max_length=255,
                                 choices=settings.LANGUAGES,
                                 default=get_generic_lang_code())
    title = models.CharField(verbose_name=_('Title'), max_length=255, blank=True,
                             help_text=_("Recommended length: up to 70 symbols"))
    description = models.CharField(verbose_name=_('Description'), max_length=255, blank=True,
                                   help_text=_("Recommended length: up to 160 symbols."))
    keywords = models.CharField(verbose_name=_('Keywords'), max_length=255, blank=True,
                                help_text=_("Recommended length: up to 10 keyword phrases."))
    text = models.TextField(verbose_name=_('Text'), blank=True)

    class Meta:
        verbose_name = _('SEO metadata')
        verbose_name_plural = _('SEO metadata')
        db_table = 'seo_metadata'
        unique_together = (('path', 'lang_code'), )
        ordering = ('path', 'lang_code')

    def __str__(self):
        return "Language: %s | URL: %s" % (self.lang_code, self.path)

    def get_absolute_url(self):
        return self.path


def update_seo(sender, instance, **kwargs):
    newpath = instance.get_absolute_url()
    SeoMetadata.objects.filter(content_object=instance).update(path=newpath)


def register_seo_signals():
    for app, model in getattr(settings, 'SEO_MODELS', []):
        ctype = ContentType.objects.get(app_label=app, model=model)
        if not hasattr(ctype.model_class(), 'get_absolute_url'):
            raise ImproperlyConfigured(
                "Needed get_absolute_url method not defined on %s.%s model." % (app, model)
            )
        models.signals.post_save.connect(update_seo, sender=ctype.model_class(), weak=False)
