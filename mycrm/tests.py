'''
Unittests

TODO

'''
from django.core.exceptions import ValidationError
from django.test import TestCase

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
        result = validators.validate_phone('123-123----')
        self.assertRaises(ValidationError)
        self.assertFalse(result, 'success')
