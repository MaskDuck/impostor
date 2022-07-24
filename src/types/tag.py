from typing import TypedDict, Union
from nextcord.types.member import Member as DiscordMember, User as DiscordUser
from datetime import datetime

__all__ = "Tag"


class Tag(TypedDict):
    owner: int
    id: int
    name: str
    description: str
    created_at: datetime.datetime
