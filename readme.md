# README #

### Installation ###
* create virtualenv:

```bash
python3 -m venv ~/projekty/venv/CRM_Django
~/projekty/venv/pythonhacking-django/bin/activate
```

* pip install --upgrade -r requirements.txt



### Simple CRM in Django ###

* create database
```bash
python manage.py makemigrations
python manage.py migrate
```

### How to run app ###

```bash
python manage.py runserver
```

* create superuser

python manage.py createsuperuser