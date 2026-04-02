from src.utils.bot import client
from src.exceptions.custom_exceptions import ChannelNotFound
from src.schemas import TicketDetails
from src.messages import TicketMessages
from src.utils.config import settings

class HelprService():
    async def ping_mentor(self, ticket_details: TicketDetails):
        channel = client.get_channel(settings.MENTOR_CHANNEL_ID)
        if channel:
            #roles need to be prefixed with &
            ticket_message = TicketMessages.ticket_created(ticket_details)
            await channel.send(ticket_message)
            return { "status_code": 200, "message": "Message sent to mentors!" }
        else:
            raise ChannelNotFound(str(settings.MENTOR_CHANNEL_ID))
