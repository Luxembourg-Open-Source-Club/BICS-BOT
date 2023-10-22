import nextcord
from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed

from datetime import datetime


class BirthdayCmd(commands.Cog):
    """This class represents the command </birthday>

    The </bithday> command allows users to enter their birth day so
    the bot can remind people on the server of that user's birthday

    Attributes:
        client: Required by the API, not directly utilized.
    """
    user = interaction.user
    user_roles = user.roles

    def __init__(self, client):
        self.client = client

    def is_valid_birthday(birthday):
        try:
            # Try to parse the provided string as a date in the expected format (DD.MM.YYYY).
            datetime.strptime(birthday, '%d.%m.%Y')
            return True
        except ValueError:
            # The date format is incorrect or invalid.
            return False

    @application_command.slash_command(
        description="Receive birthday greetings from fellow BiCS students",
    )
    async def birthday_add(
        self,
        interaction: Interaction,
        birthdate: str = nextcord.SlashOption(
            description="Your birthday in the format DD.MM.YYYY (e.g., 05.06.1990).",
            required=True,
        ),
    ) -> None:
        if not self.is_valid_birthday(birthdate):
            await interaction.response.send_message(
                embed=LoggerEmbed(
                    "Invalid Format",
                    "Please provide your birthday in the format DD.MM.YYYY (e.g., 05.06.1990).",
                ),
                ephemeral=True,
            )
            return


        
        """
        Mr Ivo Big cock 23 we will need to do the add_birthday_to_profile function
        """
        #add_birthday_to_profile(user, birthdate)

        

        await interaction.response.send_message(
            embed=LoggerEmbed(
                "Birthday Added",
                f"Your birthday ({birthdate}) has been added to your profile.",
            ),
            ephemeral=True,
        )



    
    if len(user_roles) == 1:
        # The user has no roles. So he must first use the /intro command
        msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
        await interaction.response.send_message(
            embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
            ephemeral=True,
    )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(BirthdayCmd(client))