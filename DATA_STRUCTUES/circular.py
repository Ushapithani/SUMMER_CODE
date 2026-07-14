# circular linked list insertion and deletion
from turtle import pos


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class circularlinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):# end 
    
        new_node = Node(data)
        #  first we have to insert the node and then we have to make the last node point to the first node
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    def delete(self):
        if self.head == None:
            print("List is empty")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
    def deletion_at_position(self, position):
        temp=self.head
        if self.head==None:
            print("List is empty")
            return
        if position==0:
            self.delete_at_beg()
            return
        for i in range(1,position-1):
            temp=temp.next
        temp.next=temp.next.next
        
    def display(self):
        if self.head == None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end="-> ")
            current = current.next
            if current == self.head:
                break
        print()
c = circularlinkedlist()
n = int(input("Enter the number of elements to insert: "))
for i in range(n):
    data = int(input(f"Enter element {i+1}: "))
    c.insert(data)
c.display()
c.delete()
c.display()
