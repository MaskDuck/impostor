from nextcord.ext import commands
from models.basecog import BaseCog
from nextcord.ext.application_checks import has_role
from nextcord import slash_command, Member, SlashOption, Object, Interaction
from typing import no_type_check


class Help(BaseCog):
    @slash_command()
    @no_type_check
    async def helpban(
        self,
        interaction: Interaction,
        user: Member = SlashOption(description="Member to ban", required=True),
    ):
        """Ban someone from receiving help."""
        await user.add_roles(Object(self.bot.config["no_help_id"]))
        await interaction.send("Done!")

    @slash_command()
    @no_type_check
    async def helpunban(
        self,
        interaction: Interaction,
        user: Member = SlashOption(description="Member to ban", required=True),
    ):
        """Unban someone from receiving help."""
        await user.remove_roles(Object(self.bot.config["no_help_id"]))
        await interaction.send("Done!")


def setup(bot):
    bot.add_cog(Help(bot))
