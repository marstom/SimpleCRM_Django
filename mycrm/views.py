'''
mycrm all views
'''

#core Django imports
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Coalesce

#Import from current app
import mycrm.models as models
import mycrm.forms as forms
from logger import logger

#Third party libraries import
from reportlab.pdfgen import canvas

#my utilities and libraries
from mycrm.my_utilities import queries


session = SessionStore()


class UpdateViewWithMessage(UpdateView):
    '''
    Extended Update view contain field:
    my_message - message which displays in green bracket after succesfull delete, user must first set this field
    page_title - title that dispalys in update page header
    '''
    def form_valid(self, form):
        messages.success(self.request, self.my_message)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        #using for create universal template for update views
        context = super().get_context_data()
        context['page_title'] = self.page_title
        return context

class DeleteViewWithMessage(DeleteView):
    '''
    Extended Update view contain field:
    my_message - message which displays in green bracket after succesfull delete, user must first set this field
    page_title - title that dispalys in update page header
    page_text - text display below page title in <p>page_text</p>
    '''
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.my_message)
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_title'] = self.page_title
        context['page_text'] = '{} {}?'.format(self.page_text, context['object'])
        return context


class CreateViewWithMessage(CreateView):
    '''
    Create view with green popup message after success submit
    Child must overrdte my_message
    '''

    def form_valid(self, form):
        messages.success(self.request, self.my_message)
        return super().form_valid(form)


@login_required
def logout_crm(request):
    '''
    logout current user
    /mycrm/logout
    '''
    logout(request)
    return render(request, 'logout.html')


@login_required
def company_report(request):
    '''
    create pdf report
    company/report
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


class UsersList(LoginRequiredMixin, ListView):
    '''
    page with users table
    mycrm/user/
    '''
    template_name = 'user/user.html'
    context_object_name = 'users'
    model = User


class RegisterUser(LoginRequiredMixin, CreateViewWithMessage):
    '''
    registration page
    mycrm/user/register
    '''
    form_class = forms.SignUpForm
    model = User #user from django
    template_name = 'user/register_user.html'
    success_url = reverse_lazy('mycrm:user')
    my_message = 'User created succesfully!'

class UserEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateViewWithMessage):
    '''
    user edit page
    mycrm/user/<user_id>/edit
    '''
    permission_required = 'auth.change_user'
    form_class = forms.EditUserForm
    model = User
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:user')
    my_message = 'Update user succesfully'
    page_title = 'Edit User:'


class UserDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteViewWithMessage):
    '''
    user delete page
    mycrm/user/<user_id>/delete
    '''
    permission_required = 'auth.delete_user'
    model = User
    template_name = 'delete_view.html'
    success_url = reverse_lazy('mycrm:user')
    my_message = 'You delete user succesfully!'
    page_title = 'Delete user'
    page_text = 'Are you sure delete user?'


class CompaniesListView(LoginRequiredMixin, ListView):
    '''
    page with companies table
    mycrm/company
    '''
    model = models.Company
    template_name = 'company/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompaniesListView, self).get_context_data(**kwargs)
        context['tomek']= 'przyklad'
        return context

    def get_queryset(self): # for filtering
        '''
        Using for filtering (search filed)
        :return: filtered queryset
        '''
        qs= super().get_queryset()
        var = self.request.GET.get('q')
        if var:
            return qs.filter(name__startswith=var)
        return qs


class CompanyUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateViewWithMessage):
    '''
    company update page
    mycrm/company/<company_id>/edit
    '''
    permission_required = 'mycrm.change_company'
    form_class = forms.CompanyForm
    model = models.Company
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You change company data succesfully!'
    page_title = 'Edit company:'


class CompanyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteViewWithMessage):
    '''
    company delete page
    mycrm/<company_id>/delete
    '''
    permission_required = 'mycrm.delete_company'
    model = models.Company
    success_url = reverse_lazy('mycrm:company')
    template_name = 'delete_view.html'
    page_title = 'Delete company'
    page_text = 'Are you sure you want delete company:'
    my_message = 'You delete company succesfully!'


class CompanyDetailView(LoginRequiredMixin, DetailView):
    '''
    company detail view:
    description, contacts table, orders table
    mycrm/company/<company_id>/
    '''
    model = models.Company
    template_name = 'company/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comments'] = models.Comment.objects.all()
        current_company = context['object']
        nonordered_comments = current_company.comment_set.all()
        context['comments'] = nonordered_comments.order_by(Coalesce('date', 'pk').desc())
        logger.info(context['comments'])
        return context

    def get(self, request, *args, **kwargs):
        get = request.GET
        if get and 'comm' in get and 'title' in get:
            logger.info('ADDING COMMENT ...')
            logger.info('REQEST ->   {}'.format(request))
            logger.info('kwargs  {} user {} args {}'.format(kwargs, request.user, args))
            title = request.GET['title']
            comm = request.GET['comm']
            current_company = models.Company.objects.get(pk=kwargs['pk'])
            # current_company = self.get_context_data()['object'] #not works
            #pk mam w request current_company.comment_set - comment_set.comment - wyciągam coś z comment
            comment = models.Comment(company=current_company, user=request.user, title=title, comment=comm)
            comment.save()
            logger.info('comment content :{}'.format(comment))

        if get and 'delete_comment' in get:
            logger.info('DELETING COMMENT ...')
            logger.info('comment clicked id {}'.format(get['delete_comment']))
            try:
                current_comment = models.Comment.objects.get(pk=get['delete_comment'])
                logger.info(current_comment)
                current_comment.delete()
            except:
                logger.error('no comment with corresponding ID')

        return super().get(kwargs, *args, **kwargs)


class CompanyAdd(LoginRequiredMixin, CreateViewWithMessage):
    '''
    add new company form
    mycrm/company/add
    '''
    form_class = forms.CompanyForm
    template_name = 'mycrm/company_form.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'Add Company Success!'


class ContactAdd(LoginRequiredMixin, CreateViewWithMessage):
    '''
    add new company form
    mycrm/company/addcontact
    '''
    form_class = forms.ContactAddForm
    template_name = 'mycrm/contact_form.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'Add Contact successfuly!'

class ContactEdit(LoginRequiredMixin, UpdateViewWithMessage):
    '''
    edit contact on company detail page
    mycrm/company/<contact_id>/editcontact
    '''
    form_class = forms.ContactAddForm
    model = models.BusinessCard
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You update contact succesfully!'
    page_title = 'Edit contact:'


class ContactDelete(LoginRequiredMixin, DeleteViewWithMessage):
    '''
    delete contact on company detail page
    mycrm/company/<contact_id>/deletecontact
    '''
    model = models.BusinessCard
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You delete contact succesfully!'
    template_name = 'delete_view.html'
    page_title = 'Delete contact'
    page_text = 'Are you sure you want delete contact:'
    my_message = 'You delete contact succesfully!'


class OrderAdd(LoginRequiredMixin, PermissionRequiredMixin, CreateViewWithMessage):
    '''
    Add new contact
    mycrm/company/addcontact
    '''
    permission_required = 'mycrm.add_order'
    form_class = forms.OrderAddForm
    template_name = 'mycrm/order_form.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'Add order succesfull!'


class OrderEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateViewWithMessage):
    '''
    edit order on company detail page
    mycrm/company/<contact_id>/orderedit
    '''
    permission_required = 'mycrm.change_order'
    form_class = forms.OrderAddForm
    model = models.Order
    template_name = 'update_view.html'
    success_url = reverse_lazy('mycrm:company')
    my_message = 'You update order succesfully!'
    page_title = 'Edit order:'
