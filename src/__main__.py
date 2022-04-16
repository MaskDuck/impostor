from tkinter import FALSE
from nextcord.ext import commands
from nextcord import Intents

debug = False

if debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)


class Impostor(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="sus ", intents=Intents.all())
        self.load_extension("exts.suggestion")
        self.load_extension("exts.meta")

    async def on_ready(self):
        print("SUS")


from os import getenv

bot = Impostor()
if debug == False:
    if getenv("PR_TESTING") == 0:
        bot.run(getenv("TOKEN"))
else:
    bot.run(getenv("TOKEN"))
