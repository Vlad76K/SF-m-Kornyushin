# pi=3.14159
# print(pi**2/2)
# print(round(pi**2/2))

# pi = 31.4159265
# print ("%.4e" % (pi))

# s = "AsssDD"
# print(s.isdigit()) # строка состоит из цифр?
# print(s.isalpha()) # строка состоит из букв?
# print(s.isalnum()) # строка состоит из цифр и букв?

# colors = 'red green blue'
# colors_split = colors.split() # список цветов по-отдельности

# colors_joined = ' and '.join(colors_split) # объединение строк
# print(colors_joined)
# #red and green and blue

# numbers = '1 2 3 4 5 6 7'
# num_split = numbers.split()
# print("\n".join(num_split))

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# hours = 1
# minutes = 2
# seconds = 3
# print("%02d:%02d:%02d" % (hours, minutes, seconds))

# L = ["а", "б", "в", 0, 1, 2, 3, 4]
# print (L[ :4:-1 ])
# #[4, 3, 2]

# L = ['3.3', '4.4', '5.5', '6.6']
# print (list (map ( float , L)))

# string = input("Введите числа через пробел:")
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

# list_input = input("Введите числа через пробел:").split() #получаем список
# #Подавал на вход: 1 12 3 55
# list_input[0], list_input[-1] = list_input[-1], list_input[0]
# list_input = list(map(int, list_input)) #преобразуем к целочисленному типу, чтобы посчитать сумму всех элементов
# list_input.append(sum(list_input)) #добавляем сумму всех всех элементов последним элементов списка
# #На выходе: [55, 12, 3, 1, 71]
# print(list_input)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))

# book_title = input("Название книги: ") #получаем Название книги
# book_author = input("Автор книги: ") #получаем Название книги
# book_year = int(input("Год выпуска книги: ")) #получаем Название книги
# d = {'title':book_title, 'author':book_author, 'year':book_year}
# print(d)
# print(type(d['year']))

# #The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!
# list_input = input("Введите текст:") #получаем список
# print("Количество уникальных символов: ", len(list(set(list_input))))
# #44

# a = {"Иванов", "Петров", "Васильев", "Антонов"}
# b = {"Петров", "Антонов", "Смирнов"}
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = a_set.intersection(b_set)
# print('a_and_b', a_and_b)

# a = {1, 2, 3, 4, 5, 6, 7, 8}
# b = {2, 4, 6, 8, 10, 12}
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_not_b = a_set.symmetric_difference(b_set)
# print('a_not_b', a_not_b)

# L = ['a', 'b', 'c']
# print(id(L))
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# print(id(a))
# print(id(b))
# print(id(a)-id(b))

# import numpy as np
# np.random

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
# # shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(list_id_before == list_id_after)

# Запишите вместо вопросительных знаков выражение, которое вернет True, если указывается високосный год, иначе False.
# Например, x = 2000 -> True; x = 1900 -> False; и т.д.
# Примечание: Если есть сомнения в том, какие именно годы високосные, обратитесь к Википедии
# def is_leap_year(x):
#     return ???
# x = int(input('Год: '))
# print((x % 400 == 0) or
#        not (x % 100 == 0) and
#       (x % 4 == 0))

# Дано n-значное целое число N. Определить: входят ли в него цифры 3 и 7
# N = 123456897
# print('3' in str(N) and '7' in str(N))

# Запишите вместо вопросительных знаков выражение, которое вернет True, когда каждое из чисел А и В нечетное
# def are_both_odd(A, B):
#     return ???
# A = 8
# B = 4
# if bool(A % 2 and B % 2):
#     print('А и В нечетные')
# else:
#     print('А и/или В четные')

# Использование вложенных операторов не всегда удобно. Вам дан код начинающего программиста, который не знает
# логические операторы. Он написал условие проверки принадлежности точки к координатной плоскости
# x = 1
# y = -1
# if x > 0 and y > 0:
#     print("Первая четверть")
# elif x < 0 and y > 0:
#     print("Вторая четверть")
# elif x < 0 and y < 0:
#     print("Третья четверть")
# elif x > 0 and y < 0:
#     print("Четвертая четверть")
# else:
#     print("Значение на оси координат")

