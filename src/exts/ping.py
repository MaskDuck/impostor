from models.basecog import BaseCog
from nextcord.ext import commands
from nextcord import Interaction, slash_command


class Ping(BaseCog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="pong")
    async def ping(self, interaction: Interaction):
        await interaction.send("pong")


def setup(bot):
    bot.add_cog(Ping(bot))
