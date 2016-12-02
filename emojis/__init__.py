# coding: utf-8
from django.apps.config import AppConfig
from django.utils.translation import gettext_noop

__version__ = (1, 2016, 12)

gettext_noop("Emojis")


class EmojisConfig(AppConfig):
    """ App configuration """

    name = 'emojis'
    label = 'emojis'

    def ready(self):
        """ System is ready """
        pass

# Charger la configuration ci-dessus par défaut
default_app_config = 'emojis.EmojisConfig'
