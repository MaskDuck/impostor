from __future__ import annotations

from datetime import datetime
from random import randint
from time import time_ns
from typing import TYPE_CHECKING, final

import typing_extensions
from pymongo import MongoClient

from models.tag import Tag

if TYPE_CHECKING:
    from typing import TypeVar

    from nextcord.ext.commands import Bot
    from pymongo.collection import Collection
    from typing_extensions import Self

    BotLike = TypeVar("BotLike", bound=Bot)


@final
class Database:
    def __init__(self: Self, mongodb_url: str, bot: BotLike):
        self._client: MongoClient = MongoClient(mongodb_url)
        self._tag_client: Collection = self._client["is-a-dev"].tags
        self._bot: BotLike = bot

    def tag_owned_by(self: Self, owner_id: int):
        return [
            Tag(data=tag, state=self._bot._state, bot=self._bot)
            for tag in self._tag_client.find({"owner": owner_id})
        ]

    @property
    def all_tags(self):
        return [
            Tag(data=tag, state=self._bot._state, bot=self._bot)
            for tag in self._tag_client.find()
        ]

    def get_tag_by_name(self: Self, tag_name: str):
        return Tag(
            data=self._tag_client.find({"name": tag_name}),
            state=self._bot._state,
            bot=self._bot,
        )

    def create_tag(self: Self, **kwargs):
        kwargs["id"] = time_ns() + randint(1, 10)
        kwargs["created_at"] = datetime.utcnow()
        return self._tag_client.insert_one(kwargs)

    def delete_tag(self: Self, tag_id: int):
        return self._tag_client.delete_one({"id": tag_id})
