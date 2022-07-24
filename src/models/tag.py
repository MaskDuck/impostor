from __future__ import annotations
from typing import TYPE_CHECKING

import typing_extensions



if TYPE_CHECKING:
    from typing_extensions import Self
    from ..types import Tag as TagData
    from nextcord.state import ConnectionState
    from nextcord.user import User as NextcordUser
    from nextcord.ext.commands import Bot
    from typing import TypeVar

    BotLike = TypeVar("BotLike", bound=Bot)

__all__ = "Tag"


class Tag:
    def __init__(
        self: Self, data: TagData, state: ConnectionState, bot: BotLike
    ) -> None:
        self._state: ConnectionState = state
        self._owner_id: int = data["owner"]
        self._data: TagData = data
        self.name = data["name"]
        self.description = data["description"]
        self.id = data["id"]
        self.created_at = data["created_at"]
        self._bot: BotLike = Bot

    @property
    def owner(self: Self) -> NextcordUser:
        return self._state.get_user(id=self._owner_id)

    def __eq__(self: Self, other: "Tag") -> bool:
        return other.id == self.id

    def delete(self: Self) -> "Tag":
        self._bot.db.delete_tag(self.id)
        return self
