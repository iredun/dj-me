from django.contrib import admin
from main.models import Skill, Language, Education, SocLink, Project, ContactForm


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percent']
    list_display_links = ['id', 'name', 'percent']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'stars']
    list_display_links = ['id', 'name']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'loc', 'year_start', 'year_end']
    list_display_links = ['id', 'name']


@admin.register(SocLink)
class SocLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'link', 'sort']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'sort']
    list_display_links = ['id', 'name']


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'project']
