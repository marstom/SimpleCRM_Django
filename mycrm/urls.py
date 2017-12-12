'''
mycrm urls
'''

#core Django imports
from django.conf.urls import url
from django.contrib.auth import views as auth_views

#Import from current app
from . import views

app_name = 'mycrm'

urlpatterns=[
    #login views
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^logout/$', views.logout_crm, name="logout"),
    #mycrm views
    url(r'^$', views.UsersList.as_view(), name="home"),
    url(r'^user/$', views.UsersList.as_view(), name="user"),
    url(r'^user/(?P<pk>[0-9]+)/edit$', views.UserEdit.as_view(), name="user_edit"),
    url(r'^user/(?P<pk>[0-9]+)/delete$', views.UserDelete.as_view(), name="user_delete"),
    url(r'^user/register$', views.RegisterUser.as_view(), name="register"),
    #company views
    url(r'^company/$', views.CompaniesListView.as_view(), name="company"),
    url(r'^company/add$', views.CompanyAdd.as_view(), name="company_add"),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetailView.as_view(), name="detail"),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', views.CompanyUpdate.as_view(), name="company_edit"),
    url(r'^company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name="company_delete"),
    #TODO add company pk here...
    url(r'^company/addcontact', views.ContactAdd.as_view(), name="contact_add"),
    url(r'^company/(?P<pk>[0-9]+)/editcontact', views.ContactEdit.as_view(), name="edit_contact"),
    url(r'^company/(?P<pk>[0-9]+)/deletecontact', views.ContactDelete.as_view(), name="delete_contact"),
    #TODO add company pk here
    # url(r'^company/addorder', views.OrderAdd.as_view(), name="order_add"),
    url(r'^company/(?P<pk>[0-9]+)/addorder', views.OrderAdd.as_view(), name="order_add"),    
    url(r'^company/(?P<pk>[0-9]+)/orderedit', views.OrderEdit.as_view(), name="order_edit"),
    url(r'^company/report$', views.company_report, name="company_report"),
]
