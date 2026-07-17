# 1. Check if a Given String is Palindrome
s = input()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Input: madam
# Palindrome


# 2. Count Number of Vowels, Consonants, and Spaces
s = input().lower()

vowels = consonants = spaces = 0

for ch in s:
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)

# Output:
# Input: Hello World
# Vowels: 3
# Consonants: 7
# Spaces: 1


# 3. Find the ASCII Value of a Character
ch = input()

print(ord(ch))

# Output:
# Input: A
# 65


# 4. Remove All Vowels from a String
s = input()

result = ""

for ch in s:
    if ch.lower() not in "aeiou":
        result += ch

print(result)

# Output:
# Input: education
# dctn


# 5. Remove Spaces from a String
s = input()

print(s.replace(" ", ""))

# Output:
# Input: Hello World
# HelloWorld


# 6. Remove Characters from a String Except Alphabets
s = input()

result = ""

for ch in s:
    if ch.isalpha():
        result += ch

print(result)

# Output:
# Input: abc123@#XYZ
# abcXYZ


# 7. Reverse a String
s = input()

print(s[::-1])

# Output:
# Input: Python
# nohtyP


# 8. Remove Brackets from an Algebraic Expression
s = input()

result = ""

for ch in s:
    if ch not in "(){}[]":
        result += ch

print(result)

# Output:
# Input: (a+b)*(c+d)
# a+b*c+d


# 9. Sum of the Numbers in a String
s = input()

total = 0

for ch in s:
    if ch.isdigit():
        total += int(ch)

print(total)

# Output:
# Input: a2b5c3
# 10


# 10. Capitalize First and Last Character of Each Word
words = input().split()

result = []

for word in words:
    if len(word) == 1:
        result.append(word.upper())
    else:
        word = word[0].upper() + word[1:-1] + word[-1].upper()
        result.append(word)

print(" ".join(result))

# Output:
# Input: hello world
# HellO WorlD

# 11. Calculate Frequency of Characters in a String
s = input()

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

# Output:
# Input: apple
# {'a': 1, 'p': 2, 'l': 1, 'e': 1}


# 12. Find Non-Repeating Characters of a String
s = input()

for ch in s:
    if s.count(ch) == 1:
        print(ch, end=" ")

# Output:
# Input: programming
# p o a i n


# 13. Check if Two Strings are Anagram of Each Other
s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

# Output:
# Input:
# listen
# silent
# Anagram


# 14. Count Common Characters in Two Strings
s1 = input()
s2 = input()

count = 0

for ch in set(s1):
    if ch in s2:
        count += 1

print(count)

# Output:
# Input:
# abcde
# bcdf
# 3


# 15. Check if Two Strings Match Where One String Contains Wildcard Characters
s = input()
pattern = input()

if len(s) != len(pattern):
    print("No Match")
else:
    match = True

    for i in range(len(s)):
        if pattern[i] != '?' and s[i] != pattern[i]:
            match = False
            break

    if match:
        print("Match")
    else:
        print("No Match")

# Output:
# Input:
# hello
# he?lo
# Match


# 16. Return Maximum Occurring Character in the Input String
s = input()

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(max(freq, key=freq.get))

# Output:
# Input: banana
# a


# 17. Remove All Duplicates from the Input String
s = input()

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

# Output:
# Input: programming
# progamin


# 18. Print All the Duplicates in the Input String
s = input()

printed = ""

for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch, end=" ")
        printed += ch

# Output:
# Input: programming
# r g m


# 19. Remove Characters from First String Present in the Second String
s1 = input()
s2 = input()

result = ""

for ch in s1:
    if ch not in s2:
        result += ch

print(result)

# Output:
# Input:
# computer
# cat
# ompuer


# 20. Change Every Letter with the Next Lexicographic Alphabet
s = input()

result = ""

for ch in s:
    if ch == 'z':
        result += 'a'
    elif ch == 'Z':
        result += 'A'
    else:
        result += chr(ord(ch) + 1)

print(result)

# Output:
# Input: abcxyz
# bcdyza

# 21. Find the Largest Word in a Given String
words = input().split()

largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print(largest)

# Output:
# Input: I love programming language
# programming


# 22. Sort Characters in a String
s = input()

result = "".join(sorted(s))

print(result)

# Output:
# Input: dcba
# abcd


# 23. Count Number of Words in a Given String
s = input()

words = s.split()

print(len(words))

# Output:
# Input: Welcome to Python Programming
# 4


# 24. Find a Word Having the Highest Number of Repeated Letters
sentence = input().split()

best_word = ""
max_repeat = -1

for word in sentence:
    repeat = len(word) - len(set(word))

    if repeat > max_repeat:
        max_repeat = repeat
        best_word = word

print(best_word)

# Output:
# Input: apple banana success
# success


# 25. Change Case of Each Character in a String
s = input()

print(s.swapcase())

# Output:
# Input: PyThOn
# pYtHoN


# 26. Concatenate One String to Another
s1 = input()
s2 = input()

print(s1 + s2)

# Output:
# Input:
# Hello
# World
# HelloWorld


# 27. Find a Substring Within a String
s = input()
sub = input()

position = s.find(sub)

if position != -1:
    print("Found at Index:", position)
else:
    print("Not Found")

# Output:
# Input:
# programming
# gram
# Found at Index: 3


# 28. Reverse Words in a String
s = input()

words = s.split()

print(" ".join(words[::-1]))

# Output:
# Input: I Love Python
# Python Love I