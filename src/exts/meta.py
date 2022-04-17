from models.basecog import BaseCog
from nextcord.ext import commands
from nextcord import slash_command, Interaction


class Meta(BaseCog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="meta")
    async def _meta(self, interaction: Interaction):
        pass

    @_meta.subcommand(description="show the bot source code")
    async def source(self, interaction: Interaction):
        await interaction.send("https://github.com/MaskDuck/impostor-helper-bot")


def setup(bot):
    bot.add_cog(Meta(bot))
