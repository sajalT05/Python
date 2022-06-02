import multiprocessing
import os

# create functions
# get id
# function1
def function1():
    print("function1:",os.getpid())
# function2
def function2():
    print("function2:",os.getpid())

if __name__=="__main__":
    print("main:",os.getpid())

    # create process
    process1=multiprocessing.Process(target=function1)
    process2=multiprocessing.Process(target=function2)

    # start process
    process1.start()
    process2.start()

    # id of running process
    print("process1 id:",process1.pid)
    print("process2 id:",process2.pid)

    # wait for process to finish
    process1.join()
    process2.join()

    # print result
    print("Done!")

    # check process is alive
    print("process1 is alive:",process1.is_alive())
    print("process2 is alive:",process2.is_alive())
    
