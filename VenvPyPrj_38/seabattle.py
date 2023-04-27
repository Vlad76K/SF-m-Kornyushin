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

from numpy import random

class SeaBattle:
    _ErrorId = 0
    _ship_list = []
    _pick_list = []
    def __init__(self, x, y, z, bf_list, pick_list, pick_list1):
        self.x = x
        self.y = y
        self.z = z
        self.bf_list = bf_list
        self.pick_list = pick_list
        self.pick_list1 = pick_list1

    def show(self): # вывод поля игры на экран
        print('  | 1 | 2 | 3 | 4 | 5 | 6 |           | 1 | 2 | 3 | 4 | 5 | 6 |')
        for i in range(6):
            print(i+1, '| {} | {} | {} | {} | {} | {} |'.format(*self.bf_list[i]), '       ', i+1, '| {} | {} | {} | {} | {} | {} |'.format(*self.pick_list[i]))
            i += 1
    @property
    def check_pick_error(self):
        ...
    def pick_ship(self): # здесь мы ищем в указанном месте корабль компьютера (визульно не отображается)
        # выбор поля по которому стреляем, в зависимости от того, чей ход
        if self.z:
            pl = self.pick_list1 # если ходит игрок
        else:
            pl = self.bf_list # если ходит компьютер

        if pl[self.x][self.y] == 'X' or pl[self.x][self.y] == 'T': # уже били по этой точке
            self._ErrorId = 1
            raise ValueError('По данной ячейке уже стреляли')
        elif pl[self.x][self.y] == '■': # попали по кораблю
            return 'X'
        elif pl[self.x][self.y] == 'О': # в клетку еще не били и на ней нет корабли
            return 'T'
        else:
            self._ErrorId = 2
            raise IndexError('Ошибка выбора цели! Клетка за пределами поля!')

    @property
    def pick_cell_user(self): # ход игрока - выстрел по ячейке
        return 'X' #????????????????????????????????????????????????????
    @pick_cell_user.setter
    def pick_cell_user(self, value): # ход игрока - выстрел по ячейке
        if self.pick_list[self.x][self.y] == value:
            raise ValueError("По данной ячейке уже стреляли")
        else:
            self.pick_list[self.x][self.y] = value

    @property
    def pick_cell_comp(self): # ход игрока - выстрел по ячейке
        return 'X' #????????????????????????????????????????????????????

    @pick_cell_comp.setter
    def pick_cell_comp(self, value): # ход игрока - выстрел по ячейке
        if self.bf_list[self.x][self.y] == value:
            raise ValueError("По данной ячейке уже стреляли (pc)")
        else:
            self.bf_list[self.x][self.y] = value

    def check_win_comp(self): # проверки достижения победы
        for i in range(6):
            if '■' in self.bf_list[i]: # если находим "живой участок" у выставленных кораблей - нет победы у компа
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

class ErrorWorcker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def error_check_(self):
        if self.x == 0:
            x_plus = self.x + 1
            x_minus = 0
        elif self.x == 5:
            x_plus = self.x
            x_minus = self.x - 1
        else:
            x_plus = self.x + 1
            x_minus = self.x - 1

        if self.y == 0:
            y_plus = self.x + 1
            y_minus = 0
        elif self.y == 5:
            y_plus = self.x
            y_minus = self.x - 1
        else:
            y_plus = self.x + 1
            y_minus = self.x - 1

        return ((sb_cls.bf_list[x_minus][self.y] != '■') or (sb_cls.bf_list[x_minus][self.y] == '■')) and \
               ((sb_cls.bf_list[x_plus][self.y] != '■') or (sb_cls.bf_list[x_plus][self.y] == '■')) and \
               ((sb_cls.bf_list[self.x][y_minus] != '■') or (sb_cls.bf_list[self.x][y_minus] == '■')) and \
               ((sb_cls.bf_list[self.x][y_plus] != '■') or (sb_cls.bf_list[self.x][y_plus] == '■'))

