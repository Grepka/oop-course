from uuid import UUID, uuid4
from typing import Self, Any

from mixins.serializable import Serializable
from models.entity import Entity
from models.category import Category


class Note(Entity, Serializable):
    serializable_fields = (
        "id",
        "name",
        "description",
        "text",
        "category"
    )

    def __init__(
            self,
            id: UUID,
            name: str,
            description: str,
            text: str,
            category: Category
    ):
        Entity.__init__(self, id, name, description)
        self._category = category
        self.text = ""
        self._text = text


    @property
    def category(self) -> Category:
        return self._category

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        if text is None:
            raise ValueError("Text cannot be empty")
        if len(text) > 500:
            text = text[:500]
        self._text = str(text)

    @classmethod
    def deserialize_text(cls, value: Any) -> str:
        if value is None:
            return ""
        return str(value)

    @classmethod
    def deserialize_category(cls, value: Any) -> str:
        from storage.category_storage import category_storage
        return category_storage.data[UUID(value)]

    def serialize_category(self):
        return self.category.id

    @classmethod
    def create(
            cls,
            name: str,
            description: str,
            text: str,
            category: Category
    ) -> Self:
        return cls(
            id=uuid4(),
            name=name,
            description=description,
            text=text,
            category=category
        )

    def __str__(self) -> str:
        return f"name={self.name!r}, text={self.text}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, text={self.text!r})"
