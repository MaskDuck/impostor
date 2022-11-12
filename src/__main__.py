from logging import StreamHandler, getLogger
from os import getenv

from dotenv import load_dotenv
from nextcord import Activity, ActivityType, Intents, Status
from nextcord.ext import commands
from tomlkit import parse

load_dotenv()
from helper.db import Database

_log = getLogger("nextcord")
_log.setLevel(1)
_log.addHandler(StreamHandler())


intents = Intents.all()
intents.presences = False
class Impostor(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="sus ",
            intents=intents,
            activity=Activity(type=ActivityType.watching, name="over is-a.dev"),
            status=Status.dnd,
        )
        # self.db: Database = Database(mongodb_url = getenv("MONGODB_URL"), bot=self)
        self.load_extension("exts.suggestion")
        self.load_extension("exts.meta")
        self.load_extension("exts.ping")
        self.load_extension("exts.utils")
        # self.load_extension("exts.activity")
        self.load_extension("exts.bans")
        self.load_extension("exts.stars")
        self.load_extension("exts.roles")
        self.load_extension("onami")

    with open("config.toml", "r") as config_file:
        config = parse(config_file.read())

    async def on_ready(self):
        print("SUS")


bot = Impostor()

if getenv("PR_TESTING") in ["0", None]:
    bot.run(getenv("TOKEN"))
