from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore
from django.db.models import Sum, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
import mycrm.models as models
import mycrm.forms as forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#authenticate user
from django.contrib.auth import authenticate, login, logout

session = SessionStore()
# Create your views here.

def test_page(request):
    return render(request, 'test_test_page.html', {'a':23, 'b':[1,4,3,4,5,'napis','kartówka']})

#@login_required
def index_page(request):
    return render(request, 'index.html', {})

#@login_required
def logout_crm(request):
    logout(request)

#@login_required
def user_page(request):
    return render(request, 'user/user.html', {})

class UsersList(ListView):
    template_name = 'user/user.html'
    context_object_name = 'users'
    model = User

class CompaniesListView(ListView):
    model = models.Company
    template_name = 'company/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompaniesListView, self).get_context_data(**kwargs)
        context['tomek']= 0
        context['count']=0
        print(kwargs)
        return context

    # def get_queryset(self): # for filtering
    #     qs= super().get_queryset()
    #     return qs.filter(name__startswith='co')

class CompanyUpdate(UpdateView):
    form_class = forms.CompanyForm
    model = models.Company
    success_url = reverse_lazy('mycrm:company')

class CompanyDelete(DeleteView):
    model = models.Company
    success_url = reverse_lazy('mycrm:company')

class CompanyEmployerBusinessCardList(ListView):
    template_name = 'company/company_business_card.html'

    def get_queryset(self):
        return models.BusinessCard.objects.all()

class CompanyDetailView(DetailView): #todo add special regex for it
    model = models.Company
    template_name = 'company/company_detail.html'


class CompanyAdd(CreateView):
    form_class = forms.CompanyForm
    # model = models
    # template_name = 'company/add_company.html'
    template_name = 'mycrm/company_form.html'
    success_url = '/'


class RegisterUser(CreateView):
    # form_class = UserCreationForm
    form_class = forms.SignUpForm
    model = User #user from django
    template_name = 'register_user.html'
    success_url = "/"

class ContactAdd(CreateView):
    form_class = forms.ContactAddForm
    template_name = 'mycrm/contact_form.html'
    success_url = reverse_lazy('mycrm:company')

class OrderAdd(CreateView):
    form_class = forms.OrderAddForm
    template_name = 'mycrm/order_form.html'
    success_url = reverse_lazy('mycrm:company')