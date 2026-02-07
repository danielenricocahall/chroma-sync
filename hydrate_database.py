import os

import chromadb
persistent_path = os.environ["CHROMADB_PERSISTENT_PATH"]
client = chromadb.PersistentClient(path=persistent_path)
collection_name = "sterling-cooper-accounts"
try:
    collection = client.get_collection(collection_name)
    print(f"Using existing collection {collection_name}")
except:
    collection = client.create_collection(collection_name)
    print(f"Created new collection {collection_name}")

# Add some documents
collection.add(
    documents=[
        "Roger Sterling closed the Mohawk Airlines account over martinis at lunch.",
        "Pete Campbell brought in the Clearasil account, proving himself as an account man."
    ],
    metadatas=[{"source": "doc1"}, {"source": "doc2"}],
    ids=["id1", "id2"]
)

print("Added documents to collection")
print(f"Collection now has {collection.count()} documents")

