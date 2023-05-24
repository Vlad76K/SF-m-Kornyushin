# должен содержать число Пи в виде константы 3.14, и две функции, которые будут считать площадь круга и прямоугольника.
from math import pi as PI

MAIN_CONSTANT = round(PI, 2)

def square_rectangle(side1, side2):
    return side1 * side2
def square_circle(radius):
    return MAIN_CONSTANT * radius**2


if __name__ == '__main__':
    print(MAIN_CONSTANT)  # 3.14
    print(round(PI, 2))  # 3.14

