
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

PATH = os.environ['PATH']
PATH += ":" + os.path.abspath('.')
os.environ['PATH'] = PATH

print(os.environ['PATH'])

PATH = os.environ['PATH']
PATH += ":" + os.path.abspath('.')
os.environ['PATH'] = PATH

print(os.environ['PATH'])

# ------------------------------------------------------

