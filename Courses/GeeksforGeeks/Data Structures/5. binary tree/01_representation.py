# create node
class Node:
    def __init__(self,data):
        self.data=data
        # right branch as none
        self.right=None
        # left branch as none
        self.left=None

# create nodes
rootnode=Node(5)
rightnode=Node(10)
leftNode=Node(15)
# link nodes
rootnode.left=leftNode
rootnode.riht=rightnode
        
