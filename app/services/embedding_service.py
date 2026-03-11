# app/services/embedding_service.py
# 텍스트 -> 임베딩 벡터 반환
# text-embedding-3-small은 차원수 1536

from app.clients.embedding_client import KureEmbeddingClient, OpenaiEmbeddingClient

class EmbeddingService:
    def __init__(self, client:KureEmbeddingClient|OpenaiEmbeddingClient):
        self.client=client
    
    def embed(self, text:str):
        return self.client.embed(text)