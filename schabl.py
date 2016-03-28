from abc import ABCMeta, abstractmethod

'''
Интерфейс
'''
class StudentInterface:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self):
        #raise NotImplementedError()
        pass

    @abstractmethod
    def get_age(self):
        #raise NotImplementedError()
        pass


'''
ios
'''
class IosStudent(StudentInterface):

    def get_name(self):
        return '{} [ios]'.format(self.name)

    def get_age(self):
        return '{} [ios]'.format(self.age)


'''
android
'''
class AndroidStudent(StudentInterface):

    def get_name(self):
        return '{} [android]'.format(self.name)

    def get_age(self):
        return '{} [android]'.format(self.age)



def get_student():
    '''
    Определяет систему и выдает соответветствующий объект класса

    Фабричный метод.

    :return: StudentInterface
    '''
    import sys

    if sys.platform == 'ios':
        return IosStudent()
    elif sys.platform == 'android':
        return AndroidStudent()

    return StudentInterface()



def calc_middle_age(lst):
    """
    Считает средний возраст студентов.
    :param lst: [StudentInterface, StudentInterface, ...]
    :return: средний возраст
    """
    return 0


if __name__=='__main__':


    student_1 = get_student()
    student_2 = get_student()


    ret = calc_middle_age([student_1, student_2])