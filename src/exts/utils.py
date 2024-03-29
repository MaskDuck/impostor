from dns import resolver
from nextcord import Embed, Interaction, SlashOption, slash_command
from nextcord.ext import commands

from models.basecog import BaseCog


class Utils(BaseCog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def cog_application_command_check(self, interaction: Interaction):
        return (
            interaction.channel.id == 960446827579199488
            or interaction.channel.id == 946105325914828840
            or 830875873027817484 in [role.id for role in interaction.user.roles]
            or 959723229805707285 in [role.id for role in interaction.user.roles]
            or self.bot.is_owner(interaction.user)
        )

    @commands.command(hidden=True)
    @commands.is_owner()
    async def close(self, ctx):
        await self.bot.close()

    @slash_command(name="getdns")
    async def _getdns(self, interaction: Interaction):
        pass

    @_getdns.subcommand(description="get cname of a domain")
    async def cname(
        self,
        interaction: Interaction,
        domain: str = SlashOption(
            name="domain", description="The domain you want to fetch description of"
        ),
    ):
        try:
            cnames = "\n".join(
                [str(cname) for cname in resolver.resolve(domain, "CNAME")]
            )
        except resolver.NoAnswer:
            cnames = "No CNAME found"

        embed = Embed(title=f"CNAME for {domain}", description=f"```\n{cnames}\n```")
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Utils(bot))
