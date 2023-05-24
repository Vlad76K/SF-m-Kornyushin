# C2.5. Итоговое практическое задание
# Используя знания, полученные в данном модуле, напишите следующее приложение:
# Суть написанного приложения — игра «Морской бой».
# Интерфейс приложения должен представлять собой консольное окно с двумя полями 6х6 вида:
#   | 1 | 2 | 3 | 4 | 5 | 6 |
# 1 | О | О | О | О | О | О |
# 2 | О | О | О | О | О | О |
# 3 | О | О | О | О | О | О |
# 4 | О | О | О | О | О | О |
# 5 | О | О | О | О | О | О |
# 6 | О | О | О | О | О | О |
#
# Игрок играет с компьютером. Компьютер делает ходы наугад, но не ходит по тем клеткам, в которые он уже сходил.
# Для представления корабля на игровой доске напишите класс Ship (в конструктор передаём информацию о его положении на доске).
# Опишите класс доски, на которую будут размещаться корабли.
# Корабли должны находится на расстоянии минимум одна клетка друг от друга.
# Корабли на доске должны отображаться следующим образом (пример):
#   | 1 | 2 | 3 | 4 | 5 | 6 |
# 1 | ■ | ■ | ■ | О | О | О |
# 2 | О | О | О | О | ■ | ■ |
# 3 | О | О | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |
#
# На каждой доске (у ИИ и у игрока) должно находится следующее количество кораблей: 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.
# Запретите игроку стрелять в одну и ту же клетку несколько раз. При ошибках хода игрока должно возникать исключение.
#   | 1 | 2 | 3 | 4 | 5 | 6 |
# 1 | X | X | X | О | О | О |
# 2 | О | О | О | О | X | X |
# 3 | О | T | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |
#
# В случае, если возникают непредвиденные ситуации, выбрасывать и обрабатывать исключения.
# Буквой X помечаются подбитые корабли, буквой T — промахи.
# Побеждает тот, кто быстрее всех разгромит корабли противника.
import sys

from numpy import random, copy

class Dot: # класс точек на поле
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if (self.x, self.y) == (other.x, other.y):
            return True
        return False

class Ship:
    def __init__(self, length, start_point, vertical, vitality, list_ship):
        self.length = length                # Длина
        self.start_point = start_point      # Точка, где размещён нос корабля
        self.vertical = vertical            # Направление корабля (вертикальное (True)/горизонтальное (False))
        self.vitality = vitality            # Количеством жизней (сколько точек корабля ещё не подбито)
        self.list_ship = list_ship          # Список кораблей доски.

    def dots(self):  # возвращает список всех точек корабля
        dots_ = Dot(0, 0)
        ls_point = []
        for ln in range(self.length):
            ls_point.append([dots_.x, dots_.y])

