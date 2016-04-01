# coding: utf-8
import concurrent.futures
from threading import Thread
from multiprocessing import Pool
import multiprocessing
#from multiprocessing.dummy import Pool

import threading
import os
import time


def run(filename):
    '''
    функция будет выполняться в потоке
    '''
    size = 0
    for a in range(1000):
        #print(u'Работаю в процессе', multiprocessing.current_process())
        size += os.path.getsize(filename)
    return size


#with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
# with Pool(processes=5) as executor:
#     s = sum( [ a for a in executor.map(run, os.listdir('.')) ] )
#     print(s)

print( sum( [run(a) for a in os.listdir('.')] ) )
