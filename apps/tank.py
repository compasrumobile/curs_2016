from transport import Transport

__author__ = 'andrew'


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