# Simple CRM in Django #

Simple app for customer and companies managment. Each user has privilige, admin can change user privilges. There are PDF reports.

### Installation ###
* create and activate virtualenv:

```bash
python3 -m venv ~/projekty/venv/CRM_Django
~/projekty/venv/pythonhacking-django/bin/activate
```

* pip install --upgrade -r requirements.txt
* migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```

### How to run app ###

```bash
python manage.py runserver
```
* create superuser
```bash
python manage.py createsuperuser
```