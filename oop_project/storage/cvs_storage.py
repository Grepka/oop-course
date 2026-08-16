from csv import DictReader, DictWriter
from pathlib import Path
from uuid import UUID

from storage.base import StorageProtocol
from mixins.serializable import Serializable
from models.base import Base



class CVSStorage[T: Serializable | Base](StorageProtocol):
    def __init__(self, path: Path, model_class: type[T]) -> None:
        self.path = path
        self.model_class = model_class
        self.data: dict[UUID, T] = {}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w") as file:
            writer = DictWriter(
                f=file,
                fieldnames=self.model_class.serializable_fields,
            )
            writer.writeheader()
            writer.writerows(
                item.to_dict()
                for item in self.data.values()
            )

    def load(self) -> None:
        if not self.path.exists():
            return

        with self.path.open("r") as file:
            reader = DictReader(file)
            for row in reader:
                entity = self.model_class.from_dict(row)
                self.data[entity.id] = entity




