from storage import category_storage, note_storage
from storage.csv_storage import CVSStorage
from models import Category, Note



def example_category_storage():
    category_storage.create(
        name="Список покупок",
        description="Заметки, что бы не возвращаться несколько раз в магазин"
    )

    print(category_storage.all())
    print()
    work = category_storage.get_by_name("Работа")
    print(work)


def main():
    category = category_storage.get_by_name("Домашние дела")
    # print(category)
    # note = note_storage.create(
    #     name="Мусор",
    #     description="Выкинуть мусор",
    #     category=category,
    #     text="++++++++++++"
    # )

    # for item in note_storage.data.values():
    #     print(item.category)

    print(note_storage.get_by_category(category))


if __name__ == "__main__":
    main()












