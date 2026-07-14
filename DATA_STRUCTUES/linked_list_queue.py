class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_at_begin(self):
        if self.head is None:
            print("Queue is empty. Nothing to delete.")
            return
        self.head = self.head.next

    def display(self):
        if self.head is None:
            print("Queue is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


node = Queue()
n = int(input("Enter the number of operations: "))

for _ in range(n):
    operation = input("Enter operation (insert /delete/display): ").split()

    if operation[0] == "insert":
        if len(operation) > 1:
            data = int(operation[1])
            node.insert_at_end(data)
        else:
            print("Please provide a value to insert.")
    elif operation[0] == "delete":
        node.delete_at_begin()
    elif operation[0] == "display":
        node.display()
    else:
        print("Invalid operation. Use insert/delete/display.")



# Linked List on Queues
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Qll:
    def __init__(self):
        self.head=None
    def enqueue(self,data): #insert at rear/end
        nn=Node(data)
        temp=self.head
        if self.head==None:
            self.head=nn
            return
        while temp.next is not None:
            temp =temp.next
        temp.next=nn
    def dequeue(self): #delete at beg/front
        if self.head==None:
            print("Queue is empty")
            return
        self.head=self.head.next
    def front(self):
        print("front :",self.head.data)
    def rear(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        print("rear :",temp.data),
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
        print()
a=Qll()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.display()
a.dequeue()
a.display()
a.front()
a.rear()



