# coding: utf-8
from threading import Thread
import os
import time


def run(index):
    '''
    функция будет выполняться в потоке
    '''
    print(u'Работаю в потоке', index)
    filenames = os.listdir('.')

    size = 0
    for fi in filenames:
        size += os.path.getsize(fi)
        time.sleep(1)
        print(index, ': size:', size)

    print(index, ':', size)

# ссылку на метод в target
thread1 = Thread(target=run, args=(1,))
thread2 = Thread(target=run, args=(2,))
thread3 = Thread(target=run, args=(3,))
thread4 = Thread(target=run, args=(4,))

# запуск потока
thread1.start()
thread2.start()
thread3.start()
thread4.start()

