# create node class
class Node:
    # inititalize node creation
    def __init__(self,data):
        # assign data
        self.data=data
        # assign next --> null
        self.next=None

# create linked list class
class LinkedList:
    # initialize creation of linked list head
    def __init__(self):
        self.head=None
    
# --> add node at start
    def push(self,new_node):
        # assign next of new node as head of old linked list
        new_node.next=self.head
        # make new node as head of linked list
        self.head=new_node

# --> add node in between
    def insert(self,previous_node,new_node_data):
        # check if previous node exists
        if previous_node is None:
            print("Previous node is not in the list")
            return
        # create new node
        new_node=Node(new_node_data)
        # store next of new node as previous node next
        new_node.next=previous_node.next
        # store new node in next of previous node
        previous_node.next=new_node

# --> add node at end
    def append(self,new_node):
        #  check if linked list is empty
        if self.head is None:
            print("empty linked list")
            return
        # traverse through linked list
        # create a temprorary variable and point to head
        temp_insertion=self.head
        # iterate through all nodes
        while(temp_insertion.next):
            # move to next node
            temp_insertion=temp_insertion.next
        # assign next of last node as new node
        temp_insertion.next=new_node

# --> print linked list
    def printLinkedList(self):
        # assign a temprorary variable to head
        temp_print=self.head
        # iterate through all nodes
        while(temp_print):
            # print data stored in node
            print(temp_print.data, end=" --> ")
            # shoft to next node nodes --> temporary varibale points to next node
            temp_print=temp_print.next


# execute codes in this file
if __name__ == '__main__':
    # create linked list
    llist=LinkedList()
    # create nodes
    '''
    1 -> 2 -> 4
    '''
    # head node
    llist.head=Node(1)
    # create second node
    second=Node(2)
    # create third node
    fourth=Node(4)
    # link nodes
    llist.head.next=second
    second.next=fourth

    # add node at start
    '''
    0 -> 1 -> 2 -> 4
    '''
    llist.push(Node(0))

    # add node in between
    '''
    0 -> 1 -> 2 -> 3 -> 4
    '''
    llist.insert(second,3)

    # add node at end
    '''
    0 -> 1 -> 2 -> 3 -> 4 -> 5
    '''
    llist.append(Node(5))

    # print linked list
    llist.printLinkedList()
