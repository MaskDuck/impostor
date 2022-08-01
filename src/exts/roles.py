from __future__ import annotations

from typing import TYPE_CHECKING

import typing_extensions

from models.basecog import BaseCog, commands

if TYPE_CHECKING:
    from typing import Final

    from nextcord import Member, Role
    from typing_extensions import Self

    from src.__main__ import Impostor

MEMBER_ROLE_ID: Final[int] = 1003646369975779439


class Roles(BaseCog):
    def __init__(self: Self) -> None:
        pass

    @commands.Cog.listener()
    async def on_member_join(self: Self, member: Member) -> None:
        role: Role = member.guild.get_role(MEMBER_ROLE_ID)
        await member.add_roles(role, reason="needs a license to enter this server")


def setup(bot: Impostor):
    bot.add_cog(Roles())
