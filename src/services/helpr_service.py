import discord
from src.utils.bot import client
from src.exceptions.custom_exceptions import ChannelNotFound, InvalidChannelType
from src.schemas import TicketDetails
from src.views.embeds import TicketEmbeds
from src.views.buttons import TicketButtons
from src.utils.config import settings

class HelprService():
    async def ping_mentor(self, ticket_details: TicketDetails):
        channel = client.get_channel(settings.MENTOR_CHANNEL_ID)
        if not channel:
            raise ChannelNotFound(str(settings.MENTOR_CHANNEL_ID))

        if not isinstance(channel, (discord.TextChannel)):
            raise InvalidChannelType("text channel", str(settings.MENTOR_CHANNEL_ID))

        mentor_ping = f"<@&{settings.MENTOR_ROLE_ID}>"
        embed = TicketEmbeds.ticket_created(ticket_details)
        view = TicketButtons(ticket_details)

        await channel.send(content=mentor_ping, embed=embed, view=view)
        return { "status_code": 200, "message": "Message sent to mentors!" }
