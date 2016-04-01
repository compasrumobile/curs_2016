from multiprocessing import Process

from multiprocessing import Lock, current_process

def write(filename, word, lock):
    #lock.acquire() # закрываем замок

    with lock:

        print("lalala", current_process())

        # критическая
        with open(filename, 'w') as f:
            f.write("{}\n".format(word) * 100000)


        #lock.release() # открываем замок


if __name__=='__main__':

    FILENAME = 'ttt_20.txt'

    lock = Lock()

    p1 = Process(target=write, args=(FILENAME, 'hello', lock))
    p1.start()

    p2 = Process(target=write, args=(FILENAME, 'buy', lock))
    p2.start()
