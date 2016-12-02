# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PackQuerySet(models.QuerySet):
    """ Emojis Pack Queryset/Manager """

    # Getter
    def by_name(self, name):
        """ Return the Emojis tagged with a word """
        return self.filter(name__icontains=name)


class Pack(models.Model):
    """ Emoji pack """

    # Fields
    name = models.CharField(max_length=40, blank=False, verbose_name=_("Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    subdirectory = models.CharField(max_length=32, blank=False, verbose_name=_("Path"))
    tags = models.CharField(max_length=96, blank=True, help_text=_("Comma-separated"), verbose_name=_("Tags"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    objects = PackQuerySet.as_manager()

    # Actions
    def activate(self, value=True):
        """ Activate the Emojis in the pack """
        self.is_active = value
        self.save()

    # Overrides
    def save(self, *args, **kwargs):
        """ Save the pack """
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Delete the pack """
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    # Metadata
    class Meta:
        ordering = ['name']
        verbose_name = _("Emoji pack")
        verbose_name_plural = _("Emoji packs")
        app_label = 'Emojis'
