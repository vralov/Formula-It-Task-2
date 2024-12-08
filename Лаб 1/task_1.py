import datetime
import doctest


class Student:
    def __init__(self, academic_debt: int, time_until_deadline: float):
        """
        Создание и подготовка к работе объекта "Студент"

        :param academic_debt: Количество академических долгов
        :param time_until_deadline: Время до дедлайна в днях

        Примеры:
        >>> student = Student(500, 3)  # инициализация экземпляра класса
        """
        if not isinstance(academic_debt, int):
            raise TypeError("Количество академических долгов должно быть типа int")
        if academic_debt < 0:
            raise ValueError("Количество академических долгов должно быть положительным числом")
        self.academic_debt = academic_debt

        if not isinstance(time_until_deadline, (int, float)):
            raise TypeError("Время до дедлайна должно быть int или float")
        if time_until_deadline < 0:
            raise ValueError(
                "Время до дедлайна не может быть отрицательным числом, это значит, что студента уже отчислили")
        self.time_until_deadline = time_until_deadline

    def good_student(self, name: str = "плохой студент") -> str:
        """
        Функция которая проверяет является ли студент хорошим

        :return: Является ли студент хорошим

        Примеры:
         >>> student = Student(0, 3)
         >>> student.good_student()
         'хороший студент'
        >>> student2 = Student(500, 3)
        >>> student2.good_student()
        'плохой студент'
        """
        if self.academic_debt == 0:
            name = f"хороший студент"
        return name

    def add_time(self, time: float) -> None:
        """
        Добавление студенту времени до дедлайна.

        :param time: время добавляемое к дедлайну

        :raise ValueError: Если время до дедлайна становится отрицательным, значит сдудента отчислили

        Примеры:
        >>> student = Student(500, 3)
        >>> student.add_time(200)

        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время до дедлайна должно быть int или float")
        if time + self.time_until_deadline < 0:
            raise ValueError("Вы отчислили студента")
        self.time_until_deadline = self.time_until_deadline + time


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создает экземпляр класса Book.

        :param title: Название книги (не может быть пустым).
        :param author: Автор книги (не может быть пустым).
        :param pages: Количество страниц (должно быть положительным числом).
        :raises ValueError: Если title, author пустые строки или pages не положительное число.

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1500)  # инициализация экземпляра класса
        """
        if not title:
            raise ValueError("Название книги не может быть пустым.")
        if not author:
            raise ValueError("Автор книги не может быть пустым.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        :return: Строка с информацией о книге.
        >>> book = Book("Война и мир", "Лев Толстой", 1500)
        >>> book.get_info()
        'Название: Война и мир, Автор: Лев Толстой, Страниц: 1500'
        """
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def pages_read(self, pages: float) -> int:
        """
        Возвращает сколько страниц осталось прочитать.

        >>> book = Book("Война и мир", "Лев Толстой", 1500)
        >>> book.pages_read(300)
        1200
        """
        if not isinstance(pages, (int, float)):
            raise TypeError("Страницы должны быть int или float")
        if self.pages - pages < 0:
            raise ValueError("Вы обманщик, там нет столько страниц")
        return self.pages - pages


class SocialNetwork:
    def __init__(self, name: str, creation_date: datetime.date = None):
        """
        Создает экземпляр класса SocialNetwork.

        :param name: Название социальной сети (не может быть пустым).
        :param creation_date: Дата создания социальной сети (по умолчанию - текущая дата).
        :raises ValueError: если name пустая строка
        """
        if not name:
            raise ValueError("Название социальной сети не может быть пустым.")
        self.name: str = name
        self.users: int = 0
        self.creation_date: datetime.date = creation_date or datetime.date.today()  # Используем текущую дату, если не указана

    def add_user(self, num_users: int) -> int:
        """
        Добавляет пользователей в социальную сеть.

        :param num_users: Количество добавляемых пользователей (должно быть положительным числом).
        :return: Общее количество пользователей после добавления.
        :raises ValueError: если num_users не положительное число
        >>> network = SocialNetwork("MyNet")
        >>> network.add_user(10)
        10
        """
        if num_users <= 0:
            raise ValueError("Количество пользователей должно быть положительным числом")
        self.users += num_users
        return self.users

    def get_name(self) -> str:
        """
        Возвращает имя социальной сети.
        >>> network = SocialNetwork("VK")
        >>> network.get_name()
        'VK'

        """
        return self.name

    def get_creation_date(self) -> datetime.date:
        """Возвращает дату создания социальной сети.
        >>> network = SocialNetwork("FB", datetime.date(2004, 2, 4))
        >>> network.get_creation_date()
        datetime.date(2004, 2, 4)
        """
        return self.creation_date


if __name__ == "__main__":
    doctest.testmod()
