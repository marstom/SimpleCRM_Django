from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
import mycrm.models as models
import mycrm.forms as forms

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#authenticate user
from django.contrib.auth import authenticate, login, logout

#my utilities
from mycrm.my_utilities import queries

session = SessionStore()
# Create your views here.

@login_required
def test_page(request):
    return render(request, 'test_test_page.html', {'a':23, 'b':[1,4,3,4,5,'napis','kartówka']})

@login_required
def index_page(request):
    return render(request, 'index.html', {})

def logout_crm(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def user_page(request):
    return render(request, 'user/user.html', {})

def company_report(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    lines = queries.get_companies_report_text()

    for i,line in enumerate(lines):
        p.drawString(50, 800-i*20, line)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()


    return response
    # return HttpResponse('This is test report page<br> {}'.format(napis))

class UsersList(ListView):
    template_name = 'user/user.html'
    context_object_name = 'users'
    model = User

class CompaniesListView(LoginRequiredMixin, ListView):
    model = models.Company
    template_name = 'company/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompaniesListView, self).get_context_data(**kwargs)
        context['tomek']= 'przyklad'
        return context

    def get_queryset(self): # for filtering
        qs= super().get_queryset()
        print(self.request.GET.get('q'))
        var = self.request.GET.get('q')
        if var:
            return qs.filter(name__startswith=var)
        return qs


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    form_class = forms.CompanyForm
    model = models.Company
    success_url = reverse_lazy('mycrm:company')

class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = models.Company
    success_url = reverse_lazy('mycrm:company')

class CompanyEmployerBusinessCardList(LoginRequiredMixin, ListView):
    template_name = 'company/company_business_card.html'

    def get_queryset(self):
        return models.BusinessCard.objects.all()

class CompanyDetailView(LoginRequiredMixin, DetailView): #todo add special regex for it
    model = models.Company
    template_name = 'company/company_detail.html'


class CompanyAdd(LoginRequiredMixin, CreateView):
    form_class = forms.CompanyForm
    # model = models
    # template_name = 'company/add_company.html'
    template_name = 'mycrm/company_form.html'
    success_url = reverse_lazy('mycrm:company')


class RegisterUser(CreateView):
    # form_class = UserCreationForm
    form_class = forms.SignUpForm
    model = User #user from django
    template_name = 'user/register_user.html'
    success_url = reverse_lazy('mycrm:user')

class ContactAdd(LoginRequiredMixin, CreateView):
    form_class = forms.ContactAddForm
    template_name = 'mycrm/contact_form.html'
    success_url = reverse_lazy('mycrm:company')

class ContactEdit(LoginRequiredMixin, UpdateView):
    form_class = forms.ContactAddForm
    model = models.BusinessCard
    success_url = reverse_lazy('mycrm:company')

    # def get_success_url(self):
    #     global page
    #     page = self.request.GET.get('page')
    #     print(page)
    #     return reverse_lazy('mycrm:detail')

class ContactDelete(LoginRequiredMixin, DeleteView):
    model = models.BusinessCard
    success_url = reverse_lazy('mycrm:company')

class OrderAdd(LoginRequiredMixin, CreateView):
    form_class = forms.OrderAddForm
    template_name = 'mycrm/order_form.html'
    success_url = reverse_lazy('mycrm:company')

class OrderEdit(LoginRequiredMixin, UpdateView):
    form_class = forms.OrderAddForm
    model = models.Order
    success_url = reverse_lazy('mycrm:company')