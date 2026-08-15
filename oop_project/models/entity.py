from uuid import UUID

from models.base import Base

class Entity(Base):
    def __init__(
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
