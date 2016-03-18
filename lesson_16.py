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
        return '{}({}): {}'.format(Tools.class_name(self), weight, self.cars)


    @staticmethod
    def trains():
        return Train._objects_count

    @classmethod
    def trains_2(cls):
        return cls._objects_count


class RedArrow(Train):

    _objects_count = 0

    def __init__(self, cars = []):

        RedArrow._objects_count += 1


class Car:

    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.weight)

    def __repr__(self):
        return self.__str__()


if __name__=='__main__':

    train = Train()

    print(train)

    train2 = Train([Car(3), Car(10), Car(5)])

    print(train2)

    ra = RedArrow()

    print(ra)


    print('__________________')


    from datetime import datetime

    class TimeString:

        # метод, не нуждающийся в объекте
        @staticmethod
        def now():
            return '{:%H:%M:%S}'.format(datetime.now())

        def now_o(self):
            return '{:%H:%M:%S}'.format(datetime.now())


    print(TimeString.now())

    print(TimeString().now_o())

