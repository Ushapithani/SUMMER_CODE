'''input :
8 
10 20 0 31 0 41 52 0 
output :
10 20 31 41 52 0 0 0 

'''
'''n = int(input())
arr = list(map(int,input().split()))
non_zero =[]
for x in arr:
    if x!=0:
        non_zero.append(x)
diff = n-len(non_zero)
for i in range(diff):
    non_zero.append(0)
print(*non_zero)'''


'''
Sample Input:
aabbbccccdde
Sample Output :
Distinct Species: 5
Most Common: c 4
Least Common: e 1
Species Frequency:
a 2
b 3
c 4
d 2
e 1'''


n = input()
freq = {}

for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1 

dist = len(freq)

max_char = max(freq,key= freq.get)
count = freq[max_char]


min_char = min(freq,key = freq.get)
min_count = freq[min_char]

print("Distinct Species",dist)
print("Most common",max_char, count)
print("Least common",min_char, min_count)

for i in freq:
    print(i,freq[i])

# ==========================
# Forest Tree Plantation Management
# ==========================

n = int(input())
arr = list(map(int, input().split()))

result = []

for num in arr:
    if num != 0:
        result.append(num)

while len(result) < n:
    result.append(0)

print(*result)





# ==========================
# Renewable Energy Billing System
# ==========================

class EnergyConsumer:
    def __init__(self, name, cid, units):
        self.name = name
        self.cid = cid
        self.units = units


class SolarConsumer(EnergyConsumer):
    def calculate_bill(self):
        return self.units * 6


class WindConsumer(EnergyConsumer):
    def calculate_bill(self):
        return self.units * 5


t = int(input())
name = input()
cid = int(input())
units = int(input())

if t == 1:
    obj = SolarConsumer(name, cid, units)
    print("Energy Source: Solar")
else:
    obj = WindConsumer(name, cid, units)
    print("Energy Source: Wind")

print("Consumer:", obj.name)
print("ID:", obj.cid)
print("Units:", obj.units)
print("Bill:", obj.calculate_bill())


# ==========================
# Question 4
# Book Return Management System
# ==========================

n = int(input())
stack = []

for _ in range(n):
    op = input().split()

    if op[0] == "RETURN":
        stack.append(op[1])

    elif op[0] == "ISSUE":
        if stack:
            print("Issued Book:", stack.pop())
        else:
            print("No Books Available")

    elif op[0] == "TOP":
        if stack:
            print("Top Book:", stack[-1])
        else:
            print("No Books Available")

    elif op[0] == "SIZE":
        print("Books Count:", len(stack))

    elif op[0] == "DISPLAY":
        if stack:
            print("Books:", *stack[::-1])
        else:
            print("Library Stack is Empty")


# ==========================
# Question 5
# Forest Rescue Camp Registration System
# ==========================

n = int(input())
animals = []

for _ in range(n):
    op = input().split()

    if op[0] == "REGISTER":
        animals.append(op[1])

    elif op[0] == "EMERGENCY":
        animals.insert(0, op[1])

    elif op[0] == "REMOVE":
        if op[1] in animals:
            animals.remove(op[1])
            print("Removed:", op[1])
        else:
            print("Animal Not Found")

    elif op[0] == "COUNT":
        print("Total Animals:", len(animals))

    elif op[0] == "DISPLAY":
        if animals:
            print("Animals:", *animals)
        else:
            print("No Animals Registered")