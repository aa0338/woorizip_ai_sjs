from fastapi import APIRouter, Request

from app.schemas import RoomSummaryRequest
from app.services.summary_service import SummaryService

router = APIRouter(
    prefix='/ai/summary'
)

@router.post("/room/summary/totalinfo", tags=["summary"], summary="방 정보 요약", description="방의 정보(기본정보+사진캡션요약+리뷰요약)를 종합 요약합니다.")
def roomSummary(roomSummaryRequest:RoomSummaryRequest, request:Request):
    summaryService=SummaryService(request.app.state.llmClient)
    room_info = roomSummaryRequest.text
    summary = summaryService.summaryRoomInfo(room_info)
    return {
        "status": True,
        "roomNo": roomSummaryRequest.roomNo,
        "summary": summary,
        "message": "방정보 종합 요약 성공"
    }
