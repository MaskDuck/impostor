from __future__ import annotations

from typing import TYPE_CHECKING

import aiohttp
from aiohttp import ClientSession
from nextcord.ext import tasks

from models.basecog import BaseCog

if TYPE_CHECKING:
    from typing import Final, TypeVar

    from nextcord import VoiceChannel
    from nextcord.ext.commands import Bot

    BotLike = TypeVar("BotLike", bound=Bot)

STAR_CHANNEL_ID: Final[int] = 973922065923059762  # type: ignore


class Stars(BaseCog):
    def __init__(self, bot: BotLike) -> None:
        self._bot: BotLike = bot
        self.update_stars.start()

    @tasks.loop(minutes=2)
    async def update_stars(self):
        STAR_CHANNEL: VoiceChannel = self._bot.get_channel(STAR_CHANNEL_ID)
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
