gunicorn mahindarama.wsgi:application --env DJANGO_SETTINGS_MODULE=mahindarama.settings.local_proxy

python manage.py makemigrations

# DJANGO_SETTINGS_MODULE=mahindarama.settings.local_proxy python manage.py migrate