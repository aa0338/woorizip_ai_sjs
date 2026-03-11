# app/services/embedding_service.py
# 텍스트 -> 임베딩 벡터 반환

from app.clients.embedding_client import KureEmbeddingClient, OpenaiEmbeddingClient

class EmbeddingService:
    def __init__(self, client:KureEmbeddingClient):
        self.client=client
    
    def embed(self, text:str):
        return self.client.embed(text)