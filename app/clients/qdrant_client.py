# app/clients/qdrant_client.py

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.models import VectorParams, Distance
from app.schemas import RoomRequest
from numpy import shape

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
            
    def room_upsert(self, name:str, target:RoomRequest, vector):
        (n, _) = vector.shape
        
        points=[]
        for i in range(0, n):
            points.append(PointStruct(id=target.roomNo+"-"+str(i), vector=vector[i], payload={"roomNo": target.roomNo}))
        
        info = self.client.upsert(
            collection_name=name,
            wait=True,
            points=points,
        )
        print(info)