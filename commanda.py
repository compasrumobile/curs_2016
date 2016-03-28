# coding: utf-8

'''
Коммандос
'''

class Operation:

    def execute(self, a, b):
        raise NotImplementedError()



class Plus(Operation):

    def execute(self, a, b):
        return a + b

class Minus(Operation):

    def execute(self, a, b):
        return a - b

class Divide(Operation):

    def execute(self, a, b):
        return a / b

class Multiply(Operation):

    def execute(self, a, b):
        return a * b


def main():
    import sys

    commands = {
        '+': Plus(),
        '-': Minus(),
        '/': Divide(),
        '*': Multiply(),
    }

    a, operation, b = sys.argv[1:]

    command = commands[operation]
    print(command.execute(a, b))

    
if __name__=='__main__':

    main()



