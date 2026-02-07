#!/bin/bash
set -e

echo "🧹 Cleaning up chroma-sync environment..."

# Stop and remove containers
docker-compose down -v

# Remove chroma data directory
rm -rf chroma_data

echo "✅ Cleanup complete!"
