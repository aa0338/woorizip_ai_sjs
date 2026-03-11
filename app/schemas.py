# app/schemas.py

from datetime import datetime

from pydantic import BaseModel


class RoomRequest(BaseModel):
    roomNo: str
    roomName: str
    houseNo: str
    houseName: str
    roomCreatedAt: datetime
    roomUpdatedAt: datetime
    roomDeposit: int
    roomMonthly: int
    roomMethod: str
    roomArea: float
    roomFacing: str
    roomAvailableDate: datetime
    roomAbstract: str
    roomRoomCount: int
    roomBathCount: int
    roomEmptyYn: bool
    roomStatus: str
    roomOptions: str
    imageSummary: str
    reviewSummary: str
    
    
class RoomSummaryRequest(BaseModel):
    roomNo: str
    text: list
