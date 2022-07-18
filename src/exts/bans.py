from __future__ import annotations
from typing import TYPE_CHECKING

from nextcord.ui import View, button as button_decorator, Modal, TextInput
from models.basecog import BaseCog

from nextcord.ext import commands

from nextcord import (
    TextInputStyle,
    Object,
    utils,
    Embed,
    Color,
    NotFound,
    ButtonStyle,
    Permissions
)

if TYPE_CHECKING:
    from typing import Final
    from nextcord.ui import Button
    from nextcord import Interaction

MAIN_SERVER_ID: Final[int] = 830872854677422150
APPEAL_SERVER_ID: Final[int] = 958657336765984789
APPEAL_CHANNEL_ID: Final[int] = 998204336276508742
UNBANNED_CHANNEL_ID: Final[int] = 958657337290264648


class AppealModal(Modal):
    def __init__(self):
        super().__init__("Appeal your ban.")
        self.__reason = TextInput(
            style=TextInputStyle.short,
            label="Why was you banned?",
            placeholder="If you don't know, guess.",
            required=True,
            row=1,
        )
        self.__deserve = TextInput(
            required=True, label="Do you think you deserved this ban?", row=2
        )
        self.__why = TextInput(
            required=True,
            label="Why should we unban you?",
            row=3,
        )
        self.__improvement = TextInput(
            style=TextInputStyle.paragraph,
            label="What will you do to not being banned again?",
            placeholder='Say "My ban wasn\'t deserved" if you answered no in the 2nd question.',
        )
        self.add_item(self.__deserve)
        self.add_item(self.__reason)
        self.add_item(self.__why)
        self.add_item(self.__improvement)

    async def interaction_check(self, interaction: Interaction):
        is_a_dev_server = interaction.client.get_guild(MAIN_SERVER_ID)
        maintainer_role = utils.get(is_a_dev_server.roles, name="maintainers")
        try:
            await is_a_dev_server.fetch_ban(Object(interaction.user.id))
            return True
        except NotFound:
            if maintainer_role in interaction.user.roles:
                return True
            else:
                await interaction.send("You're not banned.", ephemeral=True)
                return False

    async def callback(self, interaction):
        is_a_dev_server = interaction.client.get_guild(MAIN_SERVER_ID)
        try:
            ban = await is_a_dev_server.fetch_ban(Object(interaction.user.id))
            ban_reason = ban.reason
        except NotFound:
            ban_reason = "Being a maintainer (Testing)"
        appeal_channel = interaction.client.get_channel(APPEAL_CHANNEL_ID)
        embed = (
            Embed(
                title="New Ban Appeal",
                description="Sent by {} (ID {})".format(
                    str(interaction.user), interaction.user.id
                ),
                color=Color.blurple(),
            )
            .add_field(name="Inputted reason", value=self.__reason.value)
            .add_field(name="Actual banned reason", value=ban_reason)
            .add_field(
                name="Deserved ban, according to the user", value=self.__deserve.value
            )
            .add_field(
                name="Improvement to not being banned again",
                value=self.__improvement.value,
            )
            .add_field(name="Why to unban", value=self.__why.value)
        )
        await appeal_channel.send(
            content=interaction.user.mention, embed=embed, view=BanState()
        )
        await interaction.send(
            "Appealed. You'll get your status of your appeal in <#{}>".format(
                UNBANNED_CHANNEL_ID
            ),
            ephemeral=True,
        )


class AppealView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button_decorator(label="Appeal", custom_id="banappeal")
    async def _appeal(self, button: Button, interaction: Interaction):
        await interaction.response.send_modal(AppealModal())


class BanState(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def _after_invoke(self, interaction, state):
        for child in self.children:
            child.disabled = True

        embed: Embed = interaction.message.embeds[0]

        embed.color = Color.green() if state else Color.red()

        await interaction.message.edit(view=None, embed=embed)

    async def interaction_check(self, interaction):
        return interaction.user.guild_permissions.administrator is True

    @button_decorator(
        label="Approve", style=ButtonStyle.success, custom_id="banappealapproe"
    )
    async def _approve(self, button: Button, interaction: Interaction):
        # print(interaction.message.content)
        # print(interaction.message.mentions)
        user_to_unban = interaction.message.mentions[0]
        await interaction.guild.unban(user_to_unban)
        unbanned_channel = interaction.client.get_channel(UNBANNED_CHANNEL_ID)
        await unbanned_channel.send(
            "{}, you have been unbanned.".format(user_to_unban.mention)
        )
        await user_to_unban.send(
            "{}, you have been unbanned.".format(user_to_unban.mention)
        )
        await interaction.send("done", ephemeral=True)
        await self._after_invoke(interaction)

    @button_decorator(
        label="Deny", style=ButtonStyle.danger, custom_id="banappealdenial"
    )
    async def _deny(self, button: Button, interaction: Interaction):
        user_to_unban = interaction.message.mentions[0]
        unbanned_channel = interaction.client.get_channel(UNBANNED_CHANNEL_ID)
        await unbanned_channel.send(
            "{}, your appeal has been denied.".format(user_to_unban.mention)
        )
        await user_to_unban.send(
            "{}, your appeal has been denied.".format(user_to_unban.mention)
        )
        await interaction.send("done", ephemeral=True)


class Ban(BaseCog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def send_ban_appeal(self, ctx):
        await ctx.send(view=AppealView())

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(AppealView())
        self.bot.add_view(BanState())



def setup(bot):
    bot.add_cog(Ban(bot))