class Board:
    def __init__(self, list_prop_cell, list_ship, hid, num_live_ship, pick_list, pick_hide):
        self.list_prop_cell = list_prop_cell  # Двумерный список, в котором хранятся состояния каждой из клеток
        self.list_ship = list_ship            # Список кораблей доски.
        self.hid = hid                        # Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске (для вывода доски врага) или нет (для своей доски).
        self.num_live_ship = num_live_ship    # Количество живых кораблей на доске
        self.pick_list = pick_list            # доска компа (визуализируемая)
        self.pick_hide = pick_hide            # доска компа предподготовленная

    def add_ship(self): # ставит корабль на доску (если ставить не получается, выбрасываем исключения)
        _ship_list = []
        user = User(self.list_prop_cell, self.pick_list, self.pick_hide)
        ship = Ship(self.list_ship[0], [], None, 0, _ship_list)

        for i in range(len(self.list_ship)):
            print(f'Ставим {self.list_ship[i]}-палубник')
            j = 0
            while j < int(self.list_ship[i]):  # in range(int(self.list_ship[i])):
                ask = user.ask()

                x = ask[0]
                y = ask[1]

                if j == 0:
                    ship.length = self.list_ship[i]
                    ship.start_point = [x, y]
                    if ship.start_point[0] == x:
                        ship.vertical = False
                    elif ship.start_point[1] == y:
                        ship.vertical = True
                    self.vitality = ship.length  # Количеством жизней (сколько точек корабля ещё не подбито)

                if self.list_prop_cell[x][y] != '■' and self.list_prop_cell[x][y] != 'F':
                    if (not ship.vertical and ship.start_point[0] - x != 0) or (ship.vertical and ship.start_point[1] - y != 0):
                        print('Можно использовать только вертикальное или горизонтальное расположение корабля')
                    else:
                        if (abs(ship.start_point[0] - x) < self.list_ship[i]) \
                            and (abs(ship.start_point[1] - y) < self.list_ship[i]):
                            _ship_list.append([x, y])
                            self.list_prop_cell[x][y] = '■'
                            j += 1
                        else:
                            print('Элементы корабля слишком далеко разнесены друг от друга. Повторите ввод')
                    self.hid_board()
                else:
                    print('В эту ячейку нельзя поставть корабль!')
            ship.list_ship = _ship_list
            self.friz_cell = _ship_list
            self.contour()
            print('Вокруг корабля фризим область, чтобы новые не ставить вплотную')
            self.hid_board()

    def contour(self):  # обводит корабль по контуру
        # Он будет полезен и в ходе самой игры, и при расстановке кораблей (помечает соседние точки, где корабля по правилам быть не может)
        # print('list_prop_cell = ', self.list_prop_cell, ' --- self.friz_cell = ', self.friz_cell)
        _friz_cell = self.list_prop_cell
        for i in range(len(_friz_cell)):
            for j in range(len(_friz_cell)):
                if _friz_cell[i][j] == '■':
                    # if not self.out():
                    if i - 1 >= 0 and _friz_cell[i - 1][j] != '■':
                        _friz_cell[i - 1][j] = 'F'  # 'O'
                    if i + 1 < 6 and _friz_cell[i + 1][j] != '■':
                        _friz_cell[i + 1][j] = 'F'  # 'O'
                    if j - 1 >= 0 and _friz_cell[i][j - 1] != '■':
                        _friz_cell[i][j - 1] = 'F'  # 'O'
                    if j + 1 < 6 and _friz_cell[i][j + 1] != '■':
                        _friz_cell[i][j + 1] = 'F'  # 'O'
                    if i - 1 >= 0 and j - 1 >= 0 and _friz_cell[i - 1][j - 1] != '■':
                        _friz_cell[i - 1][j - 1] = 'F'  # 'O'
                    if i + 1 < 6 and j + 1 < 6 and _friz_cell[i + 1][j + 1] != '■':
                        _friz_cell[i + 1][j + 1] = 'F'  # 'O'
                    if i + 1 < 6 and j - 1 >= 0 and _friz_cell[i + 1][j - 1] != '■':
                        _friz_cell[i + 1][j - 1] = 'F'  # 'O'
                    if i - 1 >= 0 and j + 1 < 6 and _friz_cell[i - 1][j + 1] != '■':
                        _friz_cell[i - 1][j + 1] = 'F'  # 'O'
        self.list_prop_cell = _friz_cell

    def check_win_comp(self): # проверки достижения победы
        for i in range(6):
            if '■' in self.list_prop_cell[i]: # если находим "живой участок" у выставленных кораблей - нет победы у компа
                return True
        print('Компьютер выиграл!')
        return False

    def check_win_user(self):  # проверки достижения победы
        sum_el = 0
        for i in range(6):
            for j in range(6):  # len(self.pick_list[i])):
                if self.pick_list[i][j] == 'X':
                    sum_el += 1
        if sum_el == 11:  # все корабли компа подбиты =)
            print('Поздравляю! Вы победили!')
            return False
        return True

    def hid_board(self): # выводит доску в консоль в зависимости от параметра hid
        print('  | 1 | 2 | 3 | 4 | 5 | 6 |           | 1 | 2 | 3 | 4 | 5 | 6 |')
        for i in range(6):
            print(i+1, '| {} | {} | {} | {} | {} | {} |'.format(*self.list_prop_cell[i]) , '       ', i+1, '| {} | {} | {} | {} | {} | {} |'.format(*self.pick_list[i]))

    def out(self): # для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля, и False, если не выходит
        dot = Dot(0, 0)

        if dot.x - 1 < 0 or dot.x + 1 > 5 or dot.y - 1 < 0 or dot.y + 1 > 5:
            return True
        return False

    def shot(self): # делает выстрел по доске (если есть попытка выстрелить за пределы и в использованную точку, нужно выбрасывать исключения)
        user = User(self.list_prop_cell, self.pick_list, self.pick_hide)
        ai = AI(self.list_prop_cell, self.pick_list, self.pick_hide)

        while self.check_win_user() and self.check_win_comp():
            user.move()
            ai.move()

            self.hid_board()

