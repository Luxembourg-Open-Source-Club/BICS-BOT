from re import sub
import discord
from discord.ext import commands
from discord.ui import Select, View

TOKEN = "MTAxOTMzMDAwMTI5MzgxMTcyMg.GvqXBX.xgY_EZJhXyWhnbaevfu2MYD4Qsw4XuBXra6PEQ"

description = "BICS bot that manages the access to courses channels."

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------------")


@bot.command()
async def menu(ctx):
    menu = Select(
        options=[
            discord.SelectOption(label="Item 1", description="this is an item!"),
            discord.SelectOption(label="Item 2", description="this is an item!"),
            discord.SelectOption(label="Item 3", description="this is an item!"),
        ],
        max_values=3,
    )
    view = View()
    view.add_item(menu)
    await ctx.send("Choose an Item!", view=view)

    async def my_callb(interaction):
        await interaction.response.send_message(f"You chose the values:")
        print(interaction.data)

    menu.callback = my_callb


bot.run(TOKEN)
