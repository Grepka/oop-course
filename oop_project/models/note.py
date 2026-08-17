from uuid import UUID, uuid4
from typing import Self

from models.entity import Entity
from models.category import Category


class Note(Entity):
    def __init__(
            self,
            id: UUID,
            name: str,
            description: str,
            text: str,
            category: Category
    ):
        super().__init__(id, name, description)
        self._category = category
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
