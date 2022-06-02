import multiprocessing as mp

def square_list(list,square_list,square_list_sum):
    """
    square a list and sum of all elements in squarelist
    """
    # iterate through all elements in list and square them and add them to square_list
    for index,num in enumerate(list):
        square_list[index]=num*num
        square_list_sum.value=sum(square_list)
    # print square list
    print("square_list, in process:",square_list[:])
    # print square list sum
    print("square_list_sum, in process:",square_list_sum.value)
    
if __name__=="__main__":
    # create list
    list1=[1,2,3,4,5]
    # create square list array
    square_list1=mp.Array('i',len(list1))
    # create square list sum array
    square_list_sum1=mp.Value('i',0)

    # create process
    process=mp.Process(target=square_list,args=(list1,square_list1,square_list_sum1))
    # start process
    process.start()
    # wait for process to finish
    process.join()
    # print result
    print("in main:",square_list1[:])
    print("in main:",square_list_sum1.value)

