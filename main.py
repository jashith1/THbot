from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager

from src.utils.bot import client
from src.utils.config import settings

from src.routes import helpr

@asynccontextmanager
async def lifespan(app: FastAPI):
    #use asyncio to spin up new task because client.start runs infinitely
    asyncio.create_task(client.start(settings.DISCORD_BOT_TOKEN))
    yield
    await client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(helpr.router)
