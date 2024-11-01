#!/bin/sh

python manage.py migrate --noinput

python manage.py collectstatic --noinput --clear

gunicorn core.wsgi:application --bind 0.0.0.0:8000
