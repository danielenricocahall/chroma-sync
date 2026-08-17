#!/bin/bash
set -e
export BUCKET_NAME="chroma-backups"
export OBJECT_PATH="chroma.sqlite3"
export CHROMADB_PERSISTENT_PATH="./chroma_db"
export AWS_ENDPOINT_URL="http://localhost:4566"
export AWS_REGION="us-east-1"
export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"

echo "🚀 Starting chroma-sync..."

echo "Creating Python environment"
uv sync
echo "📦 Starting Floci..."
docker-compose up -d

echo "⏳ Waiting for Floci to be ready..."
for _ in {1..30}; do
  if curl -fs "$AWS_ENDPOINT_URL/_floci/health" > /dev/null; then
    break
  fi
  sleep 1
done

echo "🪣 Creating bucket..."
uv run python create_bucket.py

echo "✅ Setup complete!"
echo ""
echo "🔄 Running Litestream with ChromaDB..."
uv run python hydrate_database.py
litestream replicate -config litestream.yml
