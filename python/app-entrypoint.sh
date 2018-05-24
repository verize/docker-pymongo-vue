#!/bin/sh

cd /usr/src/app
echo "Enabling wsgi socket..."

uwsgi --ini app.ini && chown www-data:www-data run/app.sock

mkdir -p build
echo "<h1>hello world</h1>" >> build/index.html

exec "$@"

