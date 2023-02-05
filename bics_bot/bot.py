#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import log_setup as log
from server_ids import *

load_dotenv()

def get_intents():
    # - Loading intents
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    return intents

def load_extensions():
    for filename in os.listdir("./cogs/events"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"cogs.events.{filename[:-3]}")

    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"cogs.commands.{filename[:-3]}")

    # for filename in os.listdir("./cogs/dropdowns"):
    #     if filename.endswith(".py") and filename != "__init__.py":
    #         bot.load_extension(f"cogs.dropdowns.{filename[:-3]}")


bot_description = """**BICS-THE-BOT** is a bot made for the BICS Student Server.\n
                    It's purpose is to automate the server in someways such as let a user make a selection of the courses he/she attends, welcoming new members and much more.
                    This bot is currently under development and thus it is not up to its full potential. In order to find out what is currently available try the **/help** command."""
bot = commands.Bot(
    command_prefix="!", description=bot_description, intents=get_intents()
)

load_extensions()

bot.run(os.getenv("BOT_TOKEN"))
