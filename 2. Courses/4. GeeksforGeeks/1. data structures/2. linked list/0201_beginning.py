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
    
    # function to insert a new node at the beginning
    def push(self, new_node_data):
        """
        allocate the new node and put in the data.
        """
        new_node = Node(new_node_data)
        # change head of linked list
        # point head of old linked list to tail of new node
        new_node.next = self.head
        # make new node as head of linked list
        self.head = new_node

# --> print linked list
    # starting from head
    def printList(self):
        # temp variable assigned to head node
        temp = self.head
        while(temp):
            # print data stored in node
            print(temp.data, end=" --> ")
            # iterate through all nodes
            temp = temp.next

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

# --> add new node at the beginning
    '''
    0 -> 1 -> 2 -> 3
    '''
    llist.push(0)


# --> print linked list
    llist.printList()