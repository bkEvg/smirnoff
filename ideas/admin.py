from django.contrib import admin
from .models import Galery, Photo
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


class PhotoInline(admin.TabularInline):
	model = Photo


class GaleryAdmin(TranslationAdmin):
	list_display = ['title']
	inlines = [PhotoInline]

admin.site.register(Galery, GaleryAdmin)