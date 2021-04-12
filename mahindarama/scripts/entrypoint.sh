#!/bin/bash

/usr/local/bin/gunicorn mahindarama.wsgi:application --bind "0.0.0.0:$PORT" --env DJANGO_SETTINGS_MODULE=mahindarama.settings.production