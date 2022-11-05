import requests
from bs4 import BeautifulSoup
from discord.ext import tasks, commands

class Ktu(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.results = []

        self.fetch_latest.start()

    # NOTE: I should have used announcement page to scrape directly 🥲
    @tasks.loop(seconds=30)
    async def fetch_latest(self):
        sauce = requests.get("https://ktu.edu.in/home.htm").text
        soup = BeautifulSoup(sauce, 'lxml')
        uls = soup.find('ul', {"class": "annuncement"})
        lis = uls.find_all('li')

        for li in lis:
            a = li.find('a').text
            if a not in self.results:
                if len(self.results) == 0: return

                channel = self.bot.get_channel(867377360529260562)
                await channel.send(a)
                return

async def setup(bot: commands.Bot):
    await bot.add_cog(Ktu(bot))

