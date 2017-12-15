'''
Unittests in django-pytest

using pytest:

create file pytest.ini and set project settings file

command line:
>pytest
>pytest -s print all log and prints output

'''
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from .models import Company, Order
# Create your tests here.

#local imports
from logger import logger


class TestValidators(TestCase):
    def test_validator_phone(self):
        from . import validators
        result = validators.validate_phone('123-123')
        self.assertRaises(ValidationError)
        self.assertTrue(result, 'success')

    def test_validator_phone_digits(self):
        from . import validators
        result = validators.validate_phone('123424234424247672936952')
        self.assertRaises(ValidationError)
        self.assertTrue(result, 'success')

    def test_validator_phone_empty(self):
        '''
        Test should not pass, must fix regex
        :return:
        '''
        from . import validators
        result = validators.validate_phone('123-123')
        #self.assertRaises(ValidationError)
        self.assertTrue(result, 'success')

class TestModel(TestCase):
    def test_comp(self):
        from .models import Company
        company = Company(name='Camel', description='This is description', picture='none')
        self.assertIn(company.name, 'Camel')


class TestCompanyView(TestCase):
    '''
    Tests if user can login to system
    '''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('john', 'lennon@beatles.com', 'johnpassword')
        self.company = Company.objects.create(name='TheBeatles', description='hahaha')
        self.company2 = Company.objects.create(name='motor', description='desc')
        self.company3 = Company.objects.create(name='Harley Davidson', description='Oldschool')
        self.order = Order.objects.create(name='cd-album', description='Hey this is John lennon cd', company=self.company, value=Decimal('1200'), date_created='2017-11-11')


    def test_company_view(self):
        '''
        Creating object in create view
        '''
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('mycrm:company')) #client is like webbrowser
        logger.info('response {}'.format(resp.status_code))
        logger.info('companypk {}'.format(resp.context['object_list'].get(pk=1)))
        album = '{}'.format(resp.context['object_list'].get(pk=1).order_set.get(pk=1).description)
        logger.info(album)
        logger.info('data {}'.format(self.company.order_set.name))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(album, 'Hey this is John lennon cd')

    def test_company_view_companies_list(self):
        self.client.login(username='john', password='johnpassword')
        resp = self.client.get(reverse('mycrm:company'))  # client is like webbrowser
        content = resp.context['object_list'].all()
        logger.info('records {}'.format(content))
        length = len(content)
        print('printed something in pytest!!!')
        self.assertEqual(resp.status_code, 200)#success
        self.assertIs(length, 3)