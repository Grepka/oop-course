from storage.category_storage import category_storage
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
    category = category_storage.get_by_name("Список покупок")
    note = Note.create(
        name="Вода",
        description="Купить вечером воды домой",
        category=category,
        text="Шишкин лес 2 литра, всегда забываю купить, это просто текс, что бы наполнить тестирование"
    )
    print(note)
    print([note])

if __name__ == "__main__":
    main()












