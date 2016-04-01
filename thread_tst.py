# coding: utf-8
import concurrent.futures
from threading import Thread
from multiprocessing import Pool
from multiprocessing.dummy import Pool

import threading
import os
import time


def run(filename):
    '''
    функция будет выполняться в потоке
    '''
    size = 0
    for a in range(1000):
        #print(u'Работаю в потоке', threading.current_thread())
        size += os.path.getsize(filename)
    return size


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    s = sum( [ a for a in executor.map(run, os.listdir('.')) ] )
    print(s)







# # ссылку на метод в target
# thread1 = Thread(target=run, args=(1,))
# thread2 = Thread(target=run, args=(2,))
# thread3 = Thread(target=run, args=(3,))
# thread4 = Thread(target=run, args=(4,))
#
# # запуск потока
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
#
# thread2.join() # присоединяет поток
#
# print(100)

'''
threads:
real	0m2.489s
user	0m1.744s
sys	0m1.460s


processes:
real	0m0.602s
user	0m0.768s
sys	0m0.278s


1 thread:
real	0m0.609s
user	0m0.465s
sys	0m0.122s
'''





