import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction

from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID, CATEGORY_STUDY_GROUPS


class CalendarCmd(commands.Cog):
    """This class represents the commands to interact with the calendar system.

    </calendar_add> will let students enter a HW or an exam into the calendar 
        system with various details about the assignment/exam for their year.

    </calendar_delete> will let students remove multiple entries from the 
        calendar from their year.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Allow students to enter a HW/exam into the calendar with info such as deadline.",
    )
    async def calendar_add():
        pass

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Allow students to remove a HW/exam from the calendar.",
    )
    async def calendar_delete():
        pass        

def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CalendarCmd(client))
