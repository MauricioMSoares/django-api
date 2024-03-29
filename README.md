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

### Django REST API additional requirements

```
pip install djangorestframework
pip install django-filter
pip install markdown
```

Make sure to add rest_framework on settings.py, INSTALLED_APPS.

### Django OAuth2 dependency installing

```
pip install django-rest-framework-social-oauth2
cd project_name
python manage.py makemigrations
python manage.py migrate
```

Make sure to add oauth2_provider, social_django and rest_framework_social_oauth2 on settings.py, INSTALLED_APPS. <br>
Also, make sure to add social_django.context_processors.backends and social_django.context_processors.login_redirect on settings.py, TEMPLATES. <br>
Next, add the following line inside your urls.py

```
auth_api_urls = [
    path(r"", include("rest_framework_social_oauth2.urls")),
]
```

Then, define oauth2_provider.contrib.rest_framework.OAuth2Authentication and rest_framework_social_oauth2.authentication.SocialAuthentication on settings.py, REST_FRAMEWORK. <br>
Lastly, set the following dictionary on settings.py:

```
AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'rest_framework_social_oauth2.backends.DjangoOAuth2'
}
```