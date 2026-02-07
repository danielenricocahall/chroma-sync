import os
import chromadb

persistent_path = os.environ.get("CHROMADB_PERSISTENT_PATH", "chroma_db_backups")
client = chromadb.PersistentClient(path=persistent_path)
collection_name = "chroma-sync-testing"
try:
    collection = client.get_collection(collection_name)
    print(f"Using existing collection {collection_name}")
except:
    collection = client.create_collection(collection_name)
    print("Created new collection")

print(f"Collection {collection_name} currently has {collection.count()} documents")

# Add some documents
collection.add(
    documents=["This is yet another document about the persistent client.", "heheheh"],
    metadatas=[{"source": "doc3"}, {"source": "doc4"}],
    ids=["id3", "id4"]
)

print("Added documents to collection")
print(f"Collection now has {collection.count()} documents")

