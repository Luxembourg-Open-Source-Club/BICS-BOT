#!/usr/bin/env python3
import os
import argparse
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

from bics_bot.utils.file_manipulation import read_txt


load_dotenv()


def get_intents():
    # - Loading intents
    intents = nextcord.Intents.default()
    intents.members = True
    intents.message_content = True
    return intents


def load_extensions(bot: commands.Bot):
    for filename in os.listdir("./bics_bot/cogs/events"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"bics_bot.cogs.events.{filename[:-3]}")

    for filename in os.listdir("./bics_bot/cogs/commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f"bics_bot.cogs.commands.{filename[:-3]}")


def main(args: vars):
    bot = commands.Bot(
        command_prefix="!", description=read_txt("./bics_bot/texts/bot_description.txt"), intents=get_intents()
    )

    load_extensions(bot)

    if args["clone"]:
        bot.run(os.getenv("TOKEN_BOT_CLONE"))
    else:
        bot.run(os.getenv("TOKEN_BOT"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--clone", default=False,
                    help="When passed, the bot clone token will be used", action=argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())
    main(args)
