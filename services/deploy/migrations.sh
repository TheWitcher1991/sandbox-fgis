#!/bin/sh

echo "Running makes migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate --skip-checks

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"