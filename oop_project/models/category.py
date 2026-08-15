from uuid import uuid4
from typing import Self


from models.entity import Entity


class Category(Entity):

    @classmethod
    def create(cls, name:str, description:str) -> Self:
        return cls(
            id=uuid4(),
            name=name,
            description=description,
        )