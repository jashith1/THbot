from fastapi import Depends
from typing import Annotated
from src.services.helpr_service import HelprService

async def get_helpr_service() -> HelprService:
    return HelprService()

HelprDep = Annotated[HelprService, Depends(get_helpr_service)]
