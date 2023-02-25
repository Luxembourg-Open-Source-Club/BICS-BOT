import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction

from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID, CATEGORY_STUDY_GROUPS


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
        description="Creating a study group. Example: /create_study_group Awesome-LA1-Study-Group John D, Jane D, Adam S",
    )
    async def create_study_group(
        self,
        interaction: Interaction,
        group_name: str = nextcord.SlashOption(description="Name of the group", required=True),
        names: str = nextcord.SlashOption(description="The group members. Use server names, separate names with comma and a space after.", required=True),
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
            # The user has no roles. So he must first use this command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return
        elif nextcord.utils.get(interaction.user.roles, name="Incoming"):
            # The user has the incoming role and thus not allowed to use this command
            msg = "You are not allowed to create study groups, you aren't a student :)"
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return
        
        member_count = len(names.split(", "))
        members = await self.get_members(interaction, names)
        if len(members) != member_count:
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", "Check the names you entered, and the format in which you entered them.", WARNING_LEVEL),
                ephemeral=True,
            )
            return

        topic = f"Study group {group_name} for {names}."
        category = interaction.guild.get_channel(CATEGORY_STUDY_GROUPS)
        overwrites = {
            interaction.guild.default_role: nextcord.PermissionOverwrite(read_messages=False)
        }
        text_channel = await interaction.guild.create_text_channel(group_name, topic=topic, category=category, overwrites=overwrites)
        voice_channel = await interaction.guild.create_voice_channel(group_name, topic=topic, category=category, overwrites=overwrites)
        
        # for member in members:
        #     await text_channel.set_permissions(target=member, read_messages=True)
        #     await voice_channel.set_permissions(target=member, read_messages=True)
    
    async def get_members(self, interaction: Interaction, names: str) -> list[Interaction.user]:
        members: list[Interaction.user] = []
        for name in names.split(", "):
            print("for " + name)
            for member in interaction.guild.members:
                print("looking at " + member.display_name)
                if name == member.display_name:
                    print("found")
                    members.append(member)
                    break
            # f"The user {name} was not found on the server. Make sure you used the correct convention for inputting the names, and that you used the correct name."
        return members
        

def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CreateStudyGroupCmd(client))
