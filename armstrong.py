# palindrome in given range 
def palinodrome(start, end):
    for num in range(start, end + 1):
        temp = num
        rev = 0
        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp //= 10
        if num == rev:
            print(num)
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))   
print("The palindromic numbers in the given range are:")
palinodrome(start, end)

# armstrong number or not 
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# armstrong numbers in given range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Armstrong numbers in the given range are:")
for num in range(start, end + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)  

# prime number in given range 
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
count = 0 
for num in range(start,end+1):
    count = 0 
    for i in range(2,num):
        if num % i == 0:
            count += 1
            break
    if count == 2:
        print(num, "is a prime number")



# fin the max and min of a digit in a given number 
num = int(input("Enter a number: "))
max_digit = 0
min_digit = 9

while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    num //= 10

print("Maximum digit:", max_digit)
print("Minimum digit:", min_digit)

# factors of a given number 
num = int(input("Enter a number: "))
print("Factors of", num, "are:")    
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
