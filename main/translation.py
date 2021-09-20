from modeltranslation.translator import translator, TranslationOptions
from .models import Staff

class StaffTranslationOptions(TranslationOptions):
	fields = ('position', 'first_name', 'last_name', 'notation')

translator.register(Staff, StaffTranslationOptions)