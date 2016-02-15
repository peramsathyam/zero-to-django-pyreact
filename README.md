# Django and React Integration Project

This project aims to be as minimal as possible and try to smoothly integrate react components
and possibly very flexible with generic react
applications

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


### Running the application

```sh
virturalenv dj-env
source dj-env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

And visit <http://localhost:8000/>

## Changing the port

You can change the port number by setting the `$PORT` environment variable before invoking any of the scripts above, e.g.,

```sh
python manage.py runserver 8080
```
