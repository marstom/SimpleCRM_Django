'''
App root

'''
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

#import django.contrib.auth.urls
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/mycrm/login')),
    #crm dashboard
    url(r'^mycrm/', include('mycrm.urls')),
    #password reset pages
    url(r'^accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns