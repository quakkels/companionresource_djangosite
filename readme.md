# Getting Started with Django

This Django application is a companion resource to my [Getting Started with Django](http://quakkels.com/posts/getting-started-python-django-vs-code/) article.

I recommend using a Virtual Environment (venv) when running this project locally using Python version 3.6.5 or above.

## Installation
1. Clone this repository
1. Activate your venv
1. Execute `pip install -r requirements.txt`
1. Run data migrations `python manage.py migrate`
1. Create a super user `python manage.py createsuperuser`

Run locally with `python manage.py runserver`.