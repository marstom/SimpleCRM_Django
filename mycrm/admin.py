'''
These models are visible in django-admin page
'''
#core Django imports
from django.contrib import admin
#Import from current app
from .models import Company, BusinessCard, Order

# Register your models here.
admin.site.register(Company)
admin.site.register(BusinessCard)
admin.site.register(Order)