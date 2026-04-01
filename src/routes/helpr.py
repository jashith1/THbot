from fastapi import APIRouter, Request
from src.deps import HelprDep 

router = APIRouter(
    prefix="/helpr",
    tags=["helpr"],
)

@router.get("/test")
async def test( request: Request, service: HelprDep, ):
    return await service.test()

