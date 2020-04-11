# task1
print('Введите строки. По окончании ввода оставьте пустую строку\n')
str_file = []
while True:
    s = input()
    if s == '':
        break
    str_file.append(s)
with open('file_task1.txt', 'w') as f:
    f.write('\n'.join(str_file))

# task2
with open('file_task2.txt') as f:
    s = f.readlines()
    print(f"Файл {f.name} содержит {len(s)} строк. Количество слов в каждой строке:")
    for i in range(len(s)):
        s[i] = s[i].replace('\n', '')
        if s[i].count('-') > 0:
            my_s = s[i].split('-')
            s[i] = ' '.join(my_s)
        if len(s[i]) == 0:
            print(f"{i + 1}: {0}")
        else:
            my_s = s[i].split()
            print(f"{i + 1}: {len(my_s)}")

# task3
with open('file_task3.txt') as f:
    s = f.readlines()
    all_sum = 0
    print('Сотрудники с окладом меньше 20 тыс:')
    for i in range(s.__len__()):
        s[i] = s[i].strip()
        info = s[i].split()
        all_sum += float(info[1])
        if float(info[1]) < 20000:
            print(info[0])
    print('Средняя величина дохода сотрудников:', '%.2f' %(all_sum/s.__len__()))

# task4
with open('file_task4_1.txt', 'w') as f_target:
    my_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 15: 'Пятнадцать'}
    with open('file_task4.txt') as f_source:
        for line in f_source:
            # Если вдруг появятся не однозначные числа:
            n = int(line[len(line.replace('\n', '')) - (line.replace('\n', '')[::-1].find(' ')): len(line.replace('\n', ''))])
            f_target.write(line.replace(line[:line.find(' ')], my_dict.get(n)))

# task5
from random import uniform


n = 15
with open('file_task5.txt', 'w') as f:
    f.write(str('%.2f' % uniform(1, 100)))
    for i in range(n - 1):
        f.write(' ' + str('%.2f' % uniform(1, 100)))

with open('file_task5.txt') as f:
    s = f.read()
    total_sum = 0
    numbers = s.split()
    for i in range(len(numbers)):
        total_sum += float(numbers[i])
    print(total_sum)

# task6
less_dict = {}
with open('file_task6.txt') as f:
    for line in f:
        line.strip()
        lesson_name = line[:line.find(':')]
        lesson = line[line.find(':'):].split()
        duration = 0
        for j in range(1, len(lesson)):
            if lesson[j].find('(') > 0:
                duration += int(lesson[j][:lesson[j].find('(')])
        less_dict.update({lesson_name: duration})
print(less_dict)

# task7
import json


firms = {}
profit = {}
average_profit = 0
n = 0
with open('file_task7.txt') as f:
    for line in f:
        line.strip()
        one_firm = line.split()
        p = float(one_firm[2]) - float(one_firm[3])
        if p > 0:
            average_profit += p
            n += 1
        firms.update({one_firm[0]: p})
    profit.update({'average_profit': round(average_profit/n, 2)}) if n > 0 else profit.update({'average_profit': 0})
final_obj = [firms, profit]

with open('task7.json', 'w') as js:
    json.dump(final_obj, js)
