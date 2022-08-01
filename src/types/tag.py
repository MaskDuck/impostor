from datetime import datetime
from typing import TypedDict, Union

from nextcord.types.member import Member as DiscordMember
from nextcord.types.member import User as DiscordUser

__all__ = "Tag"


class Tag(TypedDict):
    owner: int
    id: int
    name: str
    description: str
    created_at: datetime.datetime
