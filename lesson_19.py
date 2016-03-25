
import os


# ------------------------------------------------------

# for path in os.listdir('.'):
#     print(path, os.path.getsize(path)) # размер файла

# ------------------------------------------------------

# for path, dirs, files in os.walk('.'): # пробегаем по дереву файлов
#     print (path)

# ------------------------------------------------------

#? получить pid текущего процесса
#print(os.getpid())

# ------------------------------------------------------

# ? доступ к переменным окружения

# PATH = os.environ['PATH']
# PATH += ":" + os.path.abspath('.')
# os.environ['PATH'] = PATH
#
# print(os.environ['PATH'])
#
# PATH = os.environ['PATH']
# PATH += ":" + os.path.abspath('.')
# os.environ['PATH'] = PATH
#
# print(os.environ['PATH'])

# ------------------------------------------------------

import sys


'''

             1           2
x = [0000 0101] [0000 0001]
             2           1
y = [0000 0001] [0000 0101]

x == y = True

'''


# Big Endian
# Little Endian

# print(sys.byteorder) # 'big' или 'little'


# sys.argv - список параметров значений командной строки

# ?


# if __name__=='__main__':
#     import argparse # удобные параметры командной строки
#
#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                        help='an integer for the accumulator')
#     parser.add_argument('--hello', dest='hello', action='store',
#                        type=str, default='-')
#     parser.add_argument('--sum', dest='accumulate', action='store_const',
#                        const=sum, default=max,
#                        help='sum the integers (default: find the max)')
#
#     args = parser.parse_args()
#     print(args.accumulate(args.integers))
#
#     print(args.hello)






