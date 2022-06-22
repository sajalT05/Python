import multiprocessing

# create empty list
result=[]

def square_list(list):
    """
    square a list
    """
    # get global list
    global result

    # square list function
    for i in list:
        result.append(i*i)
    print("in process:",result)

list1=[1,2,3,4,5]

if __name__=="__main__":
    # create process
    process=multiprocessing.Process(target=square_list,args=(list1,))
    # start process
    process.start()
    # wait for process to finish
    process.join()
    # print result
    print("in main:",result)

