from models.basecog import BaseCog
from nextcord import slash_command, SlashOption, Embed
from dns import resolver
class Utils(BaseCog):
    def __init__(self, bot):
        self.bot = bot
    
    def cog_application_command_check(self, interaction):
        return (
            interaction.channel.id == 960446827579199488
            or interaction.channel.id == 946105325914828840
            or 830875873027817484 in [role.id for role in interaction.user.roles]
            or 959723229805707285 in [role.id for role in interaction.user.roles]
            or self.bot.is_owner(interaction.user)
        )
    
    @slash_command(name='getdns')
    async def _getdns(self, interaction):
        pass

    @_getdns.subcommand(description='get cname of a domain')
    async def cname(self, interaction, domain: str = SlashOption(name='domain', description='The domain you want to fetch description of')):
        try:
            cnames = "\n".join([str(cname) for cname in resolver.resolve(domain, "CNAME")])
        except resolver.NoAnswer:
            cnames = "No CNAME found"
        
        embed = Embed(
            title = f'CNAME for {domain}',
            description = f"```\n{cnames}\n```"
        )
        await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(Utils(bot))
        
    
    