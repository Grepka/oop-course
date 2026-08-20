from pathlib import Path


from storage.csv_storage import CVSStorage
from models import Category
from settings import CATEGORY_STORAGE_PATH


class CategoryStorage(CVSStorage):
    """
    Хранение категорий.
    """
    def __init__(
            self,
            filepath: Path,
            model_class= Category,
    ):
        super().__init__(filepath, model_class)

    def create(self, name: str, description: str) -> Category:
        category = self.model_class.create(name, description)
        self.data[category.id] = category
        self.save()
        return category

    def get_by_name(self, name: str) -> Category | None:
        for category in self.all():
            if category.name == name:
                return category
        return None


category_storage = CategoryStorage(CATEGORY_STORAGE_PATH)
category_storage.load()
