'''
The selection sort algorithm sorts an array by 
    repeatedly finding the minimum element 
    (considering ascending order) from unsorted 
    part and putting it at the beginning. 
    
The algorithm maintains two subarrays in a given array.
    The subarray which is already sorted. 
    Remaining subarray which is unsorted.
'''

'''
Time Complexity: 
                The time complexity of Selection Sort is O(N2) 
                    as there are two nested loops:
                One loop to select an element of Array one by one = O(N)
                Another loop to compare that element with 
                    every other Array element = O(N)
                Therefore overall complexity = O(N)*O(N) = O(N*N) = O(N2)

Auxiliary Space: 
                O(1) as the only extra memory used is for temporary 
                    variable while swapping two values in Array. 
                The good thing about selection sort is it never 
                    makes more than O(n) swaps and can be useful when memory 
                    write is a costly operation. 
'''
'''
Approach:
        Initialize minimum value(min_idx) to location 0
        Traverse the array to find the minimum element in the array
        While traversing if any element smaller than min_idx is 
            found then swap both the values.
        Then, increment min_idx to point to next element
        Repeat until array is sorted
'''
class SelectionSort:
    def __init__(self,list):
        self.list=list
    
    def sort(self):
        list_data=self.list
        length=len(list_data)
        # traverse through list
        for i in range(length):
            temp=0
            # traverse through remaining list
            for j in range(i+1,length):
                # if any number is less than first loop element, swap them
                if list_data[j]<list_data[i]:
                    temp=list_data[i]
                    list_data[i]=list_data[j]
                    list_data[j]=temp
        print(self.list)

# datatypes
list=[5,8,1,6,9]

# instances
# list
list_selection_sort=SelectionSort(list)
list_selection_sort.sort()