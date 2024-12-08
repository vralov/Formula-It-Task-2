from task_1 import Student, Book, SocialNetwork# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.

    try:
        student = Student(100, 5)
        student.add_time("5 минут")
     # TODO: вызвать метод с некорректными аргументами
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        book = Book("Война и мир", "Лев Толстой", 1500)
        book.pages_read("2500")
     # TODO: вызвать метод с некорректными аргументами
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        network = SocialNetwork("MyNet")
        network.add_user(-10)
     # TODO: вызвать метод с некорректными аргументами
    except ValueError:
        print('Ошибка: неправильные данные')
