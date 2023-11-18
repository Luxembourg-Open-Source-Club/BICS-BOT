import nextcord

from nextcord.interactions import Interaction
from bics_bot.embeds.logger_embed import LoggerEmbed
from bics_bot.config.server_ids import CATEGORY_STUDY_GROUPS


class StudyGroupDropdown(nextcord.ui.Select):
    """
    This class allows a dropdown of groups if a user wants to delete a study group.

    Attributes:
        interaction: Required by API. Gives meta information about the interaction.
    """
    def __init__(self, interaction: Interaction):
        self._options = self._get_options(interaction)

    def build(self):
        super().__init__(
            placeholder="Choose the study group",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, interaction: Interaction):
        """
        This method allows to get related channels of a group that wants to be deleted

        Args:
            interaction: Required by API, gives meta information about interaction
        """
        options = []
        category = interaction.guild.get_channel(CATEGORY_STUDY_GROUPS)
        for channel in category.text_channels:
            if interaction.user in channel.members:
                options.append(nextcord.SelectOption(label=channel.name))
        return options


class StudyGroupInviteView(nextcord.ui.View):
    """
    This class allows to show dropdown of members a user might invite to study group.

    Attributes:
        interaction: Gives meta information about interaction
        members: members in the discord server
        overwrites: members permissions
    """
    def __init__(self, interaction: Interaction, members, overwrites):
        super().__init__(timeout=5000)
        self.groups = StudyGroupDropdown(interaction)
        self.members = members
        self.overwrites = overwrites
        if len(self.groups._options) > 0:
            self.groups.build()
            self.add_item(self.groups)

    @nextcord.ui.button(
        label="Confirm", style=nextcord.ButtonStyle.green, row=3
    )
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows to confirm selected members in the dropdown.

        Args:
            button: The confirm button
            interaction: The interaction with the button
        """
        for value in self.groups.values:
            for channel in interaction.guild.get_channel(
                CATEGORY_STUDY_GROUPS
            ).channels:
                if channel.name == value:
                    for member in self.members:
                        await channel.set_permissions(
                            target=member, overwrite=self.overwrites[member]
                        )

        member_names = ", ".join(
            [member.display_name for member in self.members]
        )
        await interaction.response.send_message(
            embed=LoggerEmbed(
                f"User(s) *{member_names}* have been given access.",
            ),
            ephemeral=True,
        )
        return

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red, row=3)
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows to cancel the selection of members in the dropdown.

        Args:
            button: The cancel button
            interaction: The interaction with the button
        """
        await interaction.response.send_message(
            "Canceled operation. No changes made.", ephemeral=True
        )
        self.stop()


class StudyGroupLeaveView(nextcord.ui.View):
    """
    This class allows to confirm or cancel the study group delete action.

    Attributes:
        interaction: Gives meta information about interaction
    """
    def __init__(self, interaction: Interaction):
        super().__init__(timeout=5000)
        self.groups = StudyGroupDropdown(interaction)
        if len(self.groups._options) > 0:
            self.groups.build()
            self.add_item(self.groups)

    @nextcord.ui.button(
        label="Confirm", style=nextcord.ButtonStyle.green, row=3
    )
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows to confirm deletion of selected study group in the dropdown.

        Args:
            button: The confirm button
            interaction: The interaction with the button
        """
        for value in self.groups.values:
            for channel in interaction.guild.get_channel(
                CATEGORY_STUDY_GROUPS
            ).channels:
                if channel.name == value:
                    await channel.set_permissions(
                        interaction.user, overwrite=None
                    )
        await interaction.response.send_message(
            embed=LoggerEmbed(
                f"You have left the study group. They will miss you :(",
            ),
            ephemeral=True,
        )
        return

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red, row=3)
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows to cancel the deletion of selected study group in the dropdown.

        Args:
            button: The confirm button
            interaction: The interaction with the button
        """
        await interaction.response.send_message(
            "Canceled operation. No changes made.", ephemeral=True
        )
        self.stop()
