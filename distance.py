# coding: utf-8


def show(func):

    def new_func(self, b):
        print(self.__class__.__name__, func.__name__, self, b)
        return func(self, b)

    return new_func


class Distance:

    def __init__(self, meters=0, km=0):
        self.meters = meters + km * 1000

    def __str__(self):
        return str(self.meters)

    def __add__(self, b):
        if type(b) is Distance:
            sum_meters = self.meters + b.meters
        elif type(b) is int:
            sum_meters = self.meters + b
        elif type(b) is str:
            sum_meters = self.meters + int(b)
        else:
            raise TypeError(u'Нельзя так...')
        return Distance(sum_meters)

    def __radd__(self, other):
        return self.__add__(other)

    @show
    def __truediv__(self, b):
        if type(b) is Distance:
            sum_meters = self.meters / b.meters
        elif type(b) is int:
            sum_meters = self.meters / b
        elif type(b) is float:
            sum_meters = self.meters / b
        elif type(b) is str:
            sum_meters = self.meters / int(b)
        else:
            raise TypeError(u'Нельзя так...')
        return Distance(sum_meters)

    @show
    def __rtruediv__(self, b):
        return Distance(b.__truediv__(self.meters))


    def km(self):
        return self.meters / 1000


d1 = Distance(300)
d2 = Distance(600)
d3 = Distance(100)

d4 = 100 / d1 / d2

print(d1.meters)
print(d2.meters)
print(d4.meters)

