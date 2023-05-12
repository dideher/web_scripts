#! /usr/bin/env sh
set -e

#Run prestart.sh if it exists.
PRE_START_PATH=./docker-files/prestart.sh
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no script $PRE_START_PATH"
fi

# Start Gunicorn
#gunicorn -c "$GUNICORN_CONF" "$APP_MODULE" &
gunicorn -c "$1" "$2" &
# Start Nginx
nginx -g "daemon off;"


# APP_MODULE="django_project.wsgi"
# GUNICORN_CONF="/substitute_professors/docker-files/gunicorn_conf.py"
