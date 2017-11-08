from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=128)
    ranking_position = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class CompanyEmployerBusinessCard(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    value = models.DecimalField(max_digits=12, decimal_places=2) #value in euro
    payment_status = models.BooleanField(default=False) #true if client already pait us for order
    date_created = models.DateField() #date created
    project_is_finished = models.BooleanField(default=False) #tells if project is finished
    company = models.ForeignKey(Company) #for who we make project

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.name

class User(models.Model):
    '''
    CRM user
    '''
    username = models.CharField(max_length=30)
    # name = models.CharField(max_length=30)
    # surname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name