from sys import argv

script_name, productivity, rate, premium = argv
try:
    a1 = float(productivity)
    a2 = float(rate)
    a3 = float(premium)
except ValueError:
    print('Некоррекный ввод данных')
else:
    print('Выработка в часах:', productivity)
    print('Ставка в час (руб.):', rate)
    print('Премия (руб.):', premium)
    print(f"Зарплата сотрудника составляет {a1*a2 + a3} руб.")
