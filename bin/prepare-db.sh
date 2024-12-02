#! /bin/sh

source .env

export PYTHONPATH='.'

echo "run db init"
flask db init

echo "run db migrate"
flask db migrate

echo "run db upgrade"
flask db upgrade

echo "run initialize"
flask initialize

echo "db done"

