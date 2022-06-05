import threading as t
import os

def task1():
    print("Task1 assigned to thread:",t.current_thread().name)
    print("Task1 process ID:", os.getpid())

def task2():
    print("Task2 assigned to thread:",t.current_thread().name)
    print("Task2 process ID:", os.getpid())

if __name__=="__main__":

    # Id of current process
    print("ID of process running main program:", os.getpid())
    # name of main thread
    print("Name of main thread:", t.current_thread().name)

    # create threads
    t1 = t.Thread(target=task1)
    t2 = t.Thread(target=task2)

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish
    t1.join()
    t2.join()

    print("Main process exiting")
