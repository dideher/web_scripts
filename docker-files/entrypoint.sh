#!/usr/bin/env sh
set -e

export APP_MODULE="config.wsgi"
export GUNICORN_CONF=/web_scripts/docker-files/gunicorn_conf.py

#exec "$@"
