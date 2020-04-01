# task1
a = 10
b = 20
my_str = 'String is mine'
my_str1 = '!!!'
your_str = input('Введите строку: ')
your_int = int(input('Введите целое число: '))
your_float = float(input('Введите дробное число: '))
print('Вывод: ')
print(a, a + b, my_str + my_str1, your_str, your_int, "%.2f" % your_float, sep='\n')

# task2
seconds = int(input('Введите количество секунд: '))
parts = [('0' + str(seconds//60//60))[-2:], ('0' + str(seconds//60 % 60))[-2:], ('0' + str(seconds % 60))[-2:]]
print(f"Время: {':'.join(parts)}")

# task3
n = int(input('Введите число: '))
print('Результат: ', n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

# task4
n = int(input('Введите целое положительное число: '))
max_d = 1
while n > 0 and max_d < 9:
    if n % 10 > max_d:
        max_d = n % 10
    n //= 10
print('Максимальная цифра числа: %d' % max_d)

# task5
rev = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек: '))
if cost > rev:
    print('Фирма отработала с убытком: ')
elif cost == rev:
    print('Фирма отработала в ноль: ')
else:
    print("Фирма отработала с прибылью. Рентабельность прибыли составляет %.2f %%" % ((rev - cost)/rev * 100))
    col = int(input('Введите количество сотрудников Вашей фирмы: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ',  (rev - cost)/col)

# task6
a = float(input('Введите результат первого дня: '))
b = float(input('Задайте цель: '))
i = 1
while a < b:
    a *= 1.1
    i += 1
print('На %d день будет достигнута цель' % i)