class CheckUseCell:
    def __init__(self, x, y, first_x, first_y, i, ship_frize_list, ship_element_list):
        self.x = x
        self.y = y
        self.first_x = first_x
        self.first_y = first_y
        self.i = i
        self.ship_frize_list = ship_frize_list
        self.ship_element_list = ship_element_list

    def error_check(self):
        if self.x == 0:
            x_plus = self.x + 1
            x_minus = 0
        elif self.x == 5:
            x_plus = self.x
            x_minus = self.x - 1
        else:
            x_plus = self.x + 1
            x_minus = self.x - 1

        if self.y == 0:
            y_plus = self.x + 1
            y_minus = 0
        elif self.y == 5:
            y_plus = self.x
            y_minus = self.x - 1
        else:
            y_plus = self.x + 1
            y_minus = self.x - 1

        print((self.x, self.y), ' --- ', (self.first_x, self.first_y), ' --- ', self.i)
        print('ship_element_list: ', self.ship_element_list)
        orient = (self.x, self.y) in self.ship_element_list

        return ((sb_cls.bf_list[x_minus][self.y] != '■') or (sb_cls.bf_list[x_minus][self.y] == '■' and orient))\
               and ((sb_cls.bf_list[x_plus][self.y] != '■') or (sb_cls.bf_list[x_plus][self.y] == '■' and orient))\
               and ((sb_cls.bf_list[self.x][y_minus] != '■') or (sb_cls.bf_list[self.x][y_minus] == '■' and orient))\
               and ((sb_cls.bf_list[self.x][y_plus] != '■') or (sb_cls.bf_list[self.x][y_plus] == '■' and orient))

    def we_can_use_this_cell(self):
        if not (0 <= self.x < 6 and 0 <= self.y < 6):
            print('Координаты вне поля! Повторите выбор!')
            return False

        if sb_cls.bf_list[self.x][self.y] != 'О':  # ячейка не свободна
            print('Ячейка уже занята. Выберите другую')
            return False

        if self.x == 0:
            x_plus = self.x + 1
            x_minus = 0
        elif self.x == 5:
            x_plus = self.x
            x_minus = self.x - 1
        else:
            x_plus = self.x + 1
            x_minus = self.x - 1

        if self.y == 0:
            y_plus = self.x + 1
            y_minus = 0
        elif self.y == 5:
            y_plus = self.x
            y_minus = self.x - 1
        else:
            y_plus = self.x + 1
            y_minus = self.x - 1

        num = 0
        if sb_cls.bf_list[x_minus][self.y] == '■':
            num += 1
        if sb_cls.bf_list[x_plus][self.y] == '■':
            num += 1
        if sb_cls.bf_list[self.x][y_minus] == '■':
            num += 1
        if sb_cls.bf_list[self.x][y_plus] == '■':
            num += 1

        # print((self.x, self.y),' not in ', self.ship_frize_list)
        if self.i == 0:
            if num == 0: # (self.x, self.y) not in self.ship_frize_list and
                return self.error_check()

                # необходимо проверить четыре ячейки (по две по горизонтали и вертикали) - не заняты ли
                # нельзя распологать корабли впритык ( исключая диагональ ?)
                # при этом нужно исключать из рассмотрения уже установленные блоки того же корабля
                # if self.x == 0 and self.y == 0:  # верхний левый угол
                #     return ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■'))
                # elif self.x == 0 and self.y == 5:  # верхний правый угол
                #     return ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■'))
                # elif self.x == 5 and self.y == 0:  # нижний левый угол
                #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■'))
                # elif self.x == 5 and self.y == 5:  # нижний правый угол
                #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■'))
                # elif self.x == 0:  # верхний край поля
                #     return ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■'))
                # elif self.y == 0:  # левый край
                #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■'))
                # elif self.x == 5:  # нижний край
                #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■'))
                # elif self.y == 5:  # правый край
                #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■'))
                # else:
                #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■')) and \
                #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■'))
            else:
                print('1. Нельзя располагать корабли вплотную!')
                return False
        else:
            if self.x == self.first_x or self.y == self.first_y: # либо вертикаль, либо горизонталь
                if num == 1:
                    return self.error_check()
                    # and (self.x, self.y) not in self.ship_frize_list #and (self.x + self.i == self.first_x and self.y == self.first_y)

                    # if self.x == 0 and self.y == 0: # верхний левый угол
                    #     # print(5)
                    #     return ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■' and self.x + self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■' and self.x == self.first_x and self.y + self.i == self.first_y))
                    # elif self.x == 0 and self.y == 5: # верхний правый угол
                    #     # print(6)
                    #     return ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■' and self.x + self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■' and self.x == self.first_x and self.y - self.i == self.first_y))
                    # elif self.x == 5 and self.y == 0:  # нижний левый угол
                    #     # print(7)
                    #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■' and self.x - self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■' and self.x == self.first_x and self.y + self.i == self.first_y))
                    # elif self.x == 5 and self.y == 5:  # нижний правый угол
                    #     # print(8)
                    #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■' and self.x - self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■' and self.x == self.first_x and self.y - self.i == self.first_y))
                    # elif self.x == 0:  # верхний край поля
                    #     # print(9)
                    #     return ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■' and self.x + self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■' and self.x == self.first_x and self.y - self.i == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■' and self.x == self.first_x and self.y + self.i == self.first_y))
                    # elif self.y == 0: # левый край
                    #     # print(10)
                    #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■' and self.x - self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■' and self.x + self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■' and self.x == self.first_x and self.y + self.i == self.first_y))
                    # elif self.x == 5: # нижний край
                    #     # print(11)
                    #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■' and self.x - self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■' and self.x == self.first_x and self.y - self.i == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■' and self.x == self.first_x and self.y + self.i == self.first_y))
                    # elif self.y == 5: # правый край
                    #     # print(12)
                    #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■' and self.x - self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■' and self.x + self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■' and self.x == self.first_x and self.y - self.i == self.first_y))
                    # else:
                    #     # print(13)
                    #     return ((sb_cls.bf_list[self.x - 1][self.y] != '■') or (sb_cls.bf_list[self.x - 1][self.y] == '■' and self.x - self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x + 1][self.y] != '■') or (sb_cls.bf_list[self.x + 1][self.y] == '■' and self.x + self.i == self.first_x and self.y == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y - 1] != '■') or (sb_cls.bf_list[self.x][self.y - 1] == '■' and self.x == self.first_x and self.y - self.i == self.first_y)) and \
                    #            ((sb_cls.bf_list[self.x][self.y + 1] != '■') or (sb_cls.bf_list[self.x][self.y + 1] == '■' and self.x == self.first_x and self.y + self.i == self.first_y))
                else:
                    print('2. По соседству более одного корабельного модуля!')
                    return False
            else:  # диогональ - ошибка
                print('2. По диагонали размещать нельзя!')
                return False

