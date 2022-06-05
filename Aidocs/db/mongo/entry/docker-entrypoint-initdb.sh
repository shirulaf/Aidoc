#!/bin/bash
# this will only run for the first time a db is created and
# will create the user for the db
echo "Creating mongo user - $MONGODB_USER..."
mongo admin --host localhost -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD --eval "db.getSiblingDB('$MONGODB_DATABASE').createUser({user: '$MONGODB_USER', pwd: '$MONGODB_PASS', roles: [{role: 'readWrite', db: '$MONGODB_DATABASE'}]});"
echo "Mongo user created."