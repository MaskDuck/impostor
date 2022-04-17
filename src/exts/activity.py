from nextcord.ext import activities
from models.basecog import BaseCog
from nextcord import (
    slash_command,
    SlashOption,
    VoiceChannel,
    Interaction,
    ChannelType,
    Client,
)
from nextcord.abc import GuildChannel


class Activity(BaseCog):
    def __init__(self, bot: Client):
        self.bot = bot

    @slash_command(name="activity")
    async def _activity(self):
        pass

    @_activity.subcommand(name="betrayal", description="Play some Betrayal.io.")
    async def betrayal(
        self,
        interaction: Interaction,
        channel: GuildChannel = SlashOption(
            name="channel",
            description="the channel you want to play this game in",
            channel_types=[ChannelType.voice],
        ),
    ):
        invite = await channel.create_activity_invite(activities.Activity.betrayal)
        await interaction.send(invite)

    @_activity.subcommand(name="fishington", description="play some fishington.")
    async def fishington(
        self,
        interaction: Interaction,
        channel: GuildChannel = SlashOption(
            name="channel",
            description="the channel you want to play this game in",
            channel_types=[ChannelType.voice],
        ),
    ):
        invite = await channel.create_activity_invite(activities.Activity.fishington)
        await interaction.send(invite)

    @_activity.subcommand(name="youtube", description="watch some youtube.")
    async def youtube(
        self,
        interaction: Interaction,
        channel: GuildChannel = SlashOption(
            name="channel",
            description="the channel you want to play this game in",
            channel_types=[ChannelType.voice],
        ),
    ):
        invite = await channel.create_activity_invite(activities.Activity.youtube)
        await interaction.send(invite)

    @_activity.subcommand(description="play sketch heads!")
    async def sketch(
        self,
        interaction: Interaction,
        channel: GuildChannel = SlashOption(
            name="channel",
            description="the channel you want to play this game in",
            channel_types=[ChannelType.voice],
        ),
    ):
        invite = await channel.create_activity_invite(activities.Activity.sketch)
        await interaction.send(invite)

    @_activity.subcommand(name="word-snacks", description="play some word snacks")
    async def word_snacks(
        self,
        interaction: Interaction,
        channel: GuildChannel = SlashOption(
            name="channel",
            description="the channel you want to play this game in",
            channel_types=[ChannelType.voice],
        ),
    ):
        invite = await channel.create_activity_invite(activities.Activity.word_snacks)
        await interaction.send(invite)


def setup(bot):
    bot.add_cog(Activity(bot))
