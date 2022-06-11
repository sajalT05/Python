import multiprocessing as mp

def square_list(list,q):
    """
    square a list
    """
    for num in list:
        # append squares to queue
        q.put(num*num)

def print_queue(q):
    """
    print queue
    """
    while not q.empty():
        # get squares from queue
        print(q.get())
    print("Queue is now empty!")

if __name__=="__main__":
    # input list
    list1=[1,2,3,4,5]
    # create queue
    q=mp.Queue()
    # create process
    process1=mp.Process(target=square_list,args=(list1,q))
    process2=mp.Process(target=print_queue,args=(q,))

    # running processes1 to get square list
    process1.start()
    process1.join()

    # running processes2 to print queue
    process2.start()
    process2.join()

    # print result
    

