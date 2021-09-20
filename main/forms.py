from django import forms 
from .models import Proposal


class ProposalForm(forms.ModelForm):
	class Meta:
		model = Proposal
		exclude = ['date_created', 'date_updated', 'page_from']