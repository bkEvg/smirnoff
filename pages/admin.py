from django.contrib import admin
from .models import Page
from modeltranslation.admin import TranslationAdmin


class PageAdminView(TranslationAdmin):
	prepopulated_fields = {"slug": ("title",)}
	
admin.site.register(Page, PageAdminView)

