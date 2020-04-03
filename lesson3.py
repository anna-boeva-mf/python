# task1
def division(div1, div2):
    if div2 == 0:
        print('Делитель не может равняться нулю')
    else:
        print('Частное чисел:', div1 / div2)


d1 = float(input('Введите делимое: '))
d2 = float(input('Введите делитель: '))
division(d1, d2)

# task2
def person_data(name, surname, birth_year, city, p_email = '', phone = ''):
    print(f"{name} {surname}, {birth_year} г.р., проживающий в г. {city}. Телефон: {phone}, email: {p_email}")


n = input('Имя: ')
s = input('Фамилия: ')
y = input('Год рождения: ')
c = input('Город проживания: ')
e = input('Введите контактный телефон: ')
p = input('Введите адрес электронной почты: ')
person_data(name=n, surname=s, birth_year=y, city=c, phone=e, p_email=p)

# task3
def my_func(v1, v2, v3):
    if v1 < v2 and v1 < v3:
        return v2 + v3
    elif v2 < v3:
        return v1 + v3
    else:
        return v1 + v2


print('Введите три числа: ')
x1 = float(input())
x2 = float(input())
x3 = float(input())
print('Сумма двух наибольших чисел равна', my_func(x1, x2, x3))

# task4
def my_func1(x, y):
    k = x
    for i in range(1, -y):
        k *= x
    return 1/k


def my_func2(x, y):
    k = x**(-y)
    return 1/k


x1 = float(input('Введите действительное положительное число: '))
y1 = int(input('Введите целое отрицательное число : '))
print('Результат возведения в степень:', my_func1(x1, y1))
print('Тот же результат: ', my_func2(x1, y1))

# task5
def part_sum(s):
    current_sum = 0
    ch = s.split()
    for i in ch:
        current_sum += float(i)
    return current_sum


def f_sum():
    final_sum = 0
    while True:
        k = input()
        if k[len(k) - 1].upper() == 'Q':
            final_sum += part_sum(k[:len(k) - 2])
            print('Конечная сумма:', final_sum)
            break
        else:
            final_sum += part_sum(k)
            print('Текущая сумма:', final_sum)


print('Введите числа через пробел. Для вывода суммы нажмите Enter. Для окончания ввода нажмите Q')
f_sum()

# task6
def int_func(s):
    return s.capitalize()


def final_int_func(s):
    se = []
    for i in s.split():
        se.append(int_func(i))
    return ' '.join(se)


print('Введите строку: ')
sf = input()
print('Результат: ', final_int_func(sf), sep='\n')
