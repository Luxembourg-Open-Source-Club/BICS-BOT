#!/usr/bin/env python3
import os
import argparse
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

from bics_bot.utils.file_manipulation import read_txt

# Loading the bot tokens from your .env folder.
load_dotenv()


def get_intents() -> nextcord.Intents:
    """
    Loading the intents of the bot. Intents are the capabilities of the bot.

    Args:
        None

    Returns:
        intents: The intent settings chosen.
    """
    # - Loading intents
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    return intents


def load_extensions(bot: commands.Bot):
    """
    Loading up the cogs from cogs/commands and cogs/events. Read about cogs
    from the Nextcord docs to understand what they are and how they work.

    Args:
        bot: the bot object

    Returns:
        None
    """
    for filename in os.listdir("./bics_bot/cogs/events"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"bics_bot.cogs.events.{filename[:-3]}")

    for filename in os.listdir("./bics_bot/cogs/commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"becs_bot.cogs.commands.{filename[:-3]}")


def main(args: vars):
    bot = commands.Bot(
        command_prefix="!",
        description=read_txt("./bics_bot/texts/bot_description.txt"),
        intents=get_intents(),
    )

    load_extensions(bot)

    if args["clone"]:
        bot.run(os.getenv("TOKEN_BOT_CLONE"))
    else:
        bot.run(os.getenv("TOKEN_BOT"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-c",
        "--clone",
        default=False,
        help="When passed, the bot clone token will be used",
        action=argparse.BooleanOptionalAction,
    )
    args = vars(ap.parse_args())
    main(args)
