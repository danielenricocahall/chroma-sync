#!/bin/bash
set -e

echo "🧹 Cleaning up chroma-sync environment..."

docker-compose down -v

rm -rf chroma_db
rm -rf chroma_db_backups

echo "✅ Cleanup complete!"
