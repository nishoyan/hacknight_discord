from discord.ext import commands
import discord
import os

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot started")

bot.run(token=os.environ['TOKEN'])
