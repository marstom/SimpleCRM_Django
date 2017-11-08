from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
import mycrm.models as models
import mycrm.forms as forms

from django.contrib.auth.forms import UserCreationForm

#authenticate user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
    return render(request, 'user.html', {})


class CompaniesListView(ListView):
    model = models.Company
    #context_object_name = 'company_page'
    template_name = 'company.html'

class CompanyDetailView(DetailView): #todo add special regex for it
    '''
    Show all workers belong to company
    '''
    model = models.Company #hmm company or business card?
    template_name = 'company_detail.html'

# class CompanyEmployerDetailView(DetailView): #todo in the future
    '''
    Show employer Business_card
    '''
#   pass

class AddUser(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'company/add_company.html'

class RegisterUser(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'register_user.html'

    success_url = "/"