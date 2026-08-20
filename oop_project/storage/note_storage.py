from pathlib import Path


from storage.csv_storage import CVSStorage
from models import Note, Category
from settings import NOTE_STORAGE_PATH


class NoteStorage(CVSStorage):
    """
    Хранение заметок.
    """
    def __init__(
            self,
            filepath: Path,
            model_class= Note
    ):
        super().__init__(filepath, model_class)

    def create(
            self,
            name: str,
            description: str,
            text: str,
            category: Category
    ) -> Note:
        note = self.model_class.create(name, description, text, category)
        self.data[note.id] = note
        self.save()
        return note

    def get_by_category(self, category: Category) -> list[Note]:
        return [note for note in self.all() if note.category.id == category.id]


note_storage = NoteStorage(NOTE_STORAGE_PATH)
note_storage.load()