class Player:
    move_prm = False

    def __init__(self, self_board, other_board, hide_board):
        self.self_board = self_board    # своя доска
        self.other_board = other_board  # доска противника
        self.hide_board = hide_board    # доска противника

    def ask(self):  # метод, который «спрашивает» игрока, в какую клетку он делает выстрел. Пока мы делаем общий для AI
                    # и пользователя класс, этот метод мы описать не можем. Оставим этот метод пустым. Тем самым обозначим, что потомки должны реализовать этот метод
                    # список кораблей, которые пользователь будет расставлять на поле
        ...

    def move(self):  # метод, который делает ход в игре
                     # Тут мы вызываем метод ask, делаем выстрел по вражеской доске (метод Board.shot), отлавливаем исключения,
                     # и если они есть, пытаемся повторить ход. Метод должен возвращать True, если этому игроку нужен повторный ход (например, если он выстрелом подбил корабль)
        self.move_prm = True
        move_ask = self.ask()
        move_x = move_ask[0]
        move_y = move_ask[1]
        # if self.move_prm:
        #     self.other_board[move_x][move_y] = 'X'

        return True

class AI(Player):
    def ask(self): # выбор случайной точки
        dic_key = random.randint(1, 36)  # рандомно получаем ключ к координатам по которым доллжен ударить компьютер
        if list(_comp_move.get(dic_key)) == [0, 0]:  # если по ключу лежат нулевые координаты
            while list(_comp_move.get(dic_key)) == [0, 0]:  # инкрементим ключ и ищем следующие не нулевые
                if dic_key >= 36:
                    dic_key = 1
                dic_key += 1
        cell_coord_list = list(_comp_move.get(dic_key))  # опеределили координаты по которым будет бить комп
        _comp_move[dic_key] = [0, 0]  # обнуляем использованные координаты
        print(f'Ход компьютера! Ячейка {cell_coord_list}')

        ai_x = int(cell_coord_list[0]) - 1
        ai_y = int(cell_coord_list[1]) - 1

        if self.self_board[ai_x][ai_y] == '■':
            self.self_board[ai_x][ai_y] = 'X'
        else:
            self.self_board[ai_x][ai_y] = 'T'

        return [ai_x, ai_y]

class User(Player):
    def ask(self):  # спрашивает координаты точки из консоли
        if self.move_prm:
            cell_coord_list = list(map(int, input('Куда стреляем? Координаты: ').split()))
        else:
            cell_coord_list = list(map(int, input('Куда ставим корабль? Координаты: ').split()))

        user_x = int(cell_coord_list[0]) - 1
        user_y = int(cell_coord_list[1]) - 1

        if self.move_prm:
            if self.other_board[user_x][user_y] == 'X' or self.other_board[user_x][user_y] == 'T':
                raise ValueError("По данной ячейке уже стреляли")
            else:
                if self.hide_board[user_x][user_y] == '■':
                    self.other_board[user_x][user_y] = 'X'
                else:
                    self.other_board[user_x][user_y] = 'T'

        return [user_x, user_y]

