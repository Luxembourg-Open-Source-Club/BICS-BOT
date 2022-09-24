#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import log_setup as log
from server_ids import *

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


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs/"):
    print(filename)
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


# bot.run(os.getenv("BOT_TOKEN"))
bot.run(os.getenv("BOT_TESTER_TOKEN"))
