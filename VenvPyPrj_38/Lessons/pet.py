# Задание 1.8.2
# Создайте класс Dog с помощью наследования класса Cat. Создайте метод get_pet() таким образом, чтобы он возвращал только имя и возраст.
# Далее сделайте вывод этой информации в консоль

from Lessons.cats import CatClass

class Dog(CatClass):
    def __init__(self, name=' - ', age=0):
        self.name = name
        self.age = age
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'
    # def get_name(self):
    #     return self.name
    # def get_age(self):
    #     return self.age
