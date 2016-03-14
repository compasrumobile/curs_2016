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

from airplane import Airplane

from car import Car

from tank import Tank


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


print(machines[0].__dict__)

for name in Car.__dict__:
    print(name, ':', Car.__dict__[name])


print(Car.__bases__)








