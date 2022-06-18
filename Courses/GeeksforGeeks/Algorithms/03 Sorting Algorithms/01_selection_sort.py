'''
The selection sort algorithm sorts an array by 
    repeatedly finding the minimum element 
    (considering ascending order) from unsorted 
    part and putting it at the beginning. 
    
The algorithm maintains two subarrays in a given array.
    The subarray which is already sorted. 
    Remaining subarray which is unsorted.
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