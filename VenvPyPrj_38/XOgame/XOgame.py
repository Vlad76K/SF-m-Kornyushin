data = [
   [0, ' ', ' ', ' '],
   [1, ' ', ' ', ' '],
   [2, ' ', ' ', ' ']
]
def PrintTbl(d, flg=False):
    if flg:
        print('\n' * 20) # надо как-то избавляться от старых записей в консоли
    print('   0  1  2')
    print('{}  {}  {}  {}'.format(*d[0]))
    print('{}  {}  {}  {}'.format(*d[1]))
    print('{}  {}  {}  {}'.format(*d[2]))

# Останавливаем игру, если все ячейки заполнены
def StopGame(d):
    for i in range(1, len(d)):
        for j in range(3):
            if d[i][j] == ' ':
                return False
        # print(any(x for x in d[i]),' - ',d[i])
        # print(all(x for x in d[i]), ' - ', d[i])
    return True

# Проверки на победу
def checkWin(d):
    # проверим строки на "три одинаковых в ряд"
    for i in range(3):
        if d[i][1] == ' ' or d[i][2] == ' ' or d[i][3] == ' ':  # пустые не смотрим
            ...
        else:
            if d[i][1] == d[i][2] == d[i][3]:
                print(f'Строка {i} содержит одинаковые символы. Победа!')
                return True

    # проверим столбцы на "три одинаковых в ряд"
    for i in range(1, 4):
        if d[0][i] == ' ' or d[1][i] == ' ' or d[2][i] == ' ':  # пустые не смотрим
            ...
        else:
            if d[0][i] == d[1][i] == d[2][i]:
                print('Столбец 1 содержит одинаковые символы. Победа!')
                return True

    # надо проверить диагонали
    if d[0][1] != ' ' and (d[0][1] == d[1][2] == d[2][3]):
        print('Диогональ содержит одинаковые символы. Победа!')
        return True
    if d[0][3] != ' ' and (d[0][3] == d[1][2] == d[2][1]):
        print('Диогональ содержит одинаковые символы. Победа!')
        return True

    return False

PrintTbl(data, True) # первоначальный вывод "сетки"

EmptyCell = True
step = 0
while not checkWin(data):
    if step > 10: break

    inputStr = input('Введите пару чисел через пробел (строка столбец) и значение (X / O): ') #1 1 X

    if inputStr == 'Q': break # для досрочного завершения игры

    L = list(inputStr.split()) # обработка введенного с клавиатуры значения

    if data[int(L[0])][int(L[1])+1] == ' ': # проверим не пытаются ли перезаписать значение
        data[int(L[0])][int(L[1])+1] = L[2]
    else:
        EmptyCell = False
        print('Данная клетка уже заполнена. Выберите другую')

    if StopGame(data): # если все ячейки уже заполнены
        break

    if EmptyCell: # исключаем вывод в консоль для случая перезаписи данных
        PrintTbl(data, True)

    EmptyCell = True
    step += 1 # счетчик делал для отладки

