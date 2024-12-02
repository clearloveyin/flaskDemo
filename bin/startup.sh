#! /bin/sh

/bin/bash ./docker/wait-for-services.sh
/bin/bash ./docker/prepare-db.sh

export $(cat .env | xargs)

export $(cat .flaskenv | xargs) && gunicorn -c settings/gunicorn.py "lib.create_app:create_app()"
