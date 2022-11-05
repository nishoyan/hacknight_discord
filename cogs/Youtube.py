from discord.ext import commands
from youtubesearchpython.__future__ import VideosSearch

class Youtube(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def search(self, ctx: commands.Context, *, query: str = "never going to give you up"):
        search = VideosSearch(query, limit=1)
        result = await search.next()
        link = result['result'][0]['link']
        await ctx.send(link)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Youtube(bot))
