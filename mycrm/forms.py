from django import forms
from mycrm.models import Company, User

class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Company
        fields=['name']