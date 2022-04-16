from models.basecog import BaseCog
from nextcord import slash_command


class Ping(BaseCog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="pong")
    async def ping(self, interaction):
        await interaction.send("pong")


def setup(bot):
    bot.add_cog(Ping(bot))
