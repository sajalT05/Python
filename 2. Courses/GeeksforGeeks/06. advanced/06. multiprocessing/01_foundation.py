import multiprocessing

# create functions
# cube
def cube(num):
    print("cube:",num*num*num)
# square
def square(num):
    print("square:",num*num)

if __name__ == '__main__':
    # create process
    # process=multiprocessing.Process(target=functionName,args=("arguments",))
    process1=multiprocessing.Process(target=cube,args=(100,))
    process2=multiprocessing.Process(target=square,args=(100,))

    # start process
    process1.start()
    process2.start()

    # wait for process to finish
    process1.join()
    process2.join()

    # print result
    print("Done!")
    
