from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'mycrm'

urlpatterns=[
    url(r'^$', views.index_page, name="index_page_show"),
    url(r'^test_page/$', views.test_page, name="tst"),
    url(r'^user/$', views.user_page, name="user"),
    url(r'^user/register$', views.RegisterUser.as_view(), name="registeruser"),
    url(r'^logout/$', views.logout_crm, name="logout"),
    url(r'^company/$', views.CompaniesListView.as_view(), name="company"),
    url(r'^company/add$', views.CompanyAdd.as_view(), name="company_add"),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetailView.as_view(), name="detail"),
]

