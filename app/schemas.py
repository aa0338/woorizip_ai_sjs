# app/schemas.py

from pydantic import BaseModel

# 
class RoomEmbeddingRequest(BaseModel):
    roomNo: str
    text: str
    
class RoomSummaryRequest(BaseModel):
    roomNo: str
    roomInfo: str