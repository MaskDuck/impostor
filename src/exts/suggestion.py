from models.basecog import BaseCog
from nextcord import SlashOption, Embed, Colour, slash_command
from nextcord.ext import application_checks
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nextcord import TextChannel

class Suggestion(BaseCog):
    def __init__(self, bot):
        self.bot = bot
    
    suggestion_mode = [
        "the server",
        "the service"
    ]

    @slash_command(
        name='suggestion'
    )
    async def _suggestion(self, interaction):
        pass
    
    @_suggestion.subcommand(
        name = "suggest",
        description = "We'd love to hear your suggestion!"
    )
    async def _suggest(self, interaction, _for: str = SlashOption(name='for', description='What do you want to suggest for?', required=True), suggestion: str = SlashOption(name='suggestion', description="Write your suggestion here.", required=True)):
        if _for == "the server":
            embed = Embed(
                title = "Server Suggestion",
                description = suggestion,
                colour = Colour.red()
            )
            embed.set_footer(text=f"By {str(interaction.user)} (ID {interaction.user.id})")
        
        if _for == "the service":
            embed = Embed(
                title = "Service Suggestion",
                description = suggestion,
                colour = Colour.red()
            )
            embed.set_footer(text=f"By {str(interaction.user)} (ID {interaction.user.id})")
        
        channel = self.bot.get_channel(830872946888146964)
        await channel.send(embed=embed)
        await interaction.response.send_message("You can now see your suggestion in <#831425425510760478>.", ephemeral=True)
    
    @_suggest.on_autocomplete("_for")
    async def _on_suggest_for_autocomplete(self, interaction, _for: str):
        if not _for:
            await interaction.response.send_autocomplete(self.suggestion_mode)
        
        nearest_mode = [
            mode for mode in self.suggestion_mode if _for.lower().startswith(mode.lower())
        ]
        await interaction.response.send_autocomplete(nearest_mode)
        
    
    @_suggestion.subcommand(
        name='deny',
        description='[MAINTAINER ONLY] disapprove the suggestion :('
    )
    @application_checks.has_permissions(administrator=True)
    async def _deny(self, interaction, messageId = SlashOption(name='message_id', description='Message to deny', required=True), why: str = SlashOption(name='why', description='Why did you deny this request?', required=True)):
        channel = self.bot.get_channel(830872946888146964)
        message = await channel.fetch_message(messageId)
        embed = message.embeds[0]
        embed.add_field(name=f'Denied by {str(interaction.user)}', value=why)
        await message.edit(embed=embed)
        await interaction.response.send_message("Done.")
    
    @_suggestion.subcommand(
        name='approve',
        description='[MAINTAINER ONLY] approve the suggestion :)'
    )
    @application_checks.has_permissions(administrator=True)
    async def _approve(self, interaction, messageId = SlashOption(name='message_id', description='Message to approve', required=True), why: str = SlashOption(name='why', description='Why did you deny this request?', required=False)):
        channel = self.bot.get_channel(830872946888146964)
        message = await channel.fetch_message(messageId)
        embed = message.embeds[0]
        embed.add_field(name=f'Approved by {str(interaction.user)}', value=why)
        await message.edit(embed=embed)
        await interaction.response.send_message("Done.")
def setup(bot):
    bot.add_cog(Suggestion(bot))