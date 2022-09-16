import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands, application_checks
import log_setup as log

# - Embeds
from embeds.welcome_embed import Welcome_embed
from embeds.help_embed import Help_embed

BICS_GUILD_ID = 753535223798562886
BICS_CLONE_GUILD_ID = 1014558774532509777

load_dotenv()
log.setup_nextcord_logging()

LOGGER = log.get_bot_logger()


def get_intents():
    # - Loading intents
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    return intents


bot_description = """This is the BOT built to work with the BICS student server.\n 
                     It's purpose is to automate the server in someways such as
                     let a user make a selection of the courses he/she attends, welcoming new members and much more.\n 
                     Currently the bot is under development and it is only serving as a wecoming user."""

bot = commands.Bot(
    command_prefix="!", description=bot_description, intents=get_intents()
)


# - Events


@bot.event
async def on_ready():
    LOGGER.info("The BOT is now active!")
    print("The BOT is now active!")


@bot.event
async def on_member_join(member: nextcord.Member):
    server_name = await bot.fetch_guild(member.guild.id)
    server_name = server_name.name
    LOGGER.info(f"{member} has joined the {server_name} server!")
    LOGGER.info(f"Sending welcoming message to {member}")

    await member.send(embed=Welcome_embed(member.display_name, server_name))


# - Commands
@bot.slash_command(
    guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID], description="Show bot commands"
)
async def help(interaction: nextcord.Interaction):
    await interaction.response.send_message(embed=Help_embed())


@bot.slash_command(
    guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID], description="Introduce yourself"
)
async def intro(
    interaction: nextcord.Interaction,
    name: str = nextcord.SlashOption(description="Name", required=True),
    surname: str = nextcord.SlashOption(description="Surname", required=True),
    year: str = nextcord.SlashOption(
        description="The year you will be/are in (in case of erasmus/global exchange choose **abroad**)",
        choices=["year-1", "year-2", "year-3", "abroad"],
    ),
):
    if interaction.channel_id == 1019964291597746237:
        await interaction.response.send_message(f"Hello {name} {surname}: year:{year}")
    else:
        await interaction.response.send_message(
            f"Oops something went wrong! Make sure you are on <#1019964291597746237> to send the **/intro** command"
        )


bot.run(os.getenv("BOT_TESTER_TOKEN"))
