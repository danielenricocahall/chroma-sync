# Overview
The purpose of this project is to illustrate local-first backups and cloud durability for single-node [Chroma](https://github.com/chroma-core/chroma) using [Litestream](https://litestream.io/). 

# Setup
To tinker with this project, you'll need the following installed:
- [uv](https://docs.astral.sh/uv/) as it is required for creating the local Python environment.
- Docker , as it is required for running the MinIO server
- [litestream](https://litestream.io/install/), as we'll be using it for replicating the data from Chroma

# Running
For simplicity, everything has been consolidated into the `run.sh` script. You can run it with the following command:
```shell
chmod +x run.sh
./run.sh
```

This will start the MinIO server container (running at `http://localhost:9000`), create the Python environment via `uv`, create the bucket in MinIO, and run the `hydrate_database.py` script to create and populate the persistent Chroma database. Lastly, it will use `litestream` to replicate the persistent Chroma database to the MinIO bucket.

# Restoring
```shell
litestream restore -o chroma_db_backups/chroma.sqlite3 s3://chroma-backups.localhost:9000/chroma.sqlite3
```