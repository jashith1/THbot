from fastapi import APIRouter
from src.deps import HelprDep 
from src.schemas import TicketDetails

router = APIRouter(
    prefix="/helpr",
    tags=["helpr"],
)

#TODO: Need to add some kinda authentication
@router.post("/ping-mentor")
async def ping_mentor( ticket_details: TicketDetails, service: HelprDep, ):
    return await service.ping_mentor(ticket_details)
