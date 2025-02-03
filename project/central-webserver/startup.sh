#!/bin/bash

SHARED_FILE="/usr/src/shared/admin_info.json"

echo "Waiting for DB_KEY..."
while [ ! -f "$SHARED_FILE" ]; do
  sleep 1
done

export DB_KEY=$(jq -r '.DB_KEY' "$SHARED_FILE")
echo "DB_KEY successfully retrieved"

# Use exec to replace the script process with Gunicorn
exec gunicorn --config gunicorn_config.py app:app
