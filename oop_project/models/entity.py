from os import name
from uuid import UUID

from models.base import Base

class Entity(Base):
    def _init_(
            self,
            id: UUID,
            name: str,
            description: str,
    ):
        super().__init__(id=id)
        self.name = name
        self.description = description


    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)
