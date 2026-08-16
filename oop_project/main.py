from models.category import Category
from storage.csv_storage import CVSStorage
from settings import CATEGORY_STORAGE_PATH


def print_data(dict_data):
    for key, value in dict_data.items():
        print(key, value)


def main():
    category = Category.create(name="Добавдяемая категория", description="Добавляемое описание")
    new_category = Category.create(name="Добавляемое добавляемой категория", description="Добавляемое добавляемой описание")

    print(category, "|", category.description)
    print(new_category, "|", new_category.description)

    category_storage = CVSStorage(
        path=CATEGORY_STORAGE_PATH,
        model_class=Category,
    )

    category_storage.load()
    print_data(category_storage.data)
    print()
    category_storage.data[category.id] = category
    category_storage.data[new_category.id] = new_category
    print()
    print_data(category_storage.data)
    category_storage.save()
    print()
    print_data(category_storage.data)



if __name__ == "__main__":
    main()












