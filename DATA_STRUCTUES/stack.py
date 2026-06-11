'''# add 95 at the end of the list 
stack = [3, 4, 5, 6, 7, 8, 9,45,]
stack.append(95)
print(stack)

# insert at 50 at index 2 
stack.insert(2, 50)
print(stack)

# extend list with another list 
stack.extend([100, 200, 300])
print(stack)

# count how many time 5 appears in the list
count_5 = stack.count(5)
print(count_5)

# find index position of 100 
index_100 = stack.index(100)
print(index_100)

# sort in ascending order
stack.sort()
print(stack)

# desceding oder
stack.sort(reverse=True)
print(stack)

# reverse the list
stack.reverse()
print(stack)

# remove first occurance of 45
stack.remove(45)
print(stack)

# pop last element and and store it in a variable
last_element = stack.pop()
print(last_element)
print(stack)

# check whether 50 is in the list or not using operrator 
is_50_in_stack = 50 in stack
print(is_50_in_stack)

#concate the first with [10,20]
new_stack = stack+[10,20]
print(new_stack)

# repeat the list 2 times using an operator 
repeated_stack = stack*2
print(repeated_stack)

# slice the list first 3 elements and last 3 elements 
sliced_list = stack[0:3] + stack[-3:]
print(sliced_list)

# create a copy of the list 
copied_stack = stack.copy()
print(copied_stack)

# clear all elements form copied 
copied_stack.clear()
print(copied_stack) 

# display final original stack
print(stack)


# create a list name it as stack apppend any 10 elements into the stack 
# find the lenght of the stack check the stack is overglw ,empty or not

stack = list(range(1,11))
print(stack)

# len
print(len(stack))

# check if stack is empty
is_empty=len(stack)==0
print("stack is empty:", is_empty)

# overflow 
max_size = 10 
is_overflow = len(stack) >= max_size
print("stack is overflow:", is_overflow)'''

# create a class with the name of stack and implement push, pop, peek, is_empty and is_overflow method
class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack overflow")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def is_overflow(self):
        return len(self.stack) >= self.max_size


# Example usage
stack = Stack(5)
stack.push(1)
stack.push(2)       
stack.push(3)
stack.push(4)    
stack.push(5)

print("Stack:", stack.stack)              
print("Top element:", stack.peek())       
print("Popped element:", stack.pop())     
print("Stack:", stack.stack)              
print("stack is empty:", stack.is_empty())                   
print("stack is overflow:", stack.is_overflow())                
