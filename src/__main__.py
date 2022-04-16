from nextcord.ext import commands
from nextcord import Intents
import config

from dotenv import load_dotenv

load_dotenv()


class Impostor(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="sus ", intents=Intents.all())
        self.load_extension("exts.suggestion")
        self.load_extension("exts.meta")
        self.load_extension("exts.ping")


    async def on_ready(self):
        print("SUS")

bot = Impostor()
if config.debug == False:
    if config.pr_testing == False:
        bot.run(config.token)
else:
    bot.run(config.token)
