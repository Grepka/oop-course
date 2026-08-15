from models.category import Category



if __name__ == "__main__":
    category = Category.create(name="Тестовая категория", description="Тестовое описание")
    print(category)