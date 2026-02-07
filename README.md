# chroma-sync
Local-first backups and cloud durability for single-node Chroma

# Setup
- Ensure you have 

# Restoring
```shell
litestream restore -o chroma_db_backups/chroma.sqlite3 s3://chroma-backups.localhost:9000/chroma.sqlite3
```