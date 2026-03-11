# app/store/vector_store.py


# Add vectors
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.models import VectorParams, Distance

from app.clients.qdrant_client import QdrantDbClient
from app.schemas import RoomEmbeddingRequest


class VectorStore:
    def __init__(self, client: QdrantDbClient):
        self.client = client
    
    def room_vector_store(self, collection_name, target:RoomEmbeddingRequest, vector):
        self.client.ensure_collection(collection_name)
        self.client.upsert(collection_name, target, vector)