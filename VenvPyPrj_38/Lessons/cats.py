# Задание 1.8.1
# Создайте класс Cat в отдельном файле. Класс должен содержать конструктор с параметрами: имя, пол, возраст и методы get(), которые будут возвращать все параметры объекта.
# В другом файле создайте экземпляры класса. В качестве входных данных используйте данные о котах с сайта «Дом питомца». Не забудьте импортировать класс Cat в файл.
# Далее сделайте вывод информации о котах в консоль
class CatClass:
    def __init__(self, name=' - ', gender='M', age=1):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age
