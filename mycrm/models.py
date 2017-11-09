from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=128)
    ranking_position = models.IntegerField(default=0)
    # worker = models.ManyToManyField('self', through='CompanyEmployerBusinessCard', symmetrical=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


#example filter models.Company.objects.filter(card__name='Marcin').all()
class CompanyEmployerBusinessCard(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    company = models.ForeignKey(Company, related_name='cards', related_query_name='card')

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

