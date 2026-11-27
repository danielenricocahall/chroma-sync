# Overview
The purpose of this project is to illustrate local-first backups and cloud durability for single-node [Chroma](https://github.com/chroma-core/chroma) using [Litestream](https://litestream.io/). While this was done with [Floci](https://floci.io/) (a local AWS emulator) for local development, the same principles can be applied to other object stores.

# Setup
To tinker with this project, you'll need the following installed:
- [uv](https://docs.astral.sh/uv/) as it is required for creating the local Python environment.
- Docker , as it is required for running the Floci emulator
- [litestream](https://litestream.io/install/), as we'll be using it for replicating the data from Chroma

# Running
## Initial Setup
For simplicity, everything has been consolidated into the `run_replication.sh` script:
```shell
chmod +x ./scripts/run_replication.sh
./scripts/run_replication.sh
```

This will start the Floci container (with the S3-compatible API running at `http://localhost:4566`), create the Python environment via `uv`, create the bucket via the `create_bucket.py` script, and run the `hydrate_database.py` script to create and populate the persistent Chroma database. Lastly, it will use `litestream` to replicate the persistent Chroma database to the bucket.

## Restoring
To validate the database has been properly replicated, it can be restored using `run_restore.sh` script:  

```shell
chmod +x ./scripts/run_restore.sh
./scripts/run_restore.sh
```

This will configure the `AWS` environment variables, run `litestar restore` to restore the original database to `chroma_db_backups`, and run the `evaluate_restored_database.py` script to validate the restored database as well as add new documents.

## Cleanup
To cleanup the resources after testing, 

```shell
chmod +x ./scripts/cleanup.sh
./scripts/cleanup.sh
```

This will remove the Floci container (along with its data volume) and delete the corresponding data directories.

# Notes
- Floci runs with throwaway credentials (`test`/`test`) and signature validation disabled, which is fine for local development. Against a real object store (S3, MinIO, R2, etc.), only the endpoint and credentials in `litestream.yml` need to change.
- For simplicity, this was done using the default settings. If the `PersistentClient` or corresponding Chroma collection is created using different settings (e.g., different embedding functions, different default database or tenant, etc.), these configurations will need to be specified when interacting with the restored database. 
  - For managing shared configuration, consider using something like AWS AppConfig or similar services to manage shared configurations across different environments and services.
  - Alternatively, if managed via version control and sharing across users, ensure that configuration files are checked into a repository and versioned appropriately.