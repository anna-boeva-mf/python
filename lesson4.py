# task1
"""
Скрипт salary.py получает на вход 3 параметра: выработка, ставка, премия.
   py salary.py 10 1000 500
"""

# task2
my_str = input('Введите числа через пробел: ')
my_list = my_str.split()
new_list = [int(my_list[i]) for i in range(1, len(my_list)) if int(my_list[i]) > int(my_list[i - 1])]
print('Новый список:', new_list)

# task3
my_list = [i for i in range(20, 240 + 1) if i % 20 == 0 or i % 21 == 0]
print('Числа от 20 до 240, кратные 20 или 21:', my_list, sep='\n')

# task4
my_str = input('Введите числа через пробел: ')
my_list = my_str.split()
new_list = [int(l) for l in my_list if my_list.count(l) == 1]
print('Новый список:', new_list)

# task5
from functools import reduce


def my_prod(a, b):
    return a*b


my_list = [i for i in range(100, 1000 + 1, 2)]
print('Произведение всех четных чисел от 100 до 1000:', reduce(my_prod, my_list))

# task6
"""
Скрипт task_6_a.py принимает два целых числа - начало и конец числового отрезка. Выводит целые числа в этом диапазоне.
   py task_6_a.py 17 22

Скрипт task_6_b.py получает на вход список элементов, разделенных запятыми, и количество выводов элементов по циклу. 
   py task_6_b.py 1,a,2,b,3 12
"""

# task7
def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
        yield s


n = int(input('Ведите целое положительное число: '))
for j in fact(n):
    print(j)
