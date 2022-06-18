stack =[]

# use append() to add elements in stack at last
stack.append(1)
stack.append('a')
stack.append(True)
stack.append([1,55,9989])
stack.append("565")
stack.append("godzilla")

# print inital stack
print("Initial stack:", stack)

# use pop() to remove elements from stack from top
# print elements popped from the stack
print("Elements popped from the stack:", stack.pop(),",", stack.pop(),",", stack.pop())
# print stack
print("Final stack:", stack)