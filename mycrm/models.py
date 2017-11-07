from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    ranking_position = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=30)
    # name = models.CharField(max_length=30)
    # surname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name