from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
import mycrm.models as models

#authenticate user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def test_page(request):
    return render(request, 'test_test_page.html', {'a':23, 'b':[1,4,3,4,5,'napis','kartówka']})

@login_required
def index_page(request):
    # username = request.POST['admin']
    # password = request.POST['qwerty12345']
    # username = 'admin'
    # password = 'qwerty12345'
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #      login(request, user)

    return render(request, 'index.html', {})

@login_required
def logout_crm(request):
    logout(request)

@login_required
def user_page(request):
    return render(request, 'user.html', {})

# def company_page(request):
#     return render(request, 'company.html', {})

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