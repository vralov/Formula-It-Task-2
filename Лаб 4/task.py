from math import pi


class GeometricShape:
    """
    Базовый класс для геометрических фигур.
    """

    def __init__(self, name: str):
        """
        Конструктор базового класса.
        Args:
            name: Название геометрической фигуры.
        """
        self._name = name  # Инкапсуляция: _name защищен от прямого доступа извне класса

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Геометрическая фигура: {self._name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчиков.
        """
        return f"{self.__class__.__name__}(name='{self._name}')"

    def area(self) -> float:
        """
        Вычисляет площадь фигуры (базовая реализация, может быть переопределена в подклассах).
        """
        raise NotImplementedError("Метод area должен быть реализован в подклассах.")

    def describe(self) -> str:
        """
        Общий метод для описания фигуры.
        """
        return f"Это геометрическая фигура с именем: {self._name}."


class Circle(GeometricShape):
    """
    Класс для круга.
    """

    def __init__(self, name: str, radius: float):
        """
        Конструктор класса Circle.
        Args:
            name: Название круга.
            radius: Радиус круга.
        """
        super().__init__(name)
        self._radius = radius  # Инкапсуляция: _radius защищен от прямого доступа извне класса

    def __str__(self) -> str:
        """
        Переопределенный метод str для вывода информации о круге.
        """
        return f"Круг '{self._name}' с радиусом {self._radius}"

    def __repr__(self) -> str:
        """
        Переопределенный метод repr для вывода информации о круге для разработчиков.
        """
        return f"{self.__class__.__name__}(name='{self._name}', radius={self._radius})"

    def area(self) -> float:
        """
        Вычисляет площадь круга. Переопределенный метод area из базового класса.
        """
        return pi * self._radius ** 2

    def perimeter(self) -> float:
        """
        Вычисляет периметр (длину окружности) круга.
        """
        return 2 * pi * self._radius


# Пример использования
circle1 = Circle("Круг1", 5)
print(circle1)
print(repr(circle1))
print(f"Площадь: {circle1.area()}")
print(f"Периметр: {circle1.perimeter()}")
print(circle1.describe())

try:
    shape = GeometricShape("Фигура")
    shape.area()  # Вызовет NotImplementedError
except NotImplementedError as e:
    print(e)

shape = GeometricShape("Фигура")
print(shape.describe())
