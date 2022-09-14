import nextcord
from nextcord.ext import commands
import random

TOKEN = ""

description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", description=description, intents=intents)

bot.run(TOKEN)
