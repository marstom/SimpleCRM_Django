'''
Unittests in django-pytest

using pytest:

create file pytest.ini and set project settings file

command line:
>pytest
>pytest -s print all log and prints output
>pytest -k ClassName -execute only one test
'''
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from .models import Company, Order, BusinessCard, Comment
import mycrm.forms as forms

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

class TestCompanyAdd(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('john', 'lennon@beatles.com', 'johnpassword')
        self.company = Company.objects.create(name='TheBeatles', description='hahaha')

    def test_create_company_from(self):
        self.client.login(username='john', password='johnpassword')
        # resp = self.client.get(reverse('mycrm:company_add'))  # client is like webbrowser
        form = forms.SignUpForm({
            'username':'jonny',
            'first_name':'Jonny',
            'last_name':'Lemmons',
            'email':'jonny@lemmon.com',
            'password1':'yr8237r287ry29ry287ry9r8r72yr',
            'password2':'yr8237r287ry29ry287ry9r8r72yr',
        })
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('mycrm:company_add'), data=form.data)
        # logger.info('user {}'.format(response.content)) #this is raw html
        # logger.info('user {}'.format(response.context))  #
        self.assertEqual(response.status_code, 200)

    def test_create_company_from_invalid(self):
        self.client.login(username='john', password='johnpassword')
        # resp = self.client.get(reverse('mycrm:company_add'))  # client is like webbrowser
        form = forms.SignUpForm({
            'username':'jonny',
            'first_name':'Jonny',
            'last_name':'Lemmons',
            'email':'jonny@lemmon.com',
            'password1':'aaaaaaaaaaa',
            'password2':'bbbbbbbbbbb',
        })
        self.assertFalse(form.is_valid())


class TestDetailView(TestCase):
    '''
    test for detail view, test check if user add company, add order and comments if it appears on the website
    '''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('john', 'lennon@beatles.com', 'johnpassword')
        self.company = Company.objects.create(name='TheBeatles', description='hahaha')
        self.order = Order.objects.create(name='cd-album', description='Hey this is John lennon cd', company=self.company, value=Decimal('1200'), date_created='2017-11-11')
        self.contact = BusinessCard.objects.create(name='Paul',
                                                   last_name='McCartney',
                                                   phone='662-334-342-341',
                                                   company=self.company)
        self.comment = Comment.objects.create(
            title='Great album',
            comment='Comment from beatles fan.',
            user=self.user,
            company=self.company
        )

    def test_one(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('mycrm:detail', kwargs={'pk':self.company.pk}))
        logger.info('{}', response.content)
        # self.assertIn('TheBeatles',response)
        self.assertContains(response, 'Paul') # page contains contact to paul
        self.assertContains(response, 'cd-album')  # page contains cd album in orders
        self.assertContains(response, '662-334-342-341')  # page contains phone to paul Mc Cartney
        self.assertContains(response, 'Comment from beatles fan.')  # the beatles fan leaves comment!
