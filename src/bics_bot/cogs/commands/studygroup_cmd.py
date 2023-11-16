import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction

from bics_bot.embeds.logger_embed import LogLevel, LoggerEmbed
from bics_bot.config.server_ids import (
    CATEGORY_STUDY_GROUPS,
)
from bics_bot.dropdowns.studygroup_dropdown import (
    StudyGroupLeaveView,
    StudyGroupInviteView,
)


class StudyGroupCmd(commands.Cog):
    """This class represents the command </create_study_group>

    The </create_study_group> command will let students create private text and voice
    channels for their study groups.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        description="Example: /studygroup_create Awesome LA1 Study Group @John D @Jane D @Adam S",
    )
    async def studygroup_create(
        self,
        interaction: Interaction,
        group_name: str = nextcord.SlashOption(
            description="Do not enter special characters.",
            required=True,
        ),
        names: str = nextcord.SlashOption(
            description="Mention `@` the study group members. Example: @John D @Jane D",
            required=True,
        ),
    ) -> None:
        """
        The </create_study_group> command will let students create private text and voice
        channels for their study groups.

        Args:
            interaction: Required by the API. Gives meta information about
                the interaction.
            group_name: `String` value representing the study group's name.
            names: The names of the study group members, retrieved in a Discord ID format.
                Example: '<@622007259424377748> <@224606608425044993> <@208934975432933696>'

        Returns:
            None
        """
        if len(interaction.user.roles) == 1:
            # The user has no roles. So he must first use this command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.WARNING),
                ephemeral=True,
            )
            return
        elif nextcord.utils.get(interaction.user.roles, name="Incoming"):
            # The user has the incoming role and thus not allowed to use this command
            msg = "You are not allowed to create study groups, you aren't a student :)"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.WARNING),
                ephemeral=True,
            )
            return

        group_name = group_name.lower()
        group_name = group_name.replace(" ", "-")
        group_name = group_name.replace("_", "-")

        for char in group_name:
            if not char.isalnum() and not char == "-":
                await interaction.response.send_message(
                    embed=LoggerEmbed(
                        f"Do not use {char} in group name.",
                        LogLevel.WARNING,
                    ),
                    ephemeral=True,
                )
                return

        # identical group name check
        for channel in interaction.guild.get_channel(
            CATEGORY_STUDY_GROUPS
        ).channels:
            if channel.name == group_name:
                await interaction.response.send_message(
                    embed=LoggerEmbed(
                        "Group name already in use. Enter a more unique group name.",
                        LogLevel.ERROR,
                    ),
                    ephemeral=True,
                )
                return

        members = await self.get_members(interaction, names)
        if not members:
            await interaction.response.send_message(
                embed=LoggerEmbed(
                    f"You need to enter users by mentioning them (use `@`).",
                    LogLevel.ERROR,
                ),
                ephemeral=True,
            )
        members.append(interaction.user)

        member_names = ", ".join([member.display_name for member in members])

        topic = f"Study group {group_name} for {member_names}."
        category = interaction.guild.get_channel(CATEGORY_STUDY_GROUPS)
        overwrites = self.get_overwrites(members)
        overwrites[
            interaction.guild.default_role
        ] = nextcord.PermissionOverwrite(read_messages=False)

        text_channel: nextcord.TextChannel = (
            await interaction.guild.create_text_channel(
                group_name,
                topic=topic,
                category=category,
                overwrites=overwrites,
            )
        )
        voice_channel: nextcord.VoiceChannel = (
            await interaction.guild.create_voice_channel(
                group_name, category=category, overwrites=overwrites
            )
        )

        await interaction.response.send_message(
            embed=LoggerEmbed(
                f"Text channel **{text_channel.name}** and voice channel **{voice_channel.name}** have been created.\n\nUsers *{member_names}* have been given access.",
            ),
            ephemeral=True,
        )

        return

    @application_command.slash_command(
        description="Example: /studygroup_leave. Just press ENTER, nothing more needed :)",
    )
    async def studygroup_leave(self, interaction: Interaction) -> None:
        """
        The </delete_study_group> command will let students remove their private text and voice
        channels for their study groups. The user must be in the group to delete the group.

        Args:
            interaction: Required by the API. Gives meta information about
                the interaction.

        Returns:
            None
        """

        if len(interaction.user.roles) == 1:
            # The user has no roles. So he must first use this command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.ERROR),
                ephemeral=True,
            )
            return
        elif nextcord.utils.get(interaction.user.roles, name="Incoming"):
            # The user has the incoming role and thus not allowed to use this command
            msg = "You are not allowed to create study groups, you aren't a student :)"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.ERROR),
                ephemeral=True,
            )
            return

        view = StudyGroupLeaveView(interaction)
        await interaction.response.send_message(
            view=view,
            ephemeral=True,
        )

    @application_command.slash_command(
        description="Example: /studygroup_invite awesome-la2-group @John D @Jane D",
    )
    async def studygroup_invite(
        self,
        interaction: Interaction,
        names: str = nextcord.SlashOption(
            description="Mention `@` the study group members. Example: @John D @Jane D",
            required=True,
        ),
    ) -> None:
        """ 
        The </studygroup_invite> will allow student to invite other students to their study group

        Args:
            interaction: Required by the API. Gives meta information about the interaction.
            names: Strings containing @ to add one or multiple members
        Returns:
            None
        """
        if len(interaction.user.roles) == 1:
            # The user has no roles. So he must first use this command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.ERROR),
                ephemeral=True,
            )
            return
        elif nextcord.utils.get(interaction.user.roles, name="Incoming"):
            # The user has the incoming role and thus not allowed to use this command
            msg = "You are not allowed to invite user to study groups, you aren't a student :)"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.WARNING),
                ephemeral=True,
            )
            return

        members = await self.get_members(interaction, names)
        if not members:
            await interaction.response.send_message(
                embed=LoggerEmbed(
                    f"You need to enter users by mentioning them (use `@`).",
                    LogLevel.WARNING,
                ),
                ephemeral=True,
            )

        member_names = ", ".join([member.display_name for member in members])

        category = interaction.guild.get_channel(CATEGORY_STUDY_GROUPS)
        overwrites = self.get_overwrites(members)

        view = StudyGroupInviteView(interaction, members, overwrites)
        await interaction.response.send_message(
            view=view,
            ephemeral=True,
        )

    async def get_members(
        self, interaction: Interaction, names: str
    ) -> list[Interaction.user]:
        """
        This method allows to get a list of members in the discord channel. It helps check if students
        to be invited to a study group are part of the discord channel.

        Args:
            interaction: Required by the API. Gives meta information about the interaction.
            names: String describing names to get.
        Returns:
            list of members
        """
        members: list[Interaction.user] = []
        ids = [
            int(name.strip("<@>"))
            for name in names.replace("><", "> <").split(" ")
        ]
        for id in ids:
            member = None
            try:
                member = interaction.guild.get_member(id)
            except:
                return
            members.append(member)
        return members

    def get_overwrites(self, members: list[Interaction.user]):
        """
        This method allows new members of a study group to access said group.
        Args:
            members: A list of new members
        Returns:
            dictionary containing new members and their access rights 
        """
        overwrites = {}
        for member in members:
            overwrites[member] = nextcord.PermissionOverwrite(
                view_channel=True
            )

        return overwrites


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(StudyGroupCmd(client))
