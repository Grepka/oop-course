from pathlib import Path


from models.category import Category
from storage.cvs_storage import CVSStorage



if __name__ == "__main__":
    # category = Category.create(name="Тестовая категория", description="Тестовое описание")
    # new_category = Category.create(name="Новая категория", description="Новое описание")
    # print(category)
    # print(category.description)
    #
    # data = category.to_dict()
    # print(data)
    #
    # print(Category.from_dict(data))
    #
    current_path = Path(__file__).parent
    current_path = current_path / "category.csv"

    category_storage = CVSStorage(
        path = current_path,
        model_class = Category,
    )

    # category_storage.data[category.id] = category
    # category_storage.data[new_category.id] = new_category
    #
    # category_storage.save()

    category_storage.load()
    print(category_storage.data)




