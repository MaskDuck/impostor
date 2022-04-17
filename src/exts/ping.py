from models.basecog import BaseCog
from nextcord import Interaction, slash_command, Client


class Ping(BaseCog):
    def __init__(self, bot: Client):
        self.bot = bot

    @slash_command(name="pong")
    async def ping(self, interaction: Interaction):
        await interaction.send("pong")


def setup(bot):
    bot.add_cog(Ping(bot))
