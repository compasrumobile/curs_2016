
NAME = 'vfdvfd'

class Worker:
    price_for_1_month = 10000

    def make_remont(self):
        print("Worker works hard 1 month")
        return self.price_for_1_month


class Prorab(Worker):
    price_for_1_month = 30000

    def __init__(self, *workers):
        self.workers = workers

    def make_remont(self):
        print("Prorab plans work for 1 month")

        sum_p = 0
        for w in self.workers:
            sum_p += w.make_remont()

        return self.price_for_1_month + sum_p


p = Prorab(

    Worker(),
    Worker(),
    Worker(),

)
price = p.make_remont()

print("remont price:", price)