class Game:
    def __init__(self, player_user, user_board, ai_user, ai_board, _ship_nom, pick_hide):
        self.player_user = player_user  # Игрок-пользователь, объект класса User
        self.user_board = user_board    # Доска пользователя
        self.ai_user = ai_user          # Игрок-компьютер, объект класса AI
        self.ai_board = ai_board        # Доска компьютера
        self._ship_nom = _ship_nom      # Массив кораблей
        self.pick_hide = pick_hide      # Предподготовленное поле ai

    def random_board(self):  # метод генерирует случайную доску
        # мы просто пытаемся в случайные клетки изначально пустой доски расставлять корабли (в бесконечном цикле
        # пытаемся поставить корабль в случайную доску, пока наша попытка не окажется успешной). Лучше расставлять
        # сначала длинные корабли, а потом короткие. Если было сделано много (несколько тысяч) попыток установить
        # корабль, но это не получилось, значит доска неудачная и на неё корабль уже не добавить. В таком случае
        # нужно начать генерировать новую доску
        _comp_random = copy(_comp_move)
        for i in range(len(_ship_nom)):
            cnt = 0
            j = 0
            while j < _ship_nom[i]:
                if cnt == 10000:
                    break
                cnt += 1
                if j == 0:
                    random_start_cell = random.randint(1, 36)  # рандомно получаем координату X
                    if list(_comp_move.get(random_start_cell)) == [0, 0]:  # если по ключу лежат нулевые координаты
                        s_lst = 0
                        while list(_comp_move.get(random_start_cell)) == [0, 0]:  # инкрементим ключ и ищем следующие не нулевые
                            if s_lst == 40:
                                break
                            if random_start_cell >= 36:
                                random_start_cell = 1
                            random_start_cell += 1
                            s_lst += 1
                    cell_coord_list = list(_comp_move.get(random_start_cell))  # опеределили координаты
                    _comp_move[random_start_cell] = [0, 0]  # обнуляем использованные координаты

                    random_vertical = random.randint(0, 1) # рандомно определяем по вертикали или горизонтали ставим
                    _cell_x = cell_coord_list[0]-1
                    _cell_y = cell_coord_list[1]-1
                else:
                    if not random_vertical:
                        if _cell_x == 0:
                            while empty_board[_cell_x][_cell_y] == '■' and _cell_x <= 5:
                                _cell_x = _cell_x + 1
                        elif _cell_x == 5:
                            while empty_board[_cell_x][_cell_y] == '■':
                                _cell_x = _cell_x - 1
                        else:
                            _cell_x = _cell_x + 1
                    else:
                        if _cell_y == 0:
                            _cell_y = _cell_y + 1
                        elif _cell_y == 5:
                            _cell_y = _cell_y - 1

                if empty_board[_cell_x][_cell_y] == 'О':
                    empty_board[_cell_x][_cell_y] = '■'
                    j += 1

            board = Board(empty_board, _ship_nom, False, 7, [], [])
            board.contour()

        for k in range(6):
            print(k + 1, '| {} | {} | {} | {} | {} | {} |'.format(*empty_board[k]))

    def greet(self):  # метод, который в консоли приветствует пользователя и рассказывает о формате ввода
        print(
            '*********************************************\n'
            '           Игра «Морской бой»\n'
            '*********************************************\n'
            'Вам дается два поля:\n'
            '   1. поле для расстановки своих кораблей\n'
            '   2. поле по которому Вы будете наносить\n'
            '      удары, пытаясь потопить корабли компьютера\n'
            'В обоих случаях аккуратно вводите координаты (строка - пробел - столбец). Например: 1 5\n'
            'При расстановке своих кораблей учитывайте, что нельзя их располагать вплотную дуг к другу\n'
            'При нанесении ударов по полю компьютера, нельзя бить в одну и ту же точку - это завершит игру\n'
            'Удачи!'
        )

    def loop(self):  # метод с самим игровым циклом. Здесь мы просто последовательно вызываем метод mode для игроков
                     # и делаем проверку, сколько живых кораблей осталось на досках, чтобы определить победу
        print('Поставьте корабли на поле: 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку')
        print('Без диагональных и Г-образных')
        board = Board(self.user_board, self._ship_nom, False, 7, self.ai_board, self.pick_hide)
        board.hid_board()
        board.add_ship()
        board.shot()

    def start(self):  # запуск игры. Сначала вызываем greet, а потом loop
        self.greet()
        self.loop()

