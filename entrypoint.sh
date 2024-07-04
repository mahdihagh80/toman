#!/bin/bash

python manage.py migrate

celery -A toman beat --detach

celery -A toman worker --detach

gunicorn toman.wsgi:application --bind 0.0.0.0:8000
