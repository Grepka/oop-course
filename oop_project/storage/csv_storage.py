from csv import DictReader, DictWriter
from pathlib import Path
from uuid import UUID

from storage.base import StorageProtocol
from mixins.serializable import Serializable
from models.base import Base


class CVSStorage[T: Serializable | Base](StorageProtocol):
    def __init__(self, filepath: Path, model_class: type[T]) -> None:
        self.filepath = filepath
        self.model_class = model_class
        self.data: dict[UUID, T] = {}

    def save(self) -> None:
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with self.filepath.open("w") as file:
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
        if not self.filepath.exists():
            return

        with self.filepath.open("r") as file:
            reader = DictReader(file)
            for row in reader:
                entity = self.model_class.from_dict(row)
                self.data[entity.id] = entity
