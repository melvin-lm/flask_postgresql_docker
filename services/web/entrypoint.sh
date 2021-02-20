#!/bin/sh

echo "Waiting for postgres..."

# port scanning with netcat. While database is not up and healthy, sleep. 
while ! nc -z $POSTGRESQL_HOST $POSTGRESQL_PORT; do
	sleep 0.1
done

echo "PostgreSQL started"

exec "$@"
