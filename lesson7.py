# task1
class Matrix:
    def __init__(self, arrays):
        self.m = len(arrays)
        self.n = len(arrays[0])
        self.mat_strings = []
        for i in range(self.m):
            self.mat_strings.append(arrays[i])

    def __str__(self):
        str_m = []
        for i in range(self.m):
            str_m.append(''.join([str(g).rjust(5, ' ') for g in self.mat_strings[i]]))
        return '\n'.join(str_m)

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            return 'Размерности матриц не совпадают'
        sum_mat_strings = []
        for l1, l2 in zip(self.mat_strings, other.mat_strings):
            s = []
            for k1, k2 in zip(l1, l2):
                s.append(k1 + k2)
            sum_mat_strings.append(s)
        return Matrix(sum_mat_strings)


c1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7], [35, 36, 37]])
print(f"Матрица размера {c1.m}x{c1.n}:", c1, sep='\n')
c2 = Matrix([[10, 20, 30], [30, 40, 50], [50, 60, 70], [350, 360, 370]])
print(f"Матрица размера {c2.m}x{c2.n}:", c2, sep='\n')
print('Сумма матриц:', c1 + c2, sep='\n')

# task2
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name, param):
        self.name = name
        self.param = param
        self.ww = []

    @abstractmethod
    def product_square(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.param = v

    def product_square(self):
        return round(float(self.param) / 6.5 + 0.5, 4)


class Suit(Clothes):
    def __init(self, name, h):
        self.name = name
        self.param = h

    def product_square(self):
        return round(2 * float(self.param) + 0.3, 4)


class Orders:
    def __init__(self):
        self.ww = []
        self.k = 0

    def add_order(self, t):
        self.ww.append(t.product_square())
        self.k += 1

    @property
    def common_square(self):
        square = 0
        for i in self.ww:
            square += i
        return round(square, 4)


o = Orders()
s1 = Suit('S1', 1)
print(s1.product_square())
o.add_order(s1)
print('Количество заказов:', o.k, 'Общий расход ткани:', o.common_square)
c1 = Coat('C1', 2)
print(c1.product_square())
o.add_order(c1)
print('Количество заказов:', o.k, 'Общий расход ткани:', o.common_square)
o.add_order(Suit('S2', 3))
o.add_order(Suit('S3', 4))
o.add_order(Coat('C2', 5))
print('Количество заказов:', o.k, 'Общий расход ткани:', o.common_square)

# task3
class Cell:
    def __init__(self, t):
        self.t = t

    def __add__(self, other):
        return Cell(self.t + other.t)

    def __sub__(self, other):
        if self.t - other.t > 0:
            return Cell(self.t - other.t)
        else:
            print('Вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.t * other.t)

    def __truediv__(self, other):
        if self.t / other.t > 1:
            return Cell(self.t // other.t)
        else:
            print('Деление невозможно')

    def make_order(self, j):
        if self.t // j > 0:
            if self.t % j == 0:
                return '\\n'.join('*' * j for i in range(self.t // j))
            else:
                return '\\n'.join('*' * j for i in range(self.t // j)) + '\\n' + '*' * (self.t % j)
        else:
            return '*' * (self.t % j)


c = Cell(15)
print('Количество ячеек:', c.t, '\n', 'Клетка:', c.make_order(6))
s1 = Cell(18)
s2 = Cell(3)
s3 = s1 * s2
print('Количество ячеек:', s3.t, '\n', 'Клетка:', s3.make_order(17))
s4 = s2 - s1
s5 = s1 / s2
print('Количество ячеек:', s5.t, '\n', 'Клетка:', s5.make_order(7))
