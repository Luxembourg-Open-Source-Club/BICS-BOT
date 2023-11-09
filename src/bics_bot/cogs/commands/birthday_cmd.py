import nextcord
from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.embeds.logger_embed import LoggerEmbed, LogLevel

from dateutil.parser import parse, ParserError
import json

def is_valid_birthday(birthday):
    """Validate the entered birthday format."""
    try:
        birthday_parsed = parse(birthday, dayfirst=True)
    except (ValueError, ParserError):
        return False

    return (
        birthday_parsed.strftime("%d.%m.%Y") == birthday
        and len(birthday_parsed.strftime("%Y")) == 4
    )

def store_birthday(file_name, birthday, user_id):
    """Store user's birthday in a JSON file."""
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    for _, ids in data.items():
        if user_id in ids:
            ids.remove(user_id)
            break

    if birthday in data:
        data[birthday].append(user_id)
    else:
        data[birthday] = [user_id]

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

class BirthdayCmd(commands.Cog):
    """This class represents the command </birthday>

    The </birthday> command allows users to enter their birthday so
    the bot can remind people on the server about that user's birthday.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        description="Receive birthday greetings from fellow BiCS students",
    )
    async def birthday(
        self,
        interaction: Interaction,
        birthday: str = nextcord.SlashOption(
            description="Your birthday in the format DD.MM.YYYY (e.g., 05.06.2000).",
            required=True
        ),
    ) -> None:
        
        user = interaction.user
        user_roles = user.roles

        if len(user_roles) == 1:
            # The user has no roles. So he must first use the /intro command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.WARNING),
                ephemeral=True,
        )
            return

        # Check if entered birthday is valid
        if not is_valid_birthday(birthday):
            msg = "You entered an invalid birthday. Please follow the format **DD.MM.YYYY**"
            await interaction.response.send_message(
                embed=LoggerEmbed(msg, LogLevel.WARNING),
                ephemeral=True,
            )
            return

        # Storing the user's birthday in JSON file
        file_name = "./bics_bot/config/birthdays.json"
        store_birthday(file_name, birthday, user.id)

        msg = f"Birthday Added\n Your birthday ({birthday}) has been added to your profile."
        await interaction.response.send_message(
            embed=LoggerEmbed(msg, LogLevel.INFO),
            ephemeral=True,
        )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(BirthdayCmd(client))