from os import getenv
from nextcord.ext import commands
debug = True

if debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)


class BaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return (
            ctx.channel.id == int(getenv("SUGGESTION_CHANNEL"))
            or int(getenv("ROLE1")) in [role.id for role in ctx.author.roles]
            or int(getenv("ROLE2")) in [role.id for role in ctx.author.roles]
            or self.bot.is_owner(ctx.author)
        )

    def cog_application_command_check(self, interaction):
        return (
            interaction.channel.id == int(getenv("SUGGESTION_CHANNEL"))
            or int(getenv("ROLE1")) in [role.id for role in interaction.user.roles]
            or int(getenv("ROLE2")) in [role.id for role in interaction.user.roles]
            or self.bot.is_owner(interaction.user)
        )
