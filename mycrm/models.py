from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    picture = models.CharField(max_length=500)
    ranking_position = models.IntegerField(default=0)
    # worker = models.ManyToManyField('self', through='CompanyEmployerBusinessCard', symmetrical=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class BusinessCard(models.Model):
    name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name = 'Business Card'
        verbose_name_plural = 'Business Cards'

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=2000)
    value = models.DecimalField(max_digits=12, decimal_places=2) #value in euro
    payment_status = models.BooleanField(default=False) #true if client already pait us for order
    date_created = models.DateField() #date created
    project_is_finished = models.BooleanField(default=False) #tells if project is finished
    company = models.ForeignKey(Company) #for who we make project

    @property
    def sum_quantity(self):
        total=sum([obj.value for obj in Order.objects.filter(company=self.company.pk)])
        return total

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.name

