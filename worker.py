# coding: utf-8
from datetime import datetime


def sekretnost(func):

    def new_func(*args):
        return func(*args) * 1.1

    return new_func



class Worker:
    zp = 20000

    def premia(self):
        if datetime.now().month == 11:
            return self.zp
        return 0

    @sekretnost
    def money(self):
        return self.zp + self.premia()



class Saler(Worker):
    zp = 15000
    procent = 10
    prodaz = 0

    def make_prodaz(self, sum_prodaz):
        self.prodaz = sum_prodaz


    def money(self):
        return super(Saler, self).money() + self.prodaz * self.procent / 100  # ТАК ПРАВИЛЬНО


w = Worker()
s = Saler()
s.make_prodaz(100000)
workers = [w, s]

for w in workers:
    print(w.__class__.__name__ + ":", w.money())