class Ship: # класс размещения кораблей на поле
    def __init__(self, x, y, bf_list, _ship_set, _frize_set, ship_l):
        self.x = x
        self.y = y
        self.bf_list = bf_list
        self._ship_set = _ship_set
        self._frize_set = _frize_set
        self.ship_l = ship_l

    def set_ship(self): # расставим корабли
        sb_cls = SeaBattle(0, 0, True, user_data, pick_visual, pick_hide)
        sb_err = CheckUseCell(0, 0, 0, 0, 0, _ship_frize_list, _ship_element_list)

        # ставим 3-х палубник
        print(f'Ставим {self.ship_l}-палубник')
        i = 0
        while i < self.ship_l:
            cell_coord_list = list(input(f'Введите координаты ячейки {i+1}: ').split())
            x = int(cell_coord_list[0]) - 1
            y = int(cell_coord_list[1]) - 1

            sb_err.x = x
            sb_err.y = y
            sb_err.i = i
            if i == 0:
                self._ship_set = []
                sb_err.first_x = x
                sb_err.first_y = y

            if sb_err.we_can_use_this_cell():
                print(sb_cls.bf_list[x][y], ' - ', sb_cls.bf_list[x+1][y], ' - ', sb_cls.bf_list[x][y-1], ' - ', sb_cls.bf_list[x][y+1])

                sb_cls.bf_list[x][y] = '■'


                self._ship_set.append((x, y))
                sb_err._ship_element_list = self._ship_set

                self._frize_set.append((x, y))
                self._frize_set.append((x-1, y))
                self._frize_set.append((x+1, y))
                self._frize_set.append((x, y-1))
                self._frize_set.append((x, y+1))
                sb_err.ship_frize_list = self._frize_set

                sb_cls.show()
                i += 1
            else:
                print('Нельзя ставить корабли вплотную друг к другу')

