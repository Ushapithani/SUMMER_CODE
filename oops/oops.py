class student :
    pass 
    def __init__(self,name,course):
        self.name = name
        self.course = course
s1 = student("usha","python")
print(s1.name)
print(s1.course)


# create a class of car from the company BMW
class car :
    pass
    def __init__(self,model,color):
        self.model = model
        self.color = color

c1 = car("X5","blue")
print(c1.model)
print(c1.color)


# create a class and object for bike class 
class bike :
    pass
    def __init__(self,model,color):
        self.model = model
        self.color = color

b1 = bike("Yamaha ","red")
print(b1.model)
print(b1.color)

# create a class of flowers including the funcion of parameter name ,color and price ,create 5 objects 
class flowers :
    pass
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
f1 = flowers("rose","red",100)
f2 = flowers("lily","white",150)
f3 = flowers("tulip","yellow",200)
f4 = flowers("daisy","pink",120)
f5 = flowers("red rose","purple",250)
print(f1.name,f1.color,f1.price)
print(f2.name,f2.color,f2.price)
print(f3.name,f3.color,f3.price)
print(f4.name,f4.color,f4.price)
print(f5.name,f5.color,f5.price)



# CREATE A CLASS OF EMPLOYEE FROM TCS COMPANY DISPLAY THE DETAILS OF THAT EMPLOYEE
class employee :
    pass
    def __init__(self,name,salary,id):
        self.name = name
        self.age = age
        self.designation = designation
