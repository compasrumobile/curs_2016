
from multiprocessing import Queue
from multiprocessing import Process, current_process


def write(filename, word, q):

    if word == 'hello':
        while True:
            print( "put:", current_process() )
            q.put("hello")
    else:
        while True:
            print( q.get(), current_process() )


'''
Возможности асинхронности в python 3.5

async def some_async_func():

    while True:
        now = await sleep(timeout)
        print("Hello, {}!\tts: {}".format(name, now))

'''


if __name__=='__main__':

    FILENAME = 'ttt_20.txt'

    q = Queue()


    p1 = Process(target=write, args=(FILENAME, 'hello', q))
    p1.start()

    p2 = Process(target=write, args=(FILENAME, 'buy', q))
    p2.start()


