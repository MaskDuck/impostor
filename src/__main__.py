from os import getenv
from nextcord.ext import commands
from nextcord import Intents
import config


class Impostor(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="sus ", intents=Intents.all())
        self.load_extension("exts.suggestion")
        self.load_extension("exts.meta")

    async def on_ready(self):
        print("SUS")


bot = Impostor()
if config.debug == False:
    from dotenv import load_dotenv
    load_dotenv(override=True)

    if config.pr_testing == False:
        bot.run(getenv("TOKEN"))
        
else:
    bot.run(getenv("TOKEN"))
