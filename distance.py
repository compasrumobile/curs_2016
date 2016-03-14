# coding: utf-8

class Distance:

    def __init__(self, meters=0, km=0):
        self.meters = meters + km * 1000

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

    def km(self):
        return self.meters / 1000


d1 = Distance(300)
d2 = Distance(600)
d3 = d1 + '700'

print(d1.meters)
print(d2.meters)
print(d3.meters)

