from discord.ext import commands
import discord
import os
from cogs import Ktu, Bookmark, Youtube, Meme, Confession

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot started!")
    await Ktu.setup(bot)
    await Bookmark.setup(bot)
    await Youtube.setup(bot)
    await Meme.setup(bot)
    await Confession.setup(bot)

bot.run(token=os.environ['TOKEN'])
