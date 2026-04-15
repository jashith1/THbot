from fastapi import APIRouter, Depends
from src.deps import Helpr
from src.utils.crypto import verify_hmac
from src.schemas import TicketDetails

router = APIRouter(
    prefix="/helpr",
    tags=["helpr"],
    dependencies=[Depends(verify_hmac)],
)

@router.post("/ping-mentor")
async def ping_mentor( ticket_details: TicketDetails, service: Helpr, ):
    return await service.ping_mentor(ticket_details)
