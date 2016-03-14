from transport import Transport

__author__ = 'andrew'

class Own:

    def __init__(self, owner):
        self.owner = owner


class Car(Transport, Own):
    '''
    Car - Transport with 4 wheels
    '''

    def __init__(self, owner=None):


        # позволяет достучаться до методов родителя
        super().__init__(speed = 120, wheel_count = 4, mass = 2, color = (0, 255, 0))
        Own.__init__(self, owner)