from django.conf import settings
from django.conf.urls import url, include
import mycrm

app_name = 'mycrm'

urlpatterns=[
    url(r'^index/$', mycrm.index_page, name="index_page_show")
]

