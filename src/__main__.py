from nextcord.ext import commands
from nextcord import Intents



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


from os import getenv

bot = Impostor()

if getenv("PR_TESTING") == 1:
    bot.run(getenv("TOKEN"))
