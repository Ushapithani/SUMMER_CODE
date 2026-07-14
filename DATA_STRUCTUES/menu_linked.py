'''
1x = insert at head of the linked list 
2x= insert at end of the linked list
3px  = insert at position of the linked list
SAMPLE INPUT  2 30 
1 30 
2 20 
3 30 
INPUT FORMAT 
FIRST  line contains an integer q,the number of operations 
next q lines contains one of the following 
1x
2x
3x'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_head(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def insert_at_position(self,pos,data):
        new_node = node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for i in range(pos-1):
            if current_node is None:
                print("Position out of bounds.")
                return
            current_node = current_node.next
        if current_node is None:
            print("Position out of bounds.")
            return
        new_node.next = current_node.next
        current_node.next = new_node
q=int(input())
l=Linkedlist()
a  = l.insert_at_head
b = l.insert_at_end
c = l.insert_at_position
print("Enter the operations:")
print("1x = insert at head of the linked list"
      
      "\n2x= insert at end of the linked list"
      "\n3px  = insert at position of the linked list"
      )

for i in range(q):
    operation = input().strip()
    if operation.startswith('1'):
        data = int(operation[1:])
        a(data)
    elif operation.startswith('2'):
        data = int(operation[1:])
        b(data)
    elif operation.startswith('3'):
        pos_data = operation[1:].split()
        pos = int(pos_data[0])
        data = int(pos_data[1])
        c(pos, data)
    else:
        print("Invalid operation.")




