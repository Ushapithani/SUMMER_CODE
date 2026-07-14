class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
    def delete_at_position(self,pos):
        if self.head is None:
            print("List is empty.")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        current_node = self.head
        for i in range(pos-1):
            if current_node is None:
                print("Position out of bounds.")
                return
            current_node = current_node.next
        if current_node.next is None:
            print("Position out of bounds.")
            return
        current_node.next = current_node.next.next
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def insert_at_middle(self,prev_node,data):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def insert_at_position(self,pos,data):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        for i in range(pos-1):
            if current_node is None:
                print("Position out of bounds.")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
n = int(input("Enter the number of nodes: "))
ll = LinkedList()
l2 = []
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    ll.insert_at_end(data)
    l2.append(data)


ll.display()
print("List 2:", l2)
