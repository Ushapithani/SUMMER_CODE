'''def print_numbers(n):
    # base case
    if n == 0:
        return
    else:
        if n % 2 == 0:
            print("Number divisible by 2:", n)
    print_numbers(n - 1)

n = int(input("Enter a number: "))
print_numbers(n)'''



def fibonacci(a, b, n):
    if n == 0:
        return
    else:
        print(a)
        fibonacci(b, a + b, n - 1)

n = int(input("Enter how many terms: "))
fibonacci(0, 1, n)


# print the sum of n numbers using recursion , product of n numbers using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)

n = int(input("Enter a number: "))
print("Sum of first", n, "numbers is:", sum_numbers(n))


def product_numbers(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * product_numbers(n - 1)

n = int(input("Enter a number: "))
print("Product of first", n, "numbers is:", product_numbers(n))


# factorial of a number 
# Recursiv
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial (recursive):", factorial_recursive(num))
print("Factorial (iterative):", factorial_iterative(num))



# power of a number using recusion ,reverse ,paralindrome or not 
number = 3
power=5
3
9
27
81
243

def power(number, power):
    if number == 0:
        return 0
    else:
        return number ** power

n = int(input("Enter the number: "))
m = int(input("Enter the power: "))

for i in range(1, m + 1):
    print(n ** i)

result = power(n, m)
print("Result:", result)



def reverse(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    return reverse(n // 10, rev * 10 + digit)

n = int(input("Enter the number: "))
result = reverse(n)
print("Reversed number:", result)



# reverse of string 
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("usha"))


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))   
print(is_palindrome("racecar"))
print(is_palindrome("hello"))   


# count of digits 
def count_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_digits(num // 10)

num1 = int(input("Enter a number: "))
res = count_digits(num1)
print("Count of digits:", res)


# print nth term in the fibonnacci series 



# sum of the digits 


# product of the digits 


# find gcd using recursion

# find lcm




