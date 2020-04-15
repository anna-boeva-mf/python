# task1
import time


class TrafficLight:
    __color = 'Зеленый'

    def running(self):
        i = 1
        while True:
            if self.__color == 'Зеленый':
                print(self.__color)
                time.sleep(3)
                self.__color = 'Красный'
            elif self.__color == 'Красный':
                print(self.__color)
                time.sleep(7)
                self.__color = 'Желтый'
            else:
                print(self.__color)
                time.sleep(2)
                self.__color = 'Зеленый'
            i += 1
            if i == 7:
                break


a1 = TrafficLight()
a1.running()

# task2
class Road:
    unit_mass = 30
    unit_thick = 4

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        return self._length * self._width * self.unit_mass * self.unit_thick


b1 = Road(100, 20)
print(b1.asphalt_mass())

# task3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a1 = Position('Karl', 'Froloff', 'Director', {'wage': 1000000, 'bonus': 500000})
a2 = Position('Lara', 'Croft', 'Secretary', {'wage': 200000, 'bonus': 60000})
a3 = Position('Nik', 'Perumov', 'Manager', {'wage': 75000, 'bonus': 12000})
print(a1.get_full_name(), ':', a1.get_total_income())
print(a2.get_full_name(), ':', a2.get_total_income())
print(a3.get_full_name(), ':', a3.get_total_income())

# task4
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, directory):
        print('Машина повернула на' + directory)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(self.speed)
        else:
            print(self.speed, 'Скорость превышена!', sep='\n')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(self.speed)
        else:
            print(self.speed, 'Скорость превышена!', sep='\n')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


c1 = TownCar(20, 'red', 'C1', False)
print('TownCar', c1.color, c1.name)
c1.show_speed()
c1.stop()
c1.show_speed()
c1.speed = 12
c1.go()
c1.show_speed()
c1.speed = 72
c1.show_speed()
c2 = PoliceCar(88, 'blue', 'C2', True)
print('PoliceCar', c2.color, c2.name)
c2.show_speed()
c2.turn('лево')
c2.stop()
c2.show_speed()
c2.turn('право')
c2.speed = 44
c2.go()
c2.show_speed()
c3 = WorkCar(55, 'green', 'C3', False)
print('WorkCar', c3.color, c3.name)
c3.show_speed()

# task5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашом')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркером')


d1 = Stationery('D1')
print(d1.title)
d1.draw()
d2 = Pen('D2')
print(d2.title)
d2.draw()
d3 = Pencil('D3')
print(d3.title)
d3.draw()
d4 = Handle('D4')
print(d4.title)
d4.draw()
