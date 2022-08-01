from __future__ import annotations
from typing import TYPE_CHECKING

import aiohttp


from models.basecog import BaseCog
from aiohttp import ClientSession


from nextcord.ext import tasks

if TYPE_CHECKING:
    from typing import Final, TypeVar
    from nextcord.ext.commands import Bot
    from nextcord import VoiceChannel

    BotLike = TypeVar("BotLike", bound=Bot)


class Stars(BaseCog):
    def __init__(self, bot: BotLike) -> None:
        self._bot: BotLike = bot
        self.update_stars.start()

    @tasks.loop(minutes=2)
    async def update_stars(self):
        STAR_CHANNEL: VoiceChannel = self._bot.get_channel(
            self.config["star_counter_channel_id"]
        )
        async with aiohttp.ClientSession() as ses:
            async with ses.get(
                "https://api.github.com/repos/is-a-dev/register",
                headers={"Accept": "application/vnd.github+json"},
            ) as res:
                repo_data = await res.json()
        stars = repo_data["stargazers_count"]
        expected_name = "⭐ {} Stars".format(stars)
        if STAR_CHANNEL.name != expected_name:
            await STAR_CHANNEL.edit(name=expected_name)

    @update_stars.before_loop
    async def star_bf_loop(self):
        await self._bot.wait_until_ready()


def setup(bot: BotLike) -> None:
    bot.add_cog(Stars(bot))
