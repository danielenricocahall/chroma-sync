#!/bin/bash
export LITESTREAM_ACCESS_KEY_ID=test
export LITESTREAM_SECRET_ACCESS_KEY=test

litestream restore -o chroma_db_backups/chroma.sqlite3 s3://chroma-backups.localhost:4566/chroma.sqlite3
uv run python evaluate_restored_database.py
