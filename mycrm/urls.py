from django.conf import settings
from django.conf.urls import url, include
from . import views

app_name = 'mycrm'

urlpatterns=[
    url(r'^$', views.index_page, name="index_page_show"),
    url(r'^test_page/$', views.test_page, name="tst"),
    url(r'^user/$', views.user_page, name="user"),
    url(r'^company/$', views.CompaniesListView.as_view(), name="company"),
]

