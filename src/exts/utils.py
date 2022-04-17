from models.basecog import BaseCog
from nextcord import slash_command, SlashOption, Embed
from dns import resolver
import config


class Utils(BaseCog):
    def __init__(self, bot):
        self.bot = bot

    def cog_application_command_check(self, interaction):
        return (
            interaction.channel.id == config.bot_channel
            or interaction.channel.id == config.help_channel
            or config.maintainer_role in [role.id for role in interaction.user.roles]
            or config.maintainer_role in [role.id for role in interaction.user.roles]
            or self.bot.is_owner(interaction.user)
        )

    @slash_command(name="getdns")
    async def _getdns(self, interaction):
        pass

    @_getdns.subcommand(description="get cname of a domain")
    async def cname(
        self,
        interaction,
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
