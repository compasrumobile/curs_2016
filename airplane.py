from transport import Transport

__author__ = 'andrew'


class Airplane(Transport):

    def __init__(self):
        super().__init__(speed = 800, wheel_count = 22, mass = 100,
            color = (250, 250, 250))

        self.wings_count = 2
        self.tail = True