#!/bin/bash
set -e
export BUCKET_NAME="chroma-backups"
export OBJECT_PATH="chroma.sqlite3"
export CHROMADB_PERSISTENT_PATH="./chroma_db"

echo "🚀 Starting chroma-sync..."

echo "Creating Python environment"
uv sync
echo "📦 Starting MinIO..."
docker-compose up -d

echo "⏳ Waiting for MinIO to be ready..."
sleep 3

echo "🪣 Creating bucket..."
docker exec chroma-minio mc alias set local http://localhost:9000 minioadmin minioadmin
docker exec chroma-minio mc mb local/$BUCKET_NAME --ignore-existing

echo "✅ Setup complete!"
echo ""
echo "🔄 Running Litestream with ChromaDB..."
uv run python hydrate_database.py
litestream replicate -config litestream.yml
