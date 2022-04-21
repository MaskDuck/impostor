from nextcord.ext import commands
from nextcord import Interaction
import config


class BaseCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == config.suggestion_channel
            or config.maintainer_role in [role.id for role in ctx.author.roles]
            or config.admin_role in [role.id for role in ctx.author.roles]
            or self.bot.is_owner(ctx.author)
        )

    def cog_application_command_check(self, interaction: Interaction):
        return (
            interaction.channel.id == config.suggestion_channel
            or config.maintainer_role in [role.id for role in interaction.user.roles]
            or config.admin_role in [role.id for role in interaction.user.roles]
            or self.bot.is_owner(interaction.user)
        )
