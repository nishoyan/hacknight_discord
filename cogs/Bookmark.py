from discord.ext import commands
import discord

# This is like the bookmarker bot from tinkerhub server but less advanced
class Bookmark(commands.Cog):
    """React with 📑 emoji to get the message as DM."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name in "📑🔖":
            msg = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            author = msg.author

            if msg.content != "":
                bookmark = discord.Embed(description=msg.content, colour=discord.Color.red())
                bookmark.set_author(name=author.name, icon_url=author.avatar)
                user = await self.bot.fetch_user(payload.user_id)
                await user.send(embed=bookmark)

async def setup(bot: commands.Bot):
    await bot.add_cog(Bookmark(bot))
