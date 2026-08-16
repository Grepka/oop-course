from typing import Protocol


class StorageProtocol(Protocol):

    def save(self): ...
    def load(self): ...