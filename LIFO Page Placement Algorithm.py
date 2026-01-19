# Python3 program to demonstrate working of LIFO

# Pushing element on the top of the stack
def stack_push(stack):
    for i in range(5):
        stack.append(i)
    return stack
 
# Popping element from the top of the stack
def stack_pop(stack):
    print("Pop :")
 
    for i in range(5):
        y = stack[-1]
        stack.pop()
        print(y)
    return stack
 
# Displaying element on the top of the stack
def stack_peek(stack):
    element = stack[-1]
    print("Element on stack top :", element)
 
# Searching element in the stack
def stack_search(stack, element):
    pos = -1
    co = 0
    while(len(stack) > 0):
        co+=1
        if(stack[-1] == element):
            pos = co
            break
        stack.pop()
 
    if (pos == -1):
        print( "Element not found")
    else:
        print("Element is found at position", pos)

stack = []
stack_push(stack)
stack_pop(stack)
stack_push(stack)
stack_peek(stack)
stack_search(stack, 2)
stack_search(stack, 6)

