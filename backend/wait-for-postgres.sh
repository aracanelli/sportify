#!/bin/bash
set -e

echo "⏳ Waiting for Postgres..."

until pg_isready -h db -p 5432 -U spond_user
do
  sleep 1
done

echo "✅ Postgres is ready!"
exec "$@"
