#!/bin/bash
set -e

echo "🧹 Cleaning up chroma-sync environment..."

# Stop and remove containers
docker-compose down -v

rm -rf chroma_db
rm -rf chroma_db_backups

echo "✅ Cleanup complete!"
