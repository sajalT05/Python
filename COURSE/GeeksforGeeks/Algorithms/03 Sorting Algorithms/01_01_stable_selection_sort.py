'''
Example: 
        4A 5 3 2 4B 1
            First minimum element is 1, now instead
                of swapping. Insert 1 in its correct place 
                and pushing every element one step forward
            i.e forward pushing.
                1 4A 5 3 2 4B
            Next minimum is 2 :
                1 2 4A 5 3 4B
            Next minimum is 3 :
                1 2 3 4A 5 4B
            Repeat the steps until array is sorted.
                1 2 3 4A 4B 5
'''

class StableSelectionSort:
    # register values
    def __init__(self,list):
        self.list=list
        print("input list")
        print(self.list)


    # sort list
    def sort(self):
        # list
        list_input=self.list
        list_length=len(list_input)
        # traverse through list
        for i in range(list_length):
            # temporary variable to store main loop iterated index position
            temp_index=i
            # traverse through remaining elements
            for j in range(i+1,list_length):
                # check i any element is smaller
                if list_input[j]<list_input[temp_index]:
                    # assign new index poistion to temp variable
                    temp_index=j
                # shift elements
                # shift elements before temp_index index position towards right
                # store temp_index element
                temp_element=list_input[temp_index]
                # loop till iterator index poistion reached
                while temp_index>i:
                    # shift element before temp_index position to right 
                    list_input[temp_index]=list_input[temp_index-1]
                    # decrease temp_index value
                    temp_index-=1
                # iterator element is now empty
                # allocate temp_element stored at iterator index poistion
                list_input[i]=temp_element

    # print list
    def print(self):
        print()
        print("sorted list")
        print(self.list)


list=[5,8,7,3,1,5,9,13,52,2]
# create instace of StableSelectionSort class
sortlist=StableSelectionSort(list)
# sort
sortlist.sort()
# print
sortlist.print()

