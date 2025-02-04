#!/bin/bash

SHARED_FILE="/usr/src/shared/admin_info.json"

echo "Waiting for admin_info.json to be created by user-api..."
while [ ! -f "$SHARED_FILE" ]; do
  sleep 1
done

# Ensure the file contains the expected DB_KEY
while ! grep -q '"DB_KEY":' "$SHARED_FILE"; do
  echo "Waiting for DB_KEY to be written..."
  sleep 1
done

export DB_KEY=$(jq -r '.DB_KEY' "$SHARED_FILE")
echo "DB_KEY successfully retrieved: $DB_KEY"

exec gunicorn --config gunicorn_config.py app:app
