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

    # function to insert a new node in between
    def insert(self,previous_node,new_node_data):
        '''
        new node is added after the previous node
        '''
        # check if previous node exists
        if previous_node is None:
            print("Previous node is not in the list")
            return
        # create new node
        new_node = Node(new_node_data)
        # store next of new node as previous node next
        new_node.next = previous_node.next
        # store new node in next of previous node
        previous_node.next = new_node

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
    1 -> 2 -> 4
    '''
    # head node
    llist.head = Node(1)
    # other nodes
    second = Node(2)
    fourth = Node(4)
    # link nodes
    llist.head.next = second
    second.next = fourth

# --> add new node in between
    '''
    1 -> 2 -> 3 -> 4
    '''
    # 'second' is new node
    llist.insert(second,3)

# --> print linked list
    llist.printList()