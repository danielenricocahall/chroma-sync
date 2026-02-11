#!/bin/bash
export LITESTREAM_ACCESS_KEY_ID=minioadmin
export LITESTREAM_SECRET_ACCESS_KEY=minioadmin

litestream restore -o chroma_db_backups/chroma.sqlite3 s3://chroma-backups.localhost:9000/chroma.sqlite3
uv run python evaluate_restored_database.py

