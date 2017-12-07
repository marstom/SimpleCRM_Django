import os
import re

print('This is TUTORIAL')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
di = os.path.join(BASE_DIR, 'mycrm', 'static', 'asdf')
print(di)

print('string validation')

value = '12122-2-3-3'


reg = r'^[0-9,-]*$'
rule = re.compile(reg)
print(rule.match(value))