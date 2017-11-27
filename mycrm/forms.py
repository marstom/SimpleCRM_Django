from crispy_forms.bootstrap import StrictButton, InlineField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from mycrm.models import Company, BusinessCard, Order

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class CompanyForm(forms.ModelForm):
    picture = forms.CharField(required=False)
    class Meta:
        model = Company
        fields=['name', 'description', 'picture']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ContactAddForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields=['name', 'last_name', 'phone', 'company']

class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['name', 'description', 'value', 'payment_status','date_created','project_is_finished','company']