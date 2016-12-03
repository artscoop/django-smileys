# coding: utf-8
from django.contrib import admin

from emojis.models.pack import Pack


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    """ Admin configuration for Emoji packs """

    # Configuration
    list_display = ['id', 'name', 'subdirectory', 'is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['name', 'description', 'tags']
