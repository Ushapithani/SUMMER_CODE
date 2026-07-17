
# 1. Find Smallest Element
arr = [5, 2, 8, 1, 9]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)

# Output:
# Smallest: 1


# 2. Find Largest Element
arr = [5, 2, 8, 1, 9]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest:", largest)

# Output:
# Largest: 9


# 3. Find Second Smallest and Second Largest (If-Else)
arr = [5, 2, 8, 1, 9]

smallest = arr[0]
second_smallest = arr[0]

largest = arr[0]
second_largest = arr[0]

for num in arr:

    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif (num < second_smallest or second_smallest == smallest) and num != smallest:
        second_smallest = num

    if num > largest:
        second_largest = largest
        largest = num

    elif (num > second_largest or second_largest == largest) and num != largest:
        second_largest = num

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)

# Output:
# Second Smallest: 2
# Second Largest: 8


# 4. Find Second Smallest and Second Largest (Sorting)
arr = [5, 2, 8, 1, 9]

arr = sorted(set(arr))

print("Second Smallest:", arr[1])
print("Second Largest:", arr[-2])

# Output:
# Second Smallest: 2
# Second Largest: 8


# 5. Reverse an Array
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed:", arr)

# Output:
# Reversed: [5, 4, 3, 2, 1]


# 6. Count Frequency of Each Element
arr = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

# Output:
# {1: 2, 2: 3, 3: 1, 4: 1}


# 7. Rearrange Array in Increasing-Decreasing Order
arr = [8, 7, 1, 6, 5, 9]

arr.sort()

mid = (len(arr) + 1) // 2

arr = arr[:mid] + arr[mid:][::-1]

print(arr)

# Output:
# [1, 5, 6, 9, 8, 7]


# 8. Sum of Elements
arr = [1, 2, 3, 4, 5]

total = 0

for num in arr:
    total += num

print("Sum:", total)

# Output:
# Sum: 15


# 9. Left Rotate by K Elements
arr = [1, 2, 3, 4, 5]

k = 2

k %= len(arr)

arr = arr[k:] + arr[:k]

print(arr)

# Output:
# [3, 4, 5, 1, 2]


# 10. Average of Elements
arr = [10, 20, 30, 40]

total = 0

for num in arr:
    total += num

print("Average:", total / len(arr))

# Output:
# Average: 25.0

# ============================
# ARRAY PROGRAMS (11 - 20)
# ============================

# 11. Median of Array
arr = [5, 2, 1, 4, 3]

arr.sort()

n = len(arr)

if n % 2 == 1:
    print("Median:", arr[n // 2])
else:
    print("Median:", (arr[n // 2] + arr[n // 2 - 1]) / 2)

# Output:
# Median: 3


# 12. Remove Duplicates (Sorted Array)
arr = [1, 1, 2, 2, 3, 4, 4]

result = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        result.append(arr[i])

print(result)

# Output:
# [1, 2, 3, 4]


# 13. Remove Duplicates (Unsorted Array)
arr = [3, 1, 2, 3, 4, 2, 5]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print(result)

# Output:
# [3, 1, 2, 4, 5]


# 14. Find Repeating Elements
arr = [1, 2, 3, 2, 4, 5, 1]

seen = set()
repeating = []

for num in arr:
    if num in seen and num not in repeating:
        repeating.append(num)
    else:
        seen.add(num)

print("Repeating:", repeating)

# Output:
# Repeating: [2, 1]


# 15. Find Non-Repeating Elements
arr = [1, 2, 3, 2, 1, 5]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in arr:
    if freq[num] == 1:
        print("Non-Repeating:", num)

# Output:
# Non-Repeating: 3
# Non-Repeating: 5


# 16. Find Symmetric Pairs

'''
What are Symmetric Pairs?

Two pairs are symmetric if one pair is the reverse of the other.

If you have:

(a, b)

then its symmetric pair is:

(b, a)'''
pairs = [(1,2), (3,4), (5,9), (2,1), (9,5)]

visited = set()

for a, b in pairs:
    if (b, a) in visited:
        print((a, b), (b, a))
    visited.add((a, b))

# Output:
# (2, 1) (1, 2)
# (9, 5) (5, 9)


# 17. Maximum Product Subarray
arr = [2, 3, -2, 4]

max_product = arr[0]
min_product = arr[0]
answer = arr[0]

for i in range(1, len(arr)):

    if arr[i] < 0:
        max_product, min_product = min_product, max_product

    max_product = max(arr[i], max_product * arr[i])
    min_product = min(arr[i], min_product * arr[i])

    answer = max(answer, max_product)

print("Maximum Product:", answer)

# Output:
# Maximum Product: 6


# 18. Replace Each Element by Rank
arr = [20, 15, 26, 2, 98]

sorted_arr = sorted(set(arr))

rank = {}

for i in range(len(sorted_arr)):
    rank[sorted_arr[i]] = i + 1

result = []

for num in arr:
    result.append(rank[num])

print(result)

# Output:
# [3, 2, 4, 1, 5]


# 19. Sort Array by Frequency
arr = [2,3,2,4,5,12,2,3,3,3]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

arr.sort(key=lambda x: (-freq[x], x))

print(arr)

# Output:
# [3, 3, 3, 3, 2, 2, 2, 4, 5, 12]


# 20. Right Rotate by K Elements
arr = [1,2,3,4,5]

k = 2

k %= len(arr)

arr = arr[-k:] + arr[:-k]

print(arr)

# Output:
# [4, 5, 1, 2, 3]


# 21. Finding Equilibrium Index
arr = [-7, 1, 5, 2, -4, 3, 0]

total = sum(arr)
left_sum = 0

for i in range(len(arr)):

    total -= arr[i]

    if left_sum == total:
        print("Equilibrium Index:", i)

    left_sum += arr[i]

# Output:
# Equilibrium Index: 3


# 22. Circular Rotation by K Positions
arr = [1, 2, 3, 4, 5]

k = 3

k %= len(arr)

arr = arr[-k:] + arr[:-k]

print(arr)

# Output:
# [3, 4, 5, 1, 2]


# 23. Sort an Array According to Another Array
arr1 = [2,1,2,5,7,1,9,3,6,8,8]
arr2 = [2,1,8,3]

result = []

for num in arr2:
    while num in arr1:
        result.append(num)
        arr1.remove(num)

arr1.sort()

result.extend(arr1)

print(result)

# Output:
# [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]


# 24. Linear Search
arr = [10,20,30,40,50]

target = 30

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at Index:", i)
        found = True
        break

if not found:
    print("Not Found")

# Output:
# Found at Index: 2


# 25. Binary Search
arr = [10,20,30,40,50]

target = 40

left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at Index:", mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

# Output:
# Found at Index: 3


# 26. Check if One Array is a Subset of Another
arr1 = [11,1,13,21,3,7]
arr2 = [11,3,7,1]

flag = True

for num in arr2:
    if num not in arr1:
        flag = False
        break

if flag:
    print("Subset")
else:
    print("Not a Subset")

# Output:
# Subset