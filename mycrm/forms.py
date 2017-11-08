from django import forms
from mycrm.models import Company
from django.contrib.auth import get_user_model


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Company
        fields=['name']

# class AddUserForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields=['username']