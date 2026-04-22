#!/bin/sh

set -e

echo "Waiting for DB..."

# run migrations
python manage.py migrate

echo "Creating superuser..."

python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
password = "admin"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password)
    print("Superuser created")
else:
    print("Superuser already exists")
END

echo "Starting server..."

exec python manage.py runserver 0.0.0.0:8080