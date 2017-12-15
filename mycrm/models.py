'''
Database models for mycrm
'''
#core Django imports
from django.db import models
from django.contrib.auth.models import User

#local imports
from .validators import validate_phone


class Company(models.Model):
    '''
    Company data, display on company list
    '''
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=4500)
    picture = models.CharField(max_length=500, null=True, default=None)
    # picture = models.ImageField(upload_to="images", blank=True, null=True) #picture field change require delete whole database
    ranking_position = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class Comment(models.Model):
    '''
    Company comment
    related to user and company
    '''
    title = models.CharField(max_length=128, default=None)
    comment = models.TextField(max_length=4000)

    #current time when coment post
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title

class BusinessCard(models.Model):
    '''
    Business card has user data corresponding to company
    '''
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=20, validators=[validate_phone])
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name = 'Business Card'
        verbose_name_plural = 'Business Cards'

    def __str__(self):
        return self.name


class Order(models.Model):
    '''
    Order has all orders corresponding to one company. Company can have many orders
    '''
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    value = models.DecimalField(max_digits=12, decimal_places=2) #value in euro
    payment_status = models.BooleanField(default=False) #true if client already pait us for order
    date_created = models.DateField() #date created
    project_is_finished = models.BooleanField(default=False) #tells if project is finished
    company = models.ForeignKey(Company) #for who we make project

    @property
    def sum_quantity(self):
        '''
        calculate all bills sum, total display on companies list view
        '''
        total=sum([obj.value for obj in Order.objects.filter(company=self.company.pk)])
        return total

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.name

