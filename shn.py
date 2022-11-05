from discord.ext import commands
import discord
import os

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    for f in os.listdir('cogs'):
        if f.endswith('.py'):
            cog = f.replace('.py', '')
            await bot.load_extension(f"cogs.{cog}")
            print(f"Loaded: {cog}")
    print("Bot started!")

bot.run(token=os.environ['TOKEN'])
