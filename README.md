# Django and React Integration Project

This project aims to be as minimal as possible and try to smoothly integrate react components
and possibly very flexible with generic react
applications

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


### Running the application

```sh
git clone https://github.com/peramsathyam/zero-to-django-pyreact.git
virtualenv dj-env
source dj-env/bin/activate
pip install -r requirements.txt
cd zero-to-django-pyreact/weavler
python manage.py runserver
```

And visit <http://localhost:8000/>

## Changing the port

You can change the port number by setting the `$PORT` environment variable before invoking any of the scripts above, e.g.,

```sh
python manage.py runserver 8080
```

## Django project and applications
The current project is build from scratch using `django` commands

```sh
django-admin startproject weavler
```

Which result in

```
weavler/
    manage.py
    weavler/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
Then we create the application `webshop` inside `weavler` project with the following command

```
cd weavler
python manage.py startapp webshop
```

Which create a `app` inside `weavler` and the whole
project with a application looks like

```
weavler/
  manage.py
  weavler/
    __init__.py
    settings.py
    urls.py
    wsgi.py
  webshop/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

`weavler` folder is the project environment container
where the settings[`weavler/settings.py`] is configured such `database` including other project related configurations.

`application` such as `webshop` will not be available
for the project until it is configured in `settings.py`
of `weavler` project.  

NOTE: **migrations** folder inside every `apps` are auto-generated, however they are not included in `.gitignore`

Please [readmore](https://docs.djangoproject.com/en/1.9/topics/migrations/)
