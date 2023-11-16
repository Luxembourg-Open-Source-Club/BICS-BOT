import nextcord

from nextcord.interactions import Interaction
from bics_bot.embeds.logger_embed import LoggerEmbed
from bics_bot.utils.calendar import Calendar
from bics_bot.utils.channels_utils import (
    retrieve_courses_text_channels_names,
)


class EventsDropdown(nextcord.ui.Select):
    """
    This class creates dropdown of events for use when trying to delete events in calendar.

    Attributes:
        user: The user that needs the events dropdown
        guild: The channels needed to check the courses in which user is enrolled
        calendar: The calendar to be used
    """
    def __init__(self, user, guild, calendar: Calendar):
        self.option_to_row = {}
        self._options = self._get_options(user, guild, calendar)

    def build(self):
        super().__init__(
            placeholder="Choose events to be deleted",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, user, guild, calendar):
        """
        This method allows to get the options of events to delete in the dropdown for user

        Args:
            user: The user that needs the dropdown
            guild: The channels in which to check for the user
            calendar: Calendar used
        Returns:
            list of options to show in dropdown
        """
        options = []
        enrolled_courses = self.get_courses_enrolled(user, guild)
        for entry in calendar.retrieve_entries():
            if entry.course in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=f"{entry.course} {entry.type} on {entry.deadline_date} at {entry.deadline_time}"
                    )
                )
                self.option_to_row[
                    str(
                        nextcord.SelectOption(
                            label=f"{entry.course} {entry.type} on {entry.deadline_date} at {entry.deadline_time}"
                        )
                    )
                ] = entry
        return options

    def get_courses_enrolled(
        self, user: Interaction.user, guild: Interaction.guild
    ) -> dict[str, bool]:
        """Retrieves the courses a student is enrolled to.

        Technically, it returns the courses that the student can view it by
        any means necessary (member level permission, role level permission,
        admin rights).

        Args:
            user: the user who is doing the </enroll> or <unenroll> request.
            guild: the server object, containing information on text channels
              necessary for this opeation

        Returns:
            dictionary where the keys are the courses the student can see
        """
        enrolled: dict[str, bool] = {}
        channels = guild.text_channels
        courses_channels_names = retrieve_courses_text_channels_names(guild)

        for channel in channels:
            if (
                channel.name in courses_channels_names
                and user in channel.members
            ):
                enrolled[channel.topic] = True
        return enrolled


class CalendarView(nextcord.ui.View):
    """
    This class allows user to confirm elements selected in dropdown

    Attributes:
        user: The user that needs the events dropdown
        guild: The channels needed to check the courses in which user is enrolled
        calendar: The calendar to be used
    """
    def __init__(self, user, guild, calendar: Calendar):
        super().__init__(timeout=5000)
        self.events = EventsDropdown(user, guild, calendar)
        self.calendar = calendar
        if len(self.events._options) > 0:
            self.events.build()
            self.add_item(self.events)

    @nextcord.ui.button(
        label="Confirm", style=nextcord.ButtonStyle.green, row=3
    )
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows the user to confirm options

        Args:
            button: the button to click
            interaction: Interaction needed for the click of the button
        """
        for entry in self.events.values:
            if (
                self.events.option_to_row[entry]
                in self.calendar.retrieve_entries()
            ):
                self.calendar.remove_entry(self.events.option_to_row[entry])

        self.calendar.export_calendar()
        await self.calendar.update_caledar_text_channel(interaction)

        msg = ""
        for entry in self.events.values:
            entry = self.events.option_to_row[entry]
            msg += "The following events are deleted:\n\n"
            msg += f"{entry}\n"

        await interaction.response.send_message(
            embed=LoggerEmbed(msg),
            ephemeral=True,
        )

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red, row=3)
    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red, row=3)
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows for user to cancel options

        Args:
            button: the cancel button
            interaction: Interaction needed for cancel button
        """
        await interaction.response.send_message(
            "Canceled operation. No changes made.", ephemeral=True
        )
        self.stop()
