'''
Merge Sort is a Divide and Conquer algorithm. 
It divides the input array into two halves, 
    calls itself for the two halves, 
    and then it merges the two sorted halves. 

The merge() function is used for merging two halves. 
The merge(arr, l, m, r) is a key process 
    that assumes that arr[l..m] and arr[m+1..r] are sorted and merges 
    the two sorted sub-arrays into one. 
'''

'''
Pseudocode :
•    Declare left variable to 0 and right variable to n-1 
•    Find mid by medium formula. mid = (left+right)/2
•    Call merge sort on (left,mid)
•    Call merge sort on (mid+1,rear)
•    Continue till left is less than right
•    Then call merge function to perform merge sort.
'''

'''
Algorithm:

step 1: start
step 2: declare array and left, right, mid variable 
step 3: perform merge function.
        mergesort(array,left,right)
        mergesort (array, left, right)
        if left > right
        return
        mid= (left+right)/2
        mergesort(array, left, mid)
        mergesort(array, mid+1, right)
        merge(array, left, mid, right)
step 4: Stop
'''

from uritemplate import variables


class MergeSort(object):
    # register and initiate
    def __init__(self,input_list):
        self.list=input_list
        print("list:",self.list,"|","length:", len(self.list))

    
    # merge  sort list
    def sort(self):
        """
        1. check if list if non-empty.
        2. find mid index.
        3. divide list into halves, left and right.
        4. call recursive functions to further divide list. come to aotmic list.
        5. start merging list.
        6. create loop till all elements are merged
        7. start from index position 0. check left and right lists' element.
        7.1. add the lowest element to the 0th index position.
        8. move to next index position, i.e. 1. follow step '7'.

        """
        list_input=self.list
        list_length=len(self.list)
        # check list is non-empty.
        if list_length>1:

            # create program to merge sort list
            mid_index=list_length//2

            # create two list, left and right.
            # left list, start to mid
            left_list=list_input[:mid_index]
            # right list, mid to end
            right_list=list_input[mid_index:]

            # recusrive functions to further divide list
            '''
            as classes used, create class instances and call sort method'''
            # left list recursive
            leftlistobject=MergeSort(left_list)
            leftlistobject.sort()
            # right list recursive
            rightlistobject=MergeSort(right_list)
            rightlistobject.sort()

            # all elements of input list are in atomic list(length=1)

            # merge atomic lists
            # define some variables
            i=j=k=0
            # i is for left variable
            # j is for right variable
            # k is the main array iteration

            # start merging
            # loop till i and j are less then left and right list
            while i<len(left_list) and j<len(right_list):
                # if left list element is small
                if left_list[i]<right_list[j]:
                    # add left list element to main list
                    list_input[k]=left_list[i]
                    # increase i
                    i+=1
                # else if right list element is small
                else:
                    # add right list element to main list
                    list_input[k]=right_list[j]
                    # increase j
                    j+=1
                # increase k
                k+=1
    # print list
    def print(self):
        print("sorted list:",self.list)




list=[5,8,7,3,1,5,9,13,52,2]
# create instace of StableSelectionSort class
sortlist=MergeSort(list)
# sort
sortlist.sort()
# print
sortlist.print()