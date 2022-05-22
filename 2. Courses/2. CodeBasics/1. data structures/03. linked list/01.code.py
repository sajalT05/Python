# create node class --> 
class Nodes:
    def __init__(self,data=None,next=None):
        # assign and contain data --> store data
        self.data=data
        # initialize next as null --> pointer to next element
        self.next=next
# create individual element
class LinkedList:
    def __init__(self,):
        # points to the head of the linked list
        self.head=None
    # insert element at the beginning of the list
    def insert_at_beginning(self,data):
        # inserting data value at beginning of the list
        # points to the head element as next element
        node=Node(data,self.head)
        self.head=node
    # print linked list
    def print(self):
        # if blank
        if self.head is None:
            print("empty linked list")
            return
        # iterate through linked list
        iterate=self.head
        
    


if __name__=="__main__":
    
    # start with empty list
    # instance of linked list
    llist=LinkedList()
