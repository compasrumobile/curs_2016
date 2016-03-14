# coding: utf-8
# -*- coding: utf-8 -*-

# Пример класса Точка:
'''class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Пример самого простейшего класса
class Polygon:

    def __init__(self, *points):
        self.points = points

    def find_top_point(self):
        upper = None
        for p in self.points:
            if not upper or p.y > upper.y:
                upper = p
        return upper

    def show_points(self):
        print('-'*20)
        for p in self.points:
            print(p.x, p.y)

# И тогда мы можем создавать полигоны точек:
polygon = Polygon(
    Point(10, 12), 
    Point(30, 12), 
    Point(10, 30)
)
polygon.show_points()


p = polygon.find_top_point()
print(p.y)'''



import random

class Transport:

    index = 0

    def __init__(self, speed = 0, wheel_count = 0, mass = 0, color = (0, 0, 0)):
        self.index = Transport.index = Transport.index + 1
        self.speed = speed
        self.wheel_count = wheel_count
        self.mass = mass
        self.color = color
        self.pos = 0

    def drive(self, time):
        self.pos += self.speed * time

    def show_pos(self):
        print(self, ':', self.pos)

    def crash(self, o):
        print(u'Столкнулись:', self.index, u'и', o.name)
        self.pos = 0
        o.pos = 0

    def fire(self, o):
        pass

    # для вывода на экран в консоль объекта самого
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.index)

    # для вывода на экран (как пример) в составе списка
    def __repr__(self):
        return 'R:'+self.__str__()


class Car(Transport):

    def __init__(self):
        super().__init__(speed = 120, wheel_count = 4, mass = 2, color = (0, 255, 0))


class Tank(Transport):

    def __init__(self):
        super(Tank, self).__init__(speed = 90, wheel_count = 18, mass = 20, color = (150, 155, 30))

        self.can_fire = True

    def fire(self, o):
        o.pos = 0
        print(self, 'killed:', o)

    def crash(self, o):
        print(u'Столкнулись:', self.index, u'и', o.name)
        o.pos = 0


class Airplane(Transport):

    def __init__(self):
        super().__init__(speed = 800, wheel_count = 22, mass = 100,
            color = (250, 250, 250))

        self.wings_count = 2
        self.tail = True



machines = [
    Car(),
    Car(),
    Car(),
    Tank(),
    Airplane(),
    Airplane(),
]


for m in machines:
    m.show_pos()


for m in machines:
    time = random.randint(1, 150)
    m.drive(time)

for m in machines:
    m.fire(random.choice(machines))


print('-'*20)

for m in machines:
    m.show_pos()

print('-'*20)

print(machines)









