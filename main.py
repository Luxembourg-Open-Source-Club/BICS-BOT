#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import log_setup as log
from server_ids import *

# - Embeds
from embeds.welcome_embed import Welcome_embed
from embeds.help_embed import Help_embed

load_dotenv()
log.setup_nextcord_logging()

LOGGER = log.get_bot_logger()


def get_intents():
    # - Loading intents
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    return intents


bot_description = """**BICS-THE-BOT** is a bot made for the BICS Student Server.\n
                    It's purpose is to automate the server in someways such as let a user make a selection of the courses he/she attends, welcoming new members and much more.
                    This bot is currently under development and thus it is not up to its full potential. In order to find out what is currently available try the **/help** command."""
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
    await interaction.response.send_message(embed=Help_embed(), ephemeral=True)


@bot.slash_command(
    guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID], description="Introduce yourself"
)
async def intro(
    interaction: nextcord.Interaction,
    name: str = nextcord.SlashOption(description="Name", required=True),
    surname: str = nextcord.SlashOption(description="Surname", required=True),
    year: str = nextcord.SlashOption(
        description="The year you will be (in case of erasmus/global exchange choose **erasmus**)",
        choices=["year-1", "erasmus"],
    ),
):
    if interaction.channel_id == INTRO_CHANNEL_ID:
        user = interaction.user
        user_roles = user.roles

        if len(user_roles) > 1:
            # - Means the user already has at least one role
            await interaction.response.send_message(
                f"You have already introduced yourself! In case you have a role that you think should be changed feel free to ping an <@&{ADMIN_ROLE_ID}>",
                ephemeral=True,
            )
        else:
            # - Getting the roles
            year1_role = interaction.guild.get_role(YEAR1_ROLE_ID)
            erasmus_role = interaction.guild.get_role(ABROAD_ROLE_ID)

            # if year == "year-1":
            #     await user.add_roles(year1_role)
            # else:
            #     await user.add_roles(erasmus_role)

            # - Changing the nickname to Name + Surname initial
            await user.edit(nick=f"{name.capitalize()} {surname[0].upper()}")

            await interaction.response.send_message(
                f"Welcome on board {name} {surname}. Your role has been updated and you are all set 😉. In case of any question, or your name has not correctly been changed, feel free to ping an <@&{ADMIN_ROLE_ID}>",
                ephemeral=True,
            )
    else:
        # - Trying to type the command outside the right channel
        await interaction.response.send_message(
            f"Oops something went wrong! Make sure you are on <#{INTRO_CHANNEL_ID}> to send the **/intro** command",
            ephemeral=True,
        )


bot.run(os.getenv("BOT_TOKEN"))
# bot.run(os.getenv("BOT_TESTER_TOKEN"))
