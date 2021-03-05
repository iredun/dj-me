from django.contrib import admin
from main.models import Skill, Language


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percent']
    list_display_links = ['id', 'name', 'percent']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'stars']
    list_display_links = ['id', 'name']
