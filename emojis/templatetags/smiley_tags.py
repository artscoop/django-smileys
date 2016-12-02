# coding: utf-8
from django import template
from emojis.models import Smiley
import re


register = template.Library()


@register.filter(name='smileys')
def gen_smileys(string):
    """
    Replaces all occurrences of the active smiley patterns in `value`

    with a tag that points to the image associated with the respective pattern.
    """
    for smiley in Smiley.objects.active():
        img = '<img class="smiley" src="%s" alt="%s" height="%i" width="%i" />' % (smiley.image.url, smiley.description, smiley.image.height, smiley.image.width)

        if smiley.is_regex:
            # regex patterns allow you to use the same Smiley for multiple
            # ways to type a smiley
            string = re.sub(smiley.pattern, img, string)
        else:
            # this is the stupid (strict) way
            string = string.replace(smiley.pattern, img)

    return string
