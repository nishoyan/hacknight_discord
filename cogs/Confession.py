from discord.ext import commands
import discord

class Confession(commands.Cog):
    """Send message partially anonymous to a specified user."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def confess(self, ctx: commands.Context, to: discord.Member, *, message: str=''):
        await ctx.message.delete()
        await to.send(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(Confession(bot))
