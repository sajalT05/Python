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

    # function to add a node at the end
    def append(self, new_node_data):
        # create a new node
        new_node = Node(new_node_data)
        # check if the list is empty
        if self.head is None:
            # if list is empty, then make the new node as head
            self.head = new_node
            return
        # else traverse till the last node
        temp_last_node=self.head
        while(temp_last_node.next):
            temp_last_node = temp_last_node.next
        # assign the new node to the temprorary last node through traversal
        temp_last_node.next = new_node
    
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

# --> add new node at the end
    '''
    1 -> 2 -> 3 -> 4
    '''
    llist.append(4)   

# --> print linked list
    llist.printList()
 