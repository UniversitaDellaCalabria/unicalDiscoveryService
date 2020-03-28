from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _


class EntityType(models.Model):
    TYPE = (('saml', 'SAML'),
            ('oidc', 'OIDC'),
            )
    name = models.CharField(max_length=33,
                            help_text=_("category name"),
                            unique=True)
    type = models.CharField(choices=TYPE, max_length=33)

    class Meta:
        verbose_name = _('Entity Type')
        verbose_name_plural = _('Entity Type')

    def __str__(self):
        return '{} [{}]'.format(self.name, self.type.upper())



class Entity(models.Model):
    name = models.CharField(max_length=33,
                            help_text=_("data-idp value, es: namirialid"),
                            unique=True)
    display_name = models.CharField(max_length=64)
    type = models.ForeignKey(EntityType,
                             on_delete=models.CASCADE)

    entity_id = models.TextField()
    metadata_url = models.URLField(blank=True, null=True)
    logo = models.CharField(max_length=254,
                            null=True,
                            default='/'.join((settings.STATIC_URL,
                                              'images', 'no-logo.png')),
                            help_text=_('image or relative path'),)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Entity')
        verbose_name_plural = _('Entities')

    def __str__(self):
        return '{} [{}]'.format(self.name, self.type.type.upper())
