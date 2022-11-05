from discord.ext import commands
import requests

class Meme(commands.Cog):
    """Fetches a random meme from reddit."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx, *, sub=''):
        """Specify a subreddit to get it from there!"""
        sauce = requests.get(f"https://meme-api.herokuapp.com/gimme/{sub}").json()
        await ctx.send(sauce['url'])

async def setup(bot: commands.Bot):
    await bot.add_cog(Meme(bot))
