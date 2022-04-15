from models.basecog import BaseCog
from nextcord import slash_command

class Meta(BaseCog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(name='meta'
    )
    async def _meta(self, interaction):
        pass

    @_meta.subcommand(description='show the bot source code')
    async def source(self, interaction):
        await interaction.send("https://github.com/MaskDuck/impostor-helper-bot")

def setup(bot):
    bot.add_cog(Meta(bot))