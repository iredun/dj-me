from django.contrib import admin
from main.models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percent']
    list_display_links = ['id', 'name', 'percent']