from collections import deque

stack=deque()
print("deque:",stack)

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

# Initial stack
print("Initial stack:", stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:',stack.pop(),stack.pop(),stack.pop())
  
print('\nStack after elements are popped:', stack)