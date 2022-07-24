from nextcord.ext import commands
from nextcord import Intents, Status, Activity, ActivityType


from dotenv import load_dotenv
from os import getenv

load_dotenv()
from helper.db import Database


class Impostor(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="sus ",
            intents=Intents.all(),
            activity=Activity(type=ActivityType.watching, name="over is-a.dev"),
            status=Status.dnd,
        )
        self.db: Database = Database(mongodb_url = getenv("MONGODB_URL"), bot=self)
        self.load_extension("exts.suggestion")
        self.load_extension("exts.meta")
        self.load_extension("exts.ping")
        self.load_extension("exts.utils")
        self.load_extension("exts.activity")
        self.load_extension("exts.bans")
        self.load_extension("exts.stars")

    async def on_ready(self):
        print("SUS")



bot = Impostor()

if getenv("PR_TESTING") in ["0", None]:
    bot.run(getenv("TOKEN"))
