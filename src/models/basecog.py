from nextcord.ext import commands


class BaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == 960446827579199488
            or 830875873027817484 in [role.id for role in ctx.author.roles]
            or 959723229805707285 in [role.id for role in ctx.author.roles]
            or self.bot.is_owner(ctx.author)
        )

    def cog_application_command_check(self, interaction):
        return (
            interaction.channel.id == 960446827579199488
            or 830875873027817484 in [role.id for role in interaction.user.roles]
            or 959723229805707285 in [role.id for role in interaction.user.roles]
            or self.bot.is_owner(interaction.user)
        )



