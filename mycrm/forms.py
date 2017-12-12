'''
Forms using in mycrm app
'''
#core Django imports
from django import forms
import django.contrib.auth.models as auth_models
import django.contrib.auth.forms as auth_forms

#Import from app
from .models import Company, BusinessCard, Order

class CompanyForm(forms.ModelForm):
    '''
    Form using in CompanyUpdate and CompanyAdd views. User add new company
    '''
    picture = forms.CharField(required=False)
    class Meta:
        model = Company
        fields=['name', 'description', 'picture']


class SignUpForm(auth_forms.UserCreationForm):
    '''
    Form using for reginster new user in mycrm,
    mycrm/user/register
    '''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class EditUserForm(forms.ModelForm):
    '''
    Form using in UserEdit view. Edits User django model, can change password login and other data
    mycrm/user/<user_id>/edit
    '''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name', 'email')


class ContactAddForm(forms.ModelForm):
    '''
    Using for ContactAdd and ContactEdit views. Company contact editing or add
    mycrm/company/<pk>/addcontact
    mycrm/company/<contact_id>/editcontact
    '''
    class Meta:
        model = BusinessCard
        fields=['name', 'last_name', 'phone'] #company add automaticley

class OrderAddForm(forms.ModelForm):
    '''
    Using in OrderAdd and OrderEdit. Can add/edit contact to form
    mycrm/company/addcontact
    mycrm/company/<contact_id>/orderedit
    '''
    class Meta:
        model = Order
        fields=['name', 'description', 'value', 'payment_status','date_created','project_is_finished'] #company field update automacicly