from django.contrib import admin
from mycrm.models import User, Company, CompanyEmployerBusinessCard, Order

# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(CompanyEmployerBusinessCard)
admin.site.register(Order)