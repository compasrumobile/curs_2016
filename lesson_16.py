# coding: utf-8

class Tools:

    def class_name(self):
        return self.__class__.__name__


class Train:

    _objects_count = 0


    def __init__(self, cars = []):
        Train._objects_count += 1

        self.cars = cars

        print('---', self.trains())

    def __str__(self):
        return '{}({}/{}): {}'.format(Tools.class_name(self),
                                      self.trains_2(), self.weight, self.cars)


    @staticmethod
    def trains():
        return Train._objects_count

    @classmethod
    def trains_2(cls):
        return cls._objects_count



    @property
    def weight(self):
        return sum([car.weight for car in self.cars])



class RedArrow(Train):

    _objects_count = 0

    def __init__(self, cars = []):
        super().__init__(cars)

        RedArrow._objects_count += 1


#RedArrow.trains_2()


class Car:

    def __init__(self, weight, number):
        self.weight = weight
        self.__number = number

    def __str__(self):
        return '{}({}): {}'.format(self.__class__.__name__, self.number, self.weight)

    def __repr__(self):
        return self.__str__()


    @property
    def number(self):
        print('??????')
        return self.__number

    @number.setter
    def number(self, value):
        print('!!!!!!!')
        #self.__number = value / 2

    @number.deleter
    def number(self):
        print('XXXXXXX')
        self.__number = 0
        #del self.__number


if __name__=='__main__':

    train = Train()

    train2 = Train([Car(3, 1), Car(10, 5), Car(5, 3)])

    ra = RedArrow()


    print(train)

    print(train2)

    print(ra)

    print( train2.cars[2].number )

    train2.cars[2].number = 300

    print(train2)

    del train2.cars[2].number


    print(train2)



