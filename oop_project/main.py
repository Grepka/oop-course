from models.category import Category
from storage.category_storage import category_storage


def main():
    category_storage.create(
        name="Бытовая техники",
        description="Миксеры, блендеры, микроволновки"
    )

    print(category_storage.all())
    print()
    dishes = category_storage.get_by_name("Посуда")
    print(dishes)


if __name__ == "__main__":
    main()












