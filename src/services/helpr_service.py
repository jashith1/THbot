from src.utils.bot import client
from src.utils.config import settings

class HelprService():
    async def test(self):
        channel = client.get_channel(settings.MENTOR_CHANNEL_ID)
        if channel:
            await channel.send("bruh")

        return "sent"
