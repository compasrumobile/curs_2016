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
        weight = sum([car.weight for car in self.cars])
        return '{}({}/{}): {}'.format(Tools.class_name(self),
                                      self.trains_2(), weight, self.cars)


    @staticmethod
    def trains():
        return Train._objects_count

    @classmethod
    def trains_2(cls):
        return cls._objects_count


class RedArrow(Train):

    _objects_count = 0

    def __init__(self, cars = []):
        super().__init__(cars)

        RedArrow._objects_count += 1


#RedArrow.trains_2()


class Car:

    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.weight)

    def __repr__(self):
        return self.__str__()


if __name__=='__main__':

    train = Train()

    train2 = Train([Car(3), Car(10), Car(5)])

    ra = RedArrow()


    print(train)

    print(train2)

    print(ra)



