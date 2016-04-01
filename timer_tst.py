__author__ = 'andrew'
from threading import Timer
import time


def hello():
    print("hello, world")


t = Timer(3.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed

time.sleep(1)
print('main thread')

time.sleep(4)
print('main thread 2')
