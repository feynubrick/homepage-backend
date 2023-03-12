#!/bin/bash

if [ "$RUN_ENV" == "prod" ]; then
  echo "============================"
  echo "<< PRODUCTION ENVIRONMENT >>"
  echo "============================"
  gunicorn --bind :"$DJANGO_PORT" project.configs.wsgi:application
elif [ "$RUN_ENV" == "local" ]; then
  echo "======================="
  echo "<< LOCAL ENVIRONMENT >>"
  echo "======================="
  python manage.py runserver "$DJANGO_HOST:$DJANGO_PORT"
else
  echo "ERROR: '$RUN_ENV' IS INVALID RUN_ENV" >&2
  exit 1
fi
