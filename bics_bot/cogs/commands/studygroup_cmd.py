import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction, Guild

from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
from bics_bot.utils.channels_utils import retrieve_courses_text_channels_names
from bics_bot.utils.file_manipulation import read_txt
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID, ROLE_INTRO_LIST, CHANNEL_INTRO_ID, ROLE_ADMIN_ID


class CreateStudyGroupCmd(commands.Cog):
    """This class represents the command </create_study_group>

    The </create_study_group> command will let students create private text and voice 
    channels for their study groups.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Creating a study group",
    )
    async def create_study_group(
        self,
        interaction: Interaction,
        group_name: str = nextcord.SlashOption(description="Name of the group", required=True),
        member_amount: str = nextcord.SlashOption(description="Amount of people in the group", required=True),
    ) -> None:
        """
        The </create_study_group> command will let students manage private text and voice 
        channels for their study groups.

        Args:
            interaction: Required by the API. Gives meta information about
                the interaction.
            create: Bool value indicating if the student wants to create a 
                group or delete a group.

        Returns:
            None
        """

        if len(interaction.user.roles) == 1:
            # The user has no roles. So he must first use the /intro command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
        
        

def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CreateStudyGroupCmd(client))
