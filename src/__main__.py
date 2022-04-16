from os import getenv
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
        self.load_extension("exts.activity")
        self.load_extension("exts.ping")

    async def on_ready(self):
        print("SUS")


bot = Impostor()
if not config.debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)

    if not config.pr_testing:
        bot.run(getenv("TOKEN"))

else:
    bot.run(getenv("TOKEN"))
