from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Staff, Proposal

class StaffAdmin(TranslationAdmin):
	list_display = ['first_name', 'position']

admin.site.register(Staff, StaffAdmin)

class ProposalAdmin(admin.ModelAdmin):
	list_display = ['name', 'date_created']

admin.site.register(Proposal, ProposalAdmin)