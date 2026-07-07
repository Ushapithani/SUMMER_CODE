# non repeating character using linear search 
s = input("Enter the string: ")

for i in s:
    if s.count(i) == 1:
        print("First non-repeating character:", i)
        break


# highest occurrence of an element using linear search 
s = input("Enter the string: ")
max_count = 0
max_char = ''
for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        max_char = i
print(max_char, max_count)

# second least element in the array
arr = list(map(int, input("Enter the array elements: ").split()))
arr.sort()
print("Second least element:", arr[1])


