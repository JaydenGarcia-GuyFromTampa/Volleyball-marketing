#!/bin/sh
set -e
# Wait for PostgreSQL
echo "Waiting for database..."
until python -c "
import os, sys
import psycopg
try:
    conn = psycopg.connect(
        dbname=os.environ.get('POSTGRES_DB', 'volleyball_marketing'),
        user=os.environ.get('POSTGRES_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        host=os.environ.get('POSTGRES_HOST', 'db'),
        port=os.environ.get('POSTGRES_PORT', '5432'),
        connect_timeout=5
    )
    conn.close()
except Exception as e:
    sys.exit(1)
" 2>/dev/null; do
  sleep 2
done
echo "Database is up."
echo "Running migrations..."
python manage.py migrate --noinput
echo "Starting server..."
exec "$@"
