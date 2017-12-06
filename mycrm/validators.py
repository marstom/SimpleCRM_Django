#stdlib
import re
#django
from django.core.exceptions import ValidationError

def validate_phone(value):
    '''
    Check if phone contains only digits and - characters
    :param value:
    :return: None
    '''

    reg = r'^[0-9,-]*$'
    rule = re.compile(reg)
    result = rule.match(value)
    print(rule.match(value))

    if not result:
        print(value, type(value))
        msg = "This is not valid phone number, digits must be separated - or in one line. Example: 12-123-123-123"
        raise ValidationError(msg)