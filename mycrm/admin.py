from django.contrib import admin
from mycrm.models import Company, BusinessCard, Order

# Register your models here.

admin.site.register(Company)
admin.site.register(BusinessCard)
admin.site.register(Order)