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

class BinarySearch:
    # initiate datatype registerations
    def __init__(self,datatype):
        self.dt=datatype
    # search value
    def search(self,value):
        self.v=value

        # datataypes
        if(type(self.dt)==list):
            print("list datatype:",self.dt)
            length=len(self.dt)
            data_list=self.dt
            value=self.v
            start=0
            end=length-1
            while(start<=end):
                # middle element
                mid=(start+end)//2
                # find element at middle
                if (data_list[mid]==value):
                    print(f"element '{value}' found at '{mid+1}' position")
                    break
                # if value is more than mid value
                if (value<data_list[mid]):
                    end=mid-1
                # if value if less than mid value
                if (value>data_list[mid]):
                    start=mid+1




                            

# datatypes
list_datatype=[1,2,5,9,23,59]

# instances
list_binary_search=BinarySearch(list_datatype)
list_binary_search.search(9)