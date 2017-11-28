from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
import mycrm.models as models
import mycrm.forms as forms

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.models import User

#authenticate user
from django.contrib.auth import logout
#my utilities
from mycrm.my_utilities import queries

session = SessionStore()

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
    '''
    create pdf report
    '''
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response, initialFontName='Times-Roman')
    lines = queries.get_companies_report_text()

    page_size = 35
    space = 20
    for i,line in enumerate(lines):
        p.drawString(50, 800-(i % page_size)*space, line)
        if (i+1) % page_size == 0:
            p.showPage()
    p.save()
    return response

class UpdateViewWithMessage(UpdateView):
    def form_valid(self, form):
        messages.success(self.request, self.my_message)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        #using for create universal template for update views
        context = super().get_context_data()
        context['page_title'] = self.page_title
        return context

class DeleteViewWithMessage(DeleteView):
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.my_message)
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_title'] = self.page_title
        context['page_text'] = '{} {}?'.format(self.page_text, context['object'])
        return context

class UsersList(ListView):
    template_name = 'user/user.html'
    context_object_name = 'users'
    model = User


class RegisterUser(CreateView):
    form_class = forms.SignUpForm
    model = User #user from django
    template_name = 'user/register_user.html'
    success_url = reverse_lazy('mycrm:user')

class UserEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateViewWithMessage):
    permission_required = 'auth.change_user'
    form_class = forms.EditUserForm
    model = User
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:user')
    my_message = 'Update user succesfully'
    page_title = 'Edit User:'


class UserDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteViewWithMessage):
    permission_required = 'auth.delete_user'
    model = User
    template_name = 'delete_view.html'
    success_url = reverse_lazy('mycrm:user')
    my_message = 'You delete user succesfully!'
    page_title = 'Delete user'
    page_text = 'Are you sure delete user?'



class CompaniesListView(LoginRequiredMixin, ListView):
    model = models.Company
    template_name = 'company/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompaniesListView, self).get_context_data(**kwargs)
        context['tomek']= 'przyklad'
        return context

    def get_queryset(self): # for filtering
        qs= super().get_queryset()
        var = self.request.GET.get('q')
        if var:
            return qs.filter(name__startswith=var)
        return qs


class CompanyUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateViewWithMessage):
    permission_required = 'mycrm.change_company'
    form_class = forms.CompanyForm
    model = models.Company
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You change company data succesfully!'
    page_title = 'Edit company:'


class CompanyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteViewWithMessage):
    permission_required = 'mycrm.delete_company'
    model = models.Company
    success_url = reverse_lazy('mycrm:company')
    template_name = 'delete_view.html'
    page_title = 'Delete company'
    page_text = 'Are you sure you want delete company:'
    my_message = 'You delete company succesfully!'


class CompanyEmployerBusinessCardList(LoginRequiredMixin, ListView):
    template_name = 'company/company_business_card.html'

    def get_queryset(self):
        return models.BusinessCard.objects.all()

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = models.Company
    template_name = 'company/company_detail.html'


class CompanyAdd(LoginRequiredMixin, CreateView):
    form_class = forms.CompanyForm
    template_name = 'mycrm/company_form.html'
    success_url = reverse_lazy('mycrm:company')


class ContactAdd(LoginRequiredMixin, CreateView):
    form_class = forms.ContactAddForm
    template_name = 'mycrm/contact_form.html'
    success_url = reverse_lazy('mycrm:company')


class ContactEdit(LoginRequiredMixin, UpdateViewWithMessage):
    form_class = forms.ContactAddForm
    model = models.BusinessCard
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You update contact succesfully!'
    page_title = 'Edit contact:'


class ContactDelete(LoginRequiredMixin, DeleteViewWithMessage):
    model = models.BusinessCard
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You delete contact succesfully!'
    template_name = 'delete_view.html'
    page_title = 'Delete contact'
    page_text = 'Are you sure you want delete contact:'
    my_message = 'You delete contact succesfully!'


class OrderAdd(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'mycrm.add_order'
    form_class = forms.OrderAddForm
    template_name = 'mycrm/order_form.html'
    success_url = reverse_lazy('mycrm:company')


class OrderEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateViewWithMessage):
    permission_required = 'mycrm.change_order'
    form_class = forms.OrderAddForm
    model = models.Order
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You update order succesfully!'
    page_title = 'Edit order:'
