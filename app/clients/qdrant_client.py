# app/clients/qdrant_client.py

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.models import VectorParams, Distance
from app.schemas import RoomEmbeddingRequest

# qdrant client 생성
class QdrantDbClient:
    def __init__(self, url:str="http://localhost:6333"):
        self.client=QdrantClient(url=url)
        
    def ensure_collection(self, name:str):
        if not self.client.collection_exists(name):
            self.client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
                # text-embedding-3-small은 차원수 1536, 벡터유사도 계산방식 COSINE 추천
                # nlpai-lab/KURE-v1은 차원수 1024
        )
            
    def upsert(self, name:str, target:RoomEmbeddingRequest, vector):
        info = self.client.upsert(
            
            collection_name=name,
            wait=True,
            points=[PointStruct(id=target.roomNo, vector=vector, payload={"roomNo":target.roomNo, "text":target.text})],
        )
        print(info)