import os

import chromadb
persistent_path = os.environ["CHROMADB_PERSISTENT_PATH"]
client = chromadb.PersistentClient(path=persistent_path)
collection_name = "chroma-sync-testing"
try:
    collection = client.get_collection(collection_name)
    print(f"Using existing collection {collection_name}")
except:
    collection = client.create_collection("all-my-documents")
    print(f"Created new collection {collection_name}")

# Add some documents
collection.add(
    documents=["This is a document about the persistent client.", "Another document here."],
    metadatas=[{"source": "doc1"}, {"source": "doc2"}],
    ids=["id1", "id2"]
)

print("Added documents to collection")
print(f"Collection now has {collection.count()} documents")

