from django.contrib import admin
from mycrm.models import Company, CompanyEmployerBusinessCard, Order

# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyEmployerBusinessCard)
admin.site.register(Order)