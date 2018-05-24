#!/bin/sh

cd /usr/src/app
echo "Enabling wsgi socket..."

"uwsgi", "--ini", "app.ini", "--uid","www-data","--gid","www-data"
uwsgi --ini app.ini && chown www-data:www-data app.sock

exec "$@"

