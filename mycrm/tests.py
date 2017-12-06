'''
Unittests

TODO

'''
from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
import logging
logger = logging.getLogger(__name__)


class TestValidators(TestCase):
    def test_validator_phone(self):
        from . import validators
        validators.validate_phone('123-123')
        self.assertRaises(ValidationError)
        # with self.assertRaises(ValidationError) as cm:
        #     logger.error(cm)
        # self.assertRaisesMessage(ValidationError, expected_message='This is not valid phone number, digits must be separated - or in one line. Example: 12-123-123-123')
