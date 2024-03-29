# django-api

### Configuring virtualenv and requirements.txt

```
pip install virtualenv
virtualenv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

### Starting a Django Project

```
django-admin startproject project_name
cd project_name
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Creating Django Apps inside of the Main Project

```
cd project_name
python manage.py startapp app_name
```

Then, on your main project, settings.py, add the name of the app you just created in the INSTALLED_APPS list. <br>
Next, inside your app's models.py, create a class for your Model.