# Необходимо рассчитать площадь геометрической фигуры на основе полиморфизма:
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2
# возведение в степень **2 (в квадрат)

# Задание 1.9.1
# Выполните задание, взяв за основу код из примера выше.
# Добавьте ещё один класс — круг (class Circle), конструктор которого содержит параметр радиус. Добавьте метод для расчёта площади круга (вспомните формулу).
# Далее сделайте вывод информации о площади в консоль
class Circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return self.pi * self.r**2