# У вас есть заготовка функции — def get_wind_class(speed). Вам нужно вместо ??? написать код, который
# возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с включительно - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"

# def get_wind_class(speed):
#     if 1 < speed <= 4:
#         return 'weak [1]'
#     elif 5 < speed < 10:
#         return 'moderate [2]'
#     elif 11 < speed < 18:
#         return 'strong [3]'
#     elif 19 < speed:
#         return 'hurricane [4]'
#     else:
#         return 'Неопределенный класс'
# print(get_wind_class(1))

# Вам дан словарь user_database с именами пользователей и их паролями. Допишите функцию check_user так, чтобы она
# по логину пользователя проверяла, существует он или нет, после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Примечание: чтобы вернуть True, напишите "return True"; чтобы вернуть False, напишите "return False"
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(name, pwd):
#     if name in user_database and user_database[name] == pwd:
#         print(user_database[name] == pwd)
#         return True
#     else:
#         return False
#
# print(check_user('iseedeadpeople', 'tgm'))#'greedisgood'))
#!!!!!!!!!!!!!!!! Были ошибки - не правильно назвал переменные =)
# import warnings
# warnings.filterwarnings('ignore')
# # Введите свое решение ниже
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     print(username,' ',password)
#     if username in user_database and user_database[username] == password:
#         print(user_database[username] == password)
#         return True
#     else:
#         return False
# print(check_user(username='user', password='password'))

# Записать условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их
# A = 12
# B = 46
# C = 44
# if ((A > 45 and B <= 45 and C <= 45)or \
#     (A <= 45 and B > 45 and C <= 45) or \
#     (A <= 45 and B <= 45 and C > 45)):
#     print('Есть одно число большее 45')
# else:
#     print('Нет чила больше 45 или их несколько')

# Записать логические выражения, которые определяют, что число А не принадлежит интервалу от -10 до -1 или
# интервалу от 2 до 15
# A = -1
# if -10 <= A <= -1 or 2 <= A <= 15:
#     print("'A' принадлежит одному из диапазонов")
# else:
#     print("'A' не принадлежит одному из двух диапазонов")

# Дано двузначное число. Определить: входит ли в него цифра 5. Попробуйте решить её с использованием целочисленного
# деления и деления с остатком
# n = 15
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# Проверить, все ли элементы в списке являются уникальными
# L = [1, 3, 1, 4, 5, 6]
# S = set(L)
# if len(L) != len(S):
#     print('Есть не уникальные элементы')
# else:
#     print('Все элементы уникальны')

# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково
# слева направо и справа налево)
# N = 123454326
# N_str = str(N)
# print(N_str[::-1] == N_str)

# Соотнесите начало цикла с количеством повторений
# print(list(range(3, 5)))

# Попробуйте теперь самостоятельно подсчитать произведение всех чисел от 1 до N включительно
# P = 1  # заводим переменную-счётчик, в которой мы будем считать произведение
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N включительно
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print(P, " * ", i, " = ", (P * i))
#     P *= i  # умножаем на текущее значение i и перезаписываем значение P
# print("Конец цикла")
# print()
# print("Ответ: P = ", P)

# Написать программу, которая будет печатать лесенку следующего типа:
# n = 3
# *
# **
# ***
#
# n = 6
# for i in range(1, n + 1):
#     print('*'*i)

# Написать цикл, который будет складывать натуральные числа, пока их сумма не превысит 500.
# Заранее мы не знаем число шагов нашего цикла, но знаем условие, при котором нужно остановиться. Поэтому выберем
# цикл while и заведём две переменные для суммы и для текущего числа
# S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
# # заводим цикл while, который будет работать пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счётчик
#     print("Ещё считаю ...")
# print("Сумма равна: ", S)
# print("Количество чисел: ", n-1)

