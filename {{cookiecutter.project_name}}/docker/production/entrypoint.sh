#!/bin/sh

set -e

echo "Starting the gunicorn server with $((2 * $(nproc) + 1)) uvicorn workers..."
DJANGO_SETTINGS_MODULE="config.settings.production"
BIND="0.0.0.0:8000"
WORKERS=$((2 * $(nproc) + 1))
WORKER_CLASS="config.workers.CustomUvicornWorker"
MAX_REQUESTS=1000
TIMEOUT=120

gunicorn \
  --bind "$BIND" \
  --workers "$WORKERS" \
  --worker-class "$WORKER_CLASS" \
  --max-requests "$MAX_REQUESTS" \
  --timeout "$TIMEOUT" \
  config.asgi:application
