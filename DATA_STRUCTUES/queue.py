'''railway ticket counter system 

a railway station manages customer waiting i a queue 
 perform the follwing questions 
 class railway :
    [1,2,3,456,7,0]
    enque -> add a customer with token number x 
    dequeue -> remove customer from front 
    front -> display the token number of last customer
    rear -> diplay the number of customers 
    size -> display the number of customers in the queue

'''
'''class Railway:
    def __init__(self):
        self.queue = []

    def enque(self, token_number):
        self.queue.append(token_number)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def rear(self):
        return len(self.queue)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print("Queue:", self.queue)
railway = Railway()
n = 4 
for i in range(n):
    token_number = int(input("Enter the token number of the customer: "))
    railway.enque(token_number)
railway.display()
print("Front customer token number:", railway.front())
print("Rear customer token number:", railway.rear())
print("Number of customers in the queue:", railway.size())'''


play=[]
n=int(input(" enter the number of songs"))
for  i in range(n):
    song =input("enter the songs:  ").split()
    if song[0]=="add":
        play.append(song[1])
    if song[0]=="next":
        a=play.pop(0)
        print("pop song:",a)
        play.append(a)
print(play)