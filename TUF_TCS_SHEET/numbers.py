
# 1. Check if a Number is Palindrome
num = 121

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome


# 2. Find all Palindrome Numbers in a Given Range
start = 10
end = 200

for num in range(start, end + 1):
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if num == reverse:
        print(num, end=" ")

print()

# Output:
# 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191


# 3. Check if a Number is Prime
num = 29

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

# Output:
# Prime


# 4. Prime Numbers in a Given Range
start = 10
end = 50

for num in range(start, end + 1):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")

print()

# Output:
# 11 13 17 19 23 29 31 37 41 43 47


# 5. Check if a Number is Armstrong Number
'''
An Armstrong Number (also called a Narcissistic Number) is a 
number that is equal to the sum of its own digits, 
where each digit is raised to the power of the total number of digits.'''
num = 153

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")

# Output:
# Armstrong


# 6. Check if a Number is Perfect Number
'''
A Perfect Number is a positive integer whose sum of all its 
proper divisors (excluding the number itself) is equal to the number.'''
num = 28

sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")

# Output:
# Perfect Number


# 7. Even or Odd
num = 15

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
# Odd


# 8. Positive, Negative or Zero
num = -10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Output:
# Negative


# 9. Sum of First N Natural Numbers
n = 10

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

# Output:
# Sum = 55


# 10. Sum of AP Series
a = 2
d = 3
n = 5

sum = 0

for i in range(n):
    sum += a + i * d

print("AP Sum =", sum)

# Output:
# AP Sum = 40


# 11. Sum of GP Series
a = 2
r = 3
n = 5

sum = 0

for i in range(n):
    sum += a * (r ** i)

print("GP Sum =", sum)

# Output:
# GP Sum = 242


# 12. Greatest of Two Numbers
a = 15
b = 25

if a > b:
    print(a)
else:
    print(b)

# Output:
# 25

# 13. Greatest of Three Numbers
a = 10
b = 25
c = 18

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

# Output:
# Greatest: 25


# 14. Leap Year or Not
year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Output:
# Leap Year


# 15. Reverse Digits of a Number
num = 12345

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse:", reverse)

# Output:
# Reverse: 54321


# 16. Maximum and Minimum Digit in a Number
num = 583429

maximum = 0
minimum = 9

while num > 0:
    digit = num % 10

    if digit > maximum:
        maximum = digit

    if digit < minimum:
        minimum = digit

    num //= 10

print("Maximum Digit:", maximum)
print("Minimum Digit:", minimum)

# Output:
# Maximum Digit: 9
# Minimum Digit: 2


# 17. Print Fibonacci up to Nth Term
n = 10

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()

# Output:
# 0 1 1 2 3 5 8 13 21 34


# 18. Factorial of a Number
num = 5

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)

# Output:
# Factorial: 120


# 19. Power of a Number
base = 2
power = 5

result = 1

for i in range(power):
    result *= base

print("Answer:", result)

# Output:
# Answer: 32


# 20. Factors of a Given Number
num = 24

print("Factors:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

print()

# Output:
# Factors:
# 1 2 3 4 6 8 12 24


# 21. Print All Prime Factors of a Number
num = 84

print("Prime Factors:")

for i in range(2, num + 1):

    if num % i == 0:

        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            print(i, end=" ")

print()

# Output:
# Prime Factors:
# 2 3 7


# 22. Check if a Number is Strong Number
num = 145

temp = num
sum = 0

while temp > 0:

    digit = temp % 10

    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    sum += fact

    temp //= 10

if sum == num:
    print("Strong Number")
else:
    print("Not Strong Number")

# Output:
# Strong Number


# 23. Check if a Number is Automorphic
num = 25

square = num * num

if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not Automorphic")

# Output:
# Automorphic Number


# 24. GCD of Two Numbers
a = 36
b = 60

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD:", gcd)

# Output:
# GCD: 12

# 25. LCM of Two Numbers
a = 12
b = 18

greater = max(a, b)

while True:
    if greater % a == 0 and greater % b == 0:
        print("LCM:", greater)
        break
    greater += 1

# Output:
# LCM: 36


# 26. Check if a Number is Harshad Number
num = 18

temp = num
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

if num % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")

# Output:
# Harshad Number


# 27. Check if a Number is Abundant Number
num = 18

sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div > num:
    print("Abundant Number")
else:
    print("Not Abundant Number")

# Output:
# Abundant Number


# 28. Sum of Digits of a Number
num = 12345

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of Digits:", sum_digits)

# Output:
# Sum of Digits: 15


# 29. Sum of Numbers in the Given Range
start = 10
end = 20

total = 0

for i in range(start, end + 1):
    total += i

print("Sum:", total)

# Output:
# Sum: 165


# 30. Permutations (N People can Occupy R Seats)
n = 5
r = 3

fact_n = 1
fact_nr = 1

for i in range(1, n + 1):
    fact_n *= i

for i in range(1, n - r + 1):
    fact_nr *= i

print("Permutation:", fact_n // fact_nr)

# Output:
# Permutation: 60


# 31. Add Two Fractions
num1 = 1
den1 = 2

num2 = 3
den2 = 4

numerator = (num1 * den2) + (num2 * den1)
denominator = den1 * den2

print("Sum =", numerator, "/", denominator)

# Output:
# Sum = 10 / 8


# 32. Replace all 0s with 1s
num = 10203040

result = ""

for ch in str(num):
    if ch == "0":
        result += "1"
    else:
        result += ch

print(int(result))

# Output:
# 11213141


# 33. Can a Number be Expressed as Sum of Two Prime Numbers
num = 34

for i in range(2, num):

    prime1 = True

    for j in range(2, i):
        if i % j == 0:
            prime1 = False
            break

    if prime1:

        second = num - i

        prime2 = True

        for j in range(2, second):
            if second % j == 0:
                prime2 = False
                break

        if prime2:
            print(num, "=", i, "+", second)
            break

# Output:
# 34 = 3 + 31


# 34. Calculate Area of Circle
radius = 7

pi = 3.14159

area = pi * radius * radius

print("Area:", area)

# Output:
# Area: 153.93791


# 35. Program to Find Roots of a Quadratic Equation
import math

a = 1
b = -5
c = 6

d = b * b - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots:", root1, root2)

elif d == 0:
    root = -b / (2 * a)
    print("Equal Roots:", root)

else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)
    print("Roots:", real, "+", imaginary, "i")
    print("Roots:", real, "-", imaginary, "i")

# Output:
# Roots: 3.0 2.0