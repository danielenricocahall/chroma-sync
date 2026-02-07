import os
import chromadb

persistent_path = os.environ.get("CHROMADB_PERSISTENT_PATH", "chroma_db_backups")
client = chromadb.PersistentClient(path=persistent_path)

try:
    collection = client.get_collection("all-my-documents")
    print("Using existing collection")
except:
    collection = client.create_collection("all-my-documents")
    print("Created new collection")

# Add some documents
collection.add(
    documents=["This is yet another document about the persistent client.", "heheheh"],
    metadatas=[{"source": "doc3"}, {"source": "doc4"}],
    ids=["id3", "id4"]
)

print("Added documents to collection")
print(f"Collection now has {collection.count()} documents")

