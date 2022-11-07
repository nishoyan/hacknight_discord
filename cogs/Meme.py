from discord.ext import commands
import requests

class Meme(commands.Cog):
    """Fetches a random meme from reddit."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx, sub='memes', *, count=1):
        """Specify a subreddit to get it from there!"""
        url = f"https://meme-api.herokuapp.com/gimme/{sub}/{count}"
        sauce = requests.get(url).json()
        for meme in sauce["memes"]:
            await ctx.send(meme['url'])

async def setup(bot: commands.Bot):
    await bot.add_cog(Meme(bot))
