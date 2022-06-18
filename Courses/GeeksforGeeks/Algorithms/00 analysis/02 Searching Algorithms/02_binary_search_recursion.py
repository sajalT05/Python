'''
Binary Search Algorithm: The basic steps to perform Binary Search are:
    Begin with the mid element of the whole array as a search key.
    If the value of the search key is equal to the item then return an 
        index of the search key.
    Or if the value of the search key is less than the item in the 
        middle of the interval, narrow the interval to the lower half.
    Otherwise, narrow it to the upper half.
    Repeatedly check from the second point until the value is found 
        or the interval is empty.

Binary Search Algorithm can be implemented in the following two ways
    Iterative Method
    Recursive Method

Step-by-step Binary Search Algorithm: We basically ignore half of the elements just after one comparison.

    Compare x with the middle element.
    If x matches with the middle element, we return the mid index.
    Else If x is greater than the mid element, 
        then x can only lie in the right half subarray after the mid element. 
        So we recur for the right half.
    Else (x is smaller) recur for the left half.
'''

from jmespath import search


class BinarySearch:
    # initiate datatype registerations
    def __init__(self,datatype):
        self.dt=datatype
    # search value
    def search(self,value):
        self.value=value

        # datataypes
        if(type(self.dt)==list):
            print("list datatype:",self.dt)
            # check if list if not empty
            if (len(self.dt)>0):
                # create search function
                def list_binary_search_recursion(start=0,end=len(self.dt)-1):
                    # mid index position --> left to mid value
                    mid=(start+end)//2
                    # check middle value
                    if self.dt[mid]==self.value:
                        print(f"element '{self.value}' found at '{mid+1}' position")
                    #  value greater than middle position value
                    elif self.value>self.dt[mid]:
                        return list_binary_search_recursion(start=mid+1,end=len(self.dt)-1)
                    # value less than middle position value
                    elif self.value<self.dt[mid]:
                        return list_binary_search_recursion(start=0,end=mid-1)
                    else:
                        print("NOT FOUND")
   
            else:
                print("empty string")
            return list_binary_search_recursion() 
                
            
            

# datatypes
list_datatype=[1,2,5,9,15,23,45,95,135]

# instances
list_binary_search=BinarySearch(list_datatype)
list_binary_search.search(44)