try:
    # Использую как базу для ходов компа. Рандомно выбираем ключ. Использованное значение по ключу обнуляем и при
    # повторном попадании инкрементим ключ до следующего с ненулевым value
    _comp_move = {
        1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [1, 4], 5: [1, 5], 6: [1, 6],
        7: [2, 1], 8: [2, 2], 9: [2, 3], 10: [2, 4], 11: [2, 5], 12: [2, 6],
        13: [3, 1], 14: [3, 2], 15: [3, 3], 16: [3, 4], 17: [3, 5], 18: [3, 6],
        19: [4, 1], 20: [4, 2], 21: [4, 3], 22: [4, 4], 23: [4, 5], 24: [4, 6],
        25: [5, 1], 26: [5, 2], 27: [5, 3], 28: [5, 4], 29: [5, 5], 30: [5, 6],
        31: [6, 1], 32: [6, 2], 33: [6, 3], 34: [6, 4], 35: [6, 5], 36: [6, 6]
    }
    # user_board = [
    #     ['■', '■', '■', 'О', 'О', 'О'],
    #     ['О', 'О', 'О', 'О', '■', '■'],
    #     ['О', 'О', 'О', 'О', 'О', 'О'],
    #     ['■', 'О', '■', 'О', '■', 'О'],
    #     ['О', 'О', 'О', 'О', '■', 'О'],
    #     ['■', 'О', '■', 'О', 'О', 'О']
    # ]
    empty_board = [
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', 'О', 'О']
    ]
    pick_hide0 = [
        ['■', 'О', '■', '■', 'О', 'О'],
        ['■', 'О', 'О', 'О', '■', 'О'],
        ['■', 'О', 'О', 'О', '■', 'О'],
        ['О', 'О', 'О', '■', 'О', 'О'],
        ['О', 'О', 'О', 'О', '■', 'О'],
        ['О', 'О', 'О', '■', 'О', '■']
    ]
    pick_hide1 = [
        ['О', '■', '■', '■', 'О', 'О'],
        ['О', 'О', 'О', 'О', '■', 'О'],
        ['■', '■', 'О', 'О', 'О', 'О'],
        ['О', 'О', '■', '■', 'О', '■'],
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['■', 'О', 'О', '■', 'О', 'О']
    ]
    pick_hide2 = [
        ['■', 'О', '■', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', '■', 'О'],
        ['■', '■', 'О', 'О', 'О', 'О'],
        ['О', 'О', 'О', '■', 'О', '■'],
        ['О', 'О', 'О', '■', 'О', '■'],
        ['■', 'О', 'О', '■', 'О', 'О']
    ]
    pick_hide3 = [
        ['■', '■', '■', 'О', 'О', 'О'],
        ['О', 'О', 'О', 'О', '■', '■'],
        ['О', 'О', 'О', 'О', 'О', 'О'],
        ['■', 'О', '■', 'О', '■', 'О'],
        ['О', 'О', 'О', 'О', '■', 'О'],
        ['■', 'О', '■', 'О', 'О', 'О']
    ]

    _ship_nom = [3, 2, 2, 1, 1, 1, 1]

    ai_board = copy(empty_board)
    user_board = copy(empty_board)

    player_user = User
    ai_user = AI

    d_key = random.randint(1, 4) # выбор ключа "поля компа"
    if d_key == 1:
        pick_hide = pick_hide1
    elif d_key == 2:
        pick_hide = pick_hide2
    elif d_key == 3:
        pick_hide = pick_hide3
    else:
        pick_hide = pick_hide0

    game = Game(player_user, user_board, ai_user, ai_board, _ship_nom, pick_hide)
    game.start()
    # game.random_board()

except ValueError as error:
    print(error)
except IndexError as error:
    print(error)
else:
    print('Игра завершена!')
finally:
    print('Спасибо, что выбрали нашу компанию! =)')

