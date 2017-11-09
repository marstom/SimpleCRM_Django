from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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

@login_required
def index_page(request):
    return render(request, 'index.html', {})

@login_required
def logout_crm(request):
    logout(request)

@login_required
def user_page(request):
    return render(request, 'user/user.html', {})


class CompaniesListView(ListView):
    template_name = 'company/company.html'

    def get_queryset(self):
        return models.Company.objects.all()


class CompanyEmployerBusinessCardList(ListView):
    template_name = 'company/company_business_card.html'

    def get_queryset(self):
        return models.CompanyEmployerBusinessCard.objects.all()

class CompanyDetailView(DetailView): #todo add special regex for it
    model = models.Company #hmm company or business card?
    template_name = 'company/company_detail.html'


class CompanyAdd(CreateView):
    form_class = forms.CompanyForm
    model = User
    template_name = 'company/add_company.html'
    success_url = '/'


class RegisterUser(CreateView):
    # form_class = UserCreationForm
    form_class = forms.SignUpForm
    model = User #user from django
    template_name = 'register_user.html'
    success_url = "/"