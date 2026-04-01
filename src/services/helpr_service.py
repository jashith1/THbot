from src.utils.bot import client
from src.utils.config import settings
from src.exceptions.custom_exceptions import ChannelNotFound

class HelprService():
    async def ping_mentor(self):
        channel = client.get_channel(settings.MENTOR_CHANNEL_ID)
        if channel:
            #roles need to be prefixed with &
            await channel.send(f"<@&{settings.MENTOR_ROLE_ID}>\nThere's a new ticket!")
            return { "status_code": 200, "message": "Message sent to mentors!" }
        else:
            raise ChannelNotFound(str(settings.MENTOR_CHANNEL_ID))