# user_data = [
#     ['■', '■', '■', 'О', 'О', 'О'],
#     ['О', 'О', 'О', 'О', '■', '■'],
#     ['О', 'О', 'О', 'О', 'О', 'О'],
#     ['■', 'О', '■', 'О', '■', 'О'],
#     ['О', 'О', 'О', 'О', '■', 'О'],
#     ['■', 'О', '■', 'О', 'О', 'О']
# ]
user_data = [
    ['О', 'О', 'О', 'О', 'О', 'О'],
    ['О', 'О', 'О', 'О', 'О', 'О'],
    ['О', 'О', 'О', 'О', 'О', 'О'],
    ['О', 'О', 'О', 'О', 'О', 'О'],
    ['О', 'О', 'О', 'О', 'О', 'О'],
    ['О', 'О', 'О', 'О', 'О', 'О']
]
pick_visual = [
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
    ['О', '■', 'О', 'О', 'О', 'О'],
    ['О', 'О', 'О', '■', '■', 'О'],
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
# Использую как базу для ходов компа. Рандомно выбираем ключ. Использованное значение по ключу обнуляем и при
# повторном попадании инкрементим ключ до следующего с ненулевым value
_comp_pick = {
     1:[1, 1],  2:[1, 2],  3:[1, 3],  4:[1, 4],  5:[1, 5],  6:[1, 6],
     7:[2, 1],  8:[2, 2],  9:[2, 3], 10:[2, 4], 11:[2, 5], 12:[2, 6],
    13:[3, 1], 14:[3, 2], 15:[3, 3], 16:[3, 4], 17:[3, 5], 18:[3, 6],
    19:[4, 1], 20:[4, 2], 21:[4, 3], 22:[4, 4], 23:[4, 5], 24:[4, 6],
    25:[5, 1], 26:[5, 2], 27:[5, 3], 28:[5, 4], 29:[5, 5], 30:[5, 6],
    31:[6, 1], 32:[6, 2], 33:[6, 3], 34:[6, 4], 35:[6, 5], 36:[6, 6]
}
# список кораблей, которые пользователь будет расставлять на поле
_ship_nom = [3, 2, 2, 1, 1, 1, 1]

_ship_element_list = []
_ship_frize_list = []

try:
    _set_ship = []

    d_key = random.randint(1, 4) # выбор шаблона поля компа
    if d_key == 1:
        pick_hide = pick_hide1
    elif d_key == 2:
        pick_hide = pick_hide2
    elif d_key == 3:
        pick_hide = pick_hide3
    else:
        pick_hide = pick_hide0

    sb_cls = SeaBattle(0, 0, True, user_data, pick_visual, pick_hide)
    sb_cls.show()

    s_cls = Ship(0, 0, user_data, [], [], 0)

    # Распологаем корабли на поле
    print('Поставьте корабли на поле: 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку')
    print('Без диагональных и Г-образных')
    for ship_size in range(len(_ship_nom)):
        s_cls.ship_l = int(_ship_nom[ship_size])
        s_cls.set_ship()

    # начинаем батл =)
    print('Начнем сражение!')
    k = 0
    while sb_cls.check_win_user() and sb_cls.check_win_comp():
        sb_cls.z = k % 2 == 0
        if sb_cls.z: # определяем кто ходит (пользователю даем первый ход)
            print('Ход игрока!')
            cell_coord_list = list(input('Куда стреляем? Координаты: ').split())
        else:
            dic_key = random.randint(1, 36)
            if list(_comp_pick.get(dic_key)) == [0, 0]:
                while list(_comp_pick.get(dic_key)) == [0, 0]:
                    if dic_key >= 36:
                        dic_key = 1
                    dic_key += 1
            cell_coord_list = list(_comp_pick.get(dic_key))
            _comp_pick[dic_key] = [0, 0]
            print(f'Ход компьютера! Ячейка {cell_coord_list}')

        sb_cls.x = int(cell_coord_list[0]) - 1  # -1 из-за смещения индексов элемента массива
                                                # по отношению к системе координат нашего поля
        sb_cls.y = int(cell_coord_list[1]) - 1  # -1 из-за смещения индексов элемента массива
                                                # по отношению к системе координат нашего поля
        if sb_cls.z: # определяем на каком поле играем
            sb_cls.pick_cell_user = sb_cls.pick_ship()
        else:
            sb_cls.pick_cell_comp = sb_cls.pick_ship()
        sb_cls.show()
        k += 1

except ValueError as error:
    if sb_cls._ErrorId == 1:
        print('\nПо данной ячейке уже стреляли!!!')
    elif sb_cls._ErrorId == 2:
        print('\nОшибка выбора цели! Клетка за пределами поля!')
    else:
        print(error)
else:
    ...
    # Придумать как сюда вывести сообщение о победе. А надо ли ?
    # print('\nКод, который выполнится, если всё хорошо прошло в блоке try')
finally:
    ...
    # print('\nКод, который выполнится по любому')

