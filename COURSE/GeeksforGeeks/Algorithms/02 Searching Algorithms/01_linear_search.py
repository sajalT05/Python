'''
A simple approach is to do a linear search, i.e  
    Start from the leftmost element of arr[] and one by one compare 
          x with each element of arr[]
    If x matches with an element, return the index.
    If x doesn’t match with any of elements, return -1.

Improve Linear Search Worst-Case Complexity
    if element Found at last  O(n) to O(1)
    It is the same as previous method because here we are performing 
        2 ‘if’ operations in one iteration of the loop and in previous 
        method we performed only 1 ‘if’ operation. This makes both the time complexities same.
'''

class LinearSearch:
    # initiaite to register data
    def __init__(self,datatype):
        self.dt=datatype
    # find value in specific datatype
    def search(self, value):
        '''
        1. find datatype.
        2. search for element in beginning and end.
        3. traversal search for element.
        '''
        self.value=value

        # find elements in datatypes

        # list
        if type(self.dt)==list:
            print("list datatype:", self.dt)
            left_element=self.dt[0]
            right_element=self.dt[-1]
            length_list=len(self.dt)
            if (left_element==self.value):
                print("element found in beginnning:",left_element)
            elif (right_element==self.value):
                print("element found at the end:", right_element)
            else:
                for i in range(len(self.dt)):
                    if (self.dt[i]==self.value):
                        print(f"element '{self.value}' found in list at '{i+1}' position")
        # tuple
        elif type(self.dt)==tuple:
            print("tuple datatype:", self.dt)
            left_element=self.dt[0]
            right_element=self.dt[-1]
            length_list=len(self.dt)
            if (left_element==self.value):
                print("element found in beginnning:",left_element)
            elif (right_element==self.value):
                print("element found at the end:", right_element)
            else:
                for i in range(len(self.dt)):
                    if (self.dt[i]==self.value):
                        print(f"element '{self.value}' found in tuple at '{i+1}' position")
        # sets
        elif type(self.dt)==set:
            print("set datatype:", self.dt)
            for i,item in enumerate(self.dt):
                if (item==self.value):
                    print(f"element '{self.value}' found in set at '{i+1}' position")
        # strings
        elif (type(self.dt)==str):
            print("string datatype:", self.dt)
            if str(self.value) in self.dt:
                print(f"element '{self.value}' found in set at '{self.dt.find(str(self.value))+1}' position")




# datatypes
list_datatype=[1,5,8,9]
tuple_datatype=(1,8,5,7)
set_datatype={1,5,8,9}
int_string_datatype='1245'

# instances and call methods
# list
list_linear_search=LinearSearch(list_datatype)
list_linear_search.search(2)

print()

# tuples
tuple_linear_search=LinearSearch(tuple_datatype)
tuple_linear_search.search(5)

print()

# sets
set_linear_search=LinearSearch(set_datatype)
set_linear_search.search(5)

print()

# integer string
int_string_linear_search=LinearSearch(int_string_datatype)
int_string_linear_search.search(2)