# Напишите цикл while, который находит максимальное натуральное число, квадрат которого меньше 1000
# i = 10
# while i**2 < 1000:
#     i += 1
# print(i-1,' ',(i-1)**2)

# Напишите бесконечный цикл while с условием выхода внутри цикла, находящего максимальное натуральное число,
# квадрат которого меньше 1000
# i = 1
# while True:
#     if i**2 > 1000:
#         break
#     i += 1
# print('i = ', i - 1)

# Дана двумерная матрица 3x3 (двумерный массив). Определить максимум и минимум каждой строки, а также их индексы
# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
#
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
#
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print("Минимальные элементы:", min_value_rows)
# print("Их индексы:", min_index_rows)
# print("Максимальные элементы:", max_value_rows)
# print("Их индексы:", max_index_rows)

# За один проход по циклу for мы можем либо получить само значение из списка, либо индекс, по которому дальше
# можем обратиться и получить элемент, как, например, здесь:
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# Но, чтобы убить двух зайцев сразу, есть функция enumerate. Она возвращает кортежи, где на первом месте стоит
# индекс элемента, а на втором — его значение.
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# Начинающий программист написал программу, которая находит индекс последнего отрицательного элемента в списке.
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i in range(len(list_)):
#     if list_[i] < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
# Но он не знал, что есть функция enumerate. Ваша задача — подправить код так, чтобы он работал с помощью функции enumerate
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#      else:
#          print("Положительное число: ", value)
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# # С помощью словаря в заданном тексте посчитать количество вхождений каждого символа.
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# # Символы в верхнем и нижнем регистре будем считать одинаковыми, поэтому приведём текст в нижний регистр.
# # И удалим все пробелы и символы переноса строки.
# count = {}  # для подсчёта символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
# # Заводим переменную-«счётчик» в виде словаря, где по ключу будет храниться символ, по значению — его количество.
# # Далее с помощью цикла for посимвольно будем проходиться по обработанному тексту и считать символы.
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# Допишите функцию check_h так, чтобы она проверяла гипотезу Сиракуз для числа n.
# Гипотеза Сиракуз заключается в том, что любое натуральное число можно свести к 1, если повторять над ним следующие действия:
# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
# def check_h(n):
#     while n > 1:
#         if n % 2 != 0:
#             n = n * 3 +1
#         n = n // 2
#         if n == 1:
#             return True
#     return False
# print(check_h(2))

# Рассмотрим следующую задачу: в клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги.
# Узнайте число фазанов и число кроликов.
# Количество фазанов и кроликов выражается целым числом, поэтому будем перебирать все возможные комбинации количества
# кроликов и фазанов, и если их суммарное количество ног равно указанному в условии, то мы нашли одно из решений.
# heads = 35  # количество голов
# legs = 94  # количество ног
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

# Допишите функцию print_ladder так, чтобы она для числа n печатала лесенку следующего типа:
# n = 3
# *
# **
# ***
# n = 4
# *
# **
# ***
# ****
# Функция:
# def print_ladder(n):
#     i = 1
#     for i in range(1, n + 1):
#         print('*'*i)
# print_ladder(7)

# Посчитать среднюю температуру
# country_temperature = [
#     ['Тайланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
#     ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]]
# ]
# temp = 0
# for country in country_temperature:
#     # print(len(country_temperature[i][1]))
#     temp = round(sum(map(float, country[1])) / len(country[1]), 2)
#     print(f'В стране {country[0]} средняя температура {temp} F')

# Вывести общий список ингридиентов (без разбивки на блюда), сложив в разрезе размерностей
# coock_book = {
#     'салат':[
#         {'ingredient_name':'сыр','quantity':50,'measury':'гр'},
#         {'ingredient_name': 'томаты', 'quantity': 2, 'measury': 'шт'},
#         {'ingredient_name': 'огурцы', 'quantity': 20, 'measury': 'гр'},
#         {'ingredient_name': 'маслины', 'quantity': 10, 'measury': 'гр'},
#         {'ingredient_name': 'оливковое масло', 'quantity': 20, 'measury': 'мл'},
#         {'ingredient_name': 'салат', 'quantity': 10, 'measury': 'гр'},
#         {'ingredient_name': 'перец', 'quantity': 20, 'measury': 'гр'}
#       ],
#     'пицца':[
#         {'ingredient_name':'сыр','quantity':20,'measury':'гр'},
#         {'ingredient_name': 'колбаса', 'quantity': 30, 'measury': 'гр'},
#         {'ingredient_name': 'бекон', 'quantity': 30, 'measury': 'гр'},
#         {'ingredient_name': 'оливки', 'quantity': 10, 'measury': 'гр'},
#         {'ingredient_name': 'томаты', 'quantity': 20, 'measury': 'гр'},
#         {'ingredient_name': 'тесто', 'quantity': 100, 'measury': 'гр'}
#       ],
#     'лимонад':[
#         {'ingredient_name':'лимон','quantity':1,'measury':'шт'},
#         {'ingredient_name': 'вода', 'quantity': 200, 'measury': 'мл'},
#         {'ingredient_name': 'сахар', 'quantity': 10, 'measury': 'гр'},
#         {'ingredient_name': 'лайм', 'quantity': 20, 'measury': 'гр'}
#     ]
# }
# new_dict = {}
# measury = {}
# i = 0
# item = 0
# for menu_ in coock_book.values():
#     for i in range(len(menu_)):
#         d = menu_[i]
#         key_new = d['ingredient_name'] + ' (' + d['measury'] + ')'
#         if (key_new in new_dict):
#             new_dict[key_new] = new_dict[key_new] + d['quantity']
#         else:
#             new_dict[key_new] = d['quantity']
#         i += 1
#     item += i
# print(new_dict)

# Рекурсия
# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return check(n-2)
# n = int(input('Введите число '))
# if (check(n) == True):
#     print('четное число')
# else:
#     print('нечетное число')
#
# # Генераторы
# a = [i**2 for i in range(1, 6)]
# map(int, a)

# Генератор - итератор, элемены которого можно итерировать только один раз
# Итератор - подерживает функцию next() и помнит о том, какой эл.будет браться следующим
# итерируемый объект - объект позволяющий последовательно обойти/перебрать свои элементы

# s = [1, 2, 3]
# d = iter(s)
# print(next(d)) #1
# print(next(d)) #2
# print(next(d)) #3
# print(next(d)) #ошибка

# yield == return

# Декоратор
# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper()
# def my_func():
#     print('осн.функция')
#
# my = my_decor(my_func)
# my
# def my_decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#     return wrapper
# @my_decor
# def my_func(number):
#     print(number ** 2)
#
# my_func(10)

# Напишите функцию print_2_add_2, которая будет складывать 2 и 2 и печатать этот результат.
# Не забудьте вызвать функцию, чтобы увидеть результат
# def print_2_add_2():
#     print(2 + 2)
# print_2_add_2()

# Напишите функцию hello_world, которая будет печать приветственную строку «Hello World»
# def hello_world():
#     print('Hello World')
# hello_world()

# Напишите функцию, которая проверяет, является ли число n делителем числа a и выводит на экран
# соответствующее сообщение, является ли число делителем или нет
# def check_n(n, a):
#     if (a % n):
#         print('не является')
#     else:
#         print('является')
# check_n(3, 42)

# Напишите функцию, которая печатает «обратную лесенку» следующего типа
# n = 3
# ***
# **
# *
#
# n = 4
# ****
# ***
# **
# *
# def print_ladder(n):
#     i = 1
#     for i in range(1, n + 1):
#         print('*' * i)
# print_ladder(3)
# print()
# print_ladder(4)

# Напишите функцию, которая будет возвращать количество делителей числа а
# def devCount(a):
#     i = 0
#     for j in range(1, a + 1):
#         if not (a % j):
#             # print(j)
#             i += 1
#     return i
# print(devCount(5))

# Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки.
# Пример:
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True
# def isPalindrom(inText):
#     inText = inText.lower()
#     inText = inText.replace(' ', '')
#
#     return (inText == inText[::-1])
#
# print(isPalindrom("Кит на море не романтик"))
# print(isPalindrom("test"))

# def get_mul_func(m):
#     nonlocal_m = m
#     def local_mul(n):
#         return n * nonlocal_m
#     return local_mul
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul)
# print(two_mul(5))  # 5 * 2

# Написать функцию, которая будет перемножать любое количество переданных ей аргументов
# def mult_func(*nums):
#     mul = 1
#     for n in nums:
#         mul *= n
#     return mul
# print(mult_func())
# print(mult_func(2))
# print(mult_func(2, 3, 6))
# print(mult_func(2, 3, 6, 8))

# Создадим неправильную функцию incorrect_func с указанием аргумента по умолчанию в виде списка. И вызовем эту
# функцию два раза
# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# print('-----')
# correct_func([123])
# print('-----')
# correct_func(name_arg=[123])

# Давайте рассмотрим пример с вычислением чисел Фибоначчи.
# Если вкратце, то, как известно, последовательность Фибоначчи начинается с 1 и 1, после чего каждое новое число
# является результатом сложения двух предыдущих чисел. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...
# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
# rec_fibb(10)  # 55

# С помощью рекурсивной функции найдите сумму чисел от 1 до n
# def NumberSum(n):
#     if n == 1:
#         return 1
#     return n + NumberSum(n - 1)
# print(NumberSum(15))

# С помощью рекурсивной функции разверните строку
# def StrReverse(text):
#     if len(text) == 0:
#         return ''
#     else:
#         return text[-1] + StrReverse(text[:-1])
# print(StrReverse('test'))

# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется)
# def NumberSum(n):
#     if n <= 0:
#        return 0
#     return n % 10 + NumberSum(n // 10)
# print(NumberSum(1876)) #22

# Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел. По умолчанию она
# начинается с единицы, её шаг равен 1, но пользователь может указать любой шаг и любое число в качестве
# аргумента функции, с которого будет начинаться последовательность
# def count(start=1, step=1):
#     counter = start
#     # print(start, ' - ', step)
#     while True:
#         yield counter
#         counter += step
# start = int(input('Введите начальное значение: '))
# step = int(input('Введите шаг: '))
# for num in count(start, step):
#     if num > 100:
#         break
#     print('num = ', num)

# Создать генератор цикла, то есть в функцию на входе будет передаваться массив, например, [1, 2, 3], генератор
# будет вечно работать возвращая 1 2 3 1 2 3… и так далее
# def GenArray(array_):
#     while True:
#         for counter in array_:
#             yield counter
# i = 0
# for num in GenArray([1, 2, 3]):
#     if i > 100:
#         break
#     i += 1
#     print(num)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

# Функция высшего порядка — в программировании это функция, принимающая в качестве аргументов другие функции
# или возвращающая другую функцию в качестве результата
# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()
#
# def hello():
#     print("Hello")
#
# test = twice_func(hello)

# Замыкание в программировании — это функция, в теле которой присутствуют ссылки на переменные, объявленные вне
# тела этой функции в окружающем коде и не являющиеся её аргументами
# def make_adder(x):
#    def adder(n):
#        return x + n # захват переменной "x" из nonlocal области
#    return adder  # возвращение функции в качестве результата
# # функция, которая будет к любому числу прибавлять пятёрку
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105

# Декораторы предназначены для подключения любого дополнительного поведения к основной функции,
# называемой декорируемой функцией, которое может выполняться до, после или даже вместо основной функции.
# При этом исходный код декорируемой функции никак не затрагивается
# - Декораторы добавляют дополнительное поведение функции без изменения её исходного кода.
# - Декораторы — вызовы дополнительных функций, поэтому они немного замедляют ваш код.
# - Для передачи аргументов декорируемой функции используйте *args и **kwargs.
# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обёртку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#         print("Я буду выполнен после основного вызова!")
#         return result
#     return wrapper
#
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0

# Возьмите из предыдущего примера декорированные функции, которые возвращают время работы основной функции.
# Найдите среднее время выполнения для 100 выполнений каждой функции
# import time
# N = 100
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
# def pow_2():
#     return 1000000000 ** 2
#
# def in_build_pow():
#     return pow(1000000000, 2)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#     mean_pow_2 += pow_2()
#     mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")

# Синтаксический сахар в языке программирования — это синтаксические возможности, применение которых не влияет на
# поведение программы, но делает использование языка более удобным для человека
# def my_decorator(fn):
#    def wrapper():
#        fn()
#    return wrapper  # возвращается задекорированная функция, которая заменяет исходную
#
# # выведем незадекорированную функцию
# def my_function():
#    pass
# print(my_function)  # <function my_function at 0x7f938401ba60>
#
# # выведем задекорированную функцию
# @my_decorator
# def my_function():
#    pass
# print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>

# декоратор, в котором встроенная функция умеет принимать аргументы
# def do_it_twice(func):
#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
# @do_it_twice
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# Oo!!!
# Oo!!!

# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. Для хранения
# переменной, содержащей количество вызовов, используйте nonlocal область декоратора
# def do_it_twice(func):
#     nonlocal_int = 0
#     def wrapper(*args, **kwargs):
#         nonlocal nonlocal_int
#         nonlocal_int += 1
#         func(*args, **kwargs)
#     return wrapper
#
# @do_it_twice
# def say_word(word):
#     print(word)
#
# say_word("Aa!!!")
# say_word("Uu!!!")
# say_word("Oo!!!")

# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре. Словарь
# должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент функции, по значению —
# результат работы функции, например, {n: f(n)}.
# И при повторном вызове функции декоратор будет брать значение из словаря, а не вычислять заново. То есть словарь
# можно считать промежуточной памятью на время работы программы, где будут храниться ранее вычисленные значения.
# Исходная функция, которую нужно задекорировать имеет следующий вид и выполняет простое умножение на число 123456789:
# def dict_write(func):
#     nonlocal_int = 0
#     nonlocal_dict = {}
#     def wrapper(nonlocal_int):
#         nonlocal nonlocal_dict
#         if nonlocal_int not in nonlocal_dict:
#             nonlocal_dict[nonlocal_int] = func(nonlocal_int)
#             print(nonlocal_dict)
#         else:
#             print('Возвращаемое значение: ', nonlocal_dict[nonlocal_int])
#     return wrapper
#
# @dict_write
# def f(n):
#    return n * 123456789
#
# for i in range(10):
#     f(i)
#     f(i)

# Как работают импорт и вызов функций
# def _print_hi(a):
#     return f'Hi, {a}'
# if __name__ == '__main__':
#     print(_print_hi('V'))

# Содержимое директории .git
# Рассмотрим, что содержится в папках и файлах:
#
# В файле config находятся настройки данного репозитория. Его содержимое представлено в текстовом формате.
# Файл HEAD указывает на текущую ветку.
# В файле index хранится содержимое индекса.
# В директории objects находится, собственно, база данных объектов Git. Если открыть каталог objects, то в нём будут находиться каталоги, имена которых представлены двумя шестнадцатеричными числами, внутри них будут файлы, имена которых представлены 38 шестнадцатеричными числами. Вместе имя каталога и файл образуют 40-разрядный хеш, взятый от имени файла и его содержимого.
# В директории refs находятся ссылки на объекты коммитов в этой базе (ветки).
# Директория logs хранит логи коммитов.
# В директории info расположен файл с глобальными настройкам игнорирования файлов. Он позволяет исключить файлы, которые вы не хотите помещать в .gitignore. Позднее мы остановимся на назначении файла .gitignore.
# В директории hooks располагаются клиентские и серверные триггеры. Желающие прочитать про них могут обратиться к руководству по Git.