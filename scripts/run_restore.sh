#!/bin/bash
export AWS_ACCESS_KEY=minioadmin
export AWS_SECRET_ACCESS_KEY=minioadmin
litestream restore -o chroma_db_backups/chroma.sqlite3 s3://chroma-backups.localhost:9000/chroma.sqlite3
uv run python evaluate_restored_database.py

