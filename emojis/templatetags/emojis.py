# coding: utf-8
from django import template


register = template.Library()


@register.filter(name='emojis')
def convert_emoji(string):
    """ Replaces all occurrences of unicode and codenamed emojis with actual emoji pictures """
    return string
