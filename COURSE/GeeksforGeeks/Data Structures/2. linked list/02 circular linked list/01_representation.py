# node class
class Node:
    # function to initialize the node object
    def __init__(self,data):
        # Assign data
        self.data = data
        # Initialize next as null
        self.next = None

# Linked List class
class LinkedList:
    
    # function to initialize head
    def __init__(self):
        self.head = None
    
# --> print linked list
    # starting from head
    def printLinkedList(self):
        # temp variable assigned to head node
        temp = self.head
        while(temp):
            # print data stored in node
            print(f"[{temp.data}, -->]", end="  ")
            # iterate through all nodes
            temp = temp.next
            # terminate loop when head element is again iterated
            if temp==self.head:
                break


# start code execution
if __name__ == '__main__':


# --> create linked list
    # start with empty list
    llist = LinkedList()
    '''
    1 -> 2 -> 3
    '''
    # head node
    llist.head = Node(1)
    # other nodes
    second = Node(2)
    third = Node(3)
    
    # link nodes
    llist.head.next = second
    second.next = third
    # link last node to first node
    third.next=llist.head

# --> print linked list
    llist.printLinkedList()