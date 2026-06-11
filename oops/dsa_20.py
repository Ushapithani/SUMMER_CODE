# 1. Find the Smallest Number in an Array

arr = list(map(int, input().split()))
smallest = arr[0]
for num in arr:
    if num < smallest:
        smallest = num
print(smallest)


# 2. Find the Largest Number in an Array

arr = list(map(int, input().split()))
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print(largest)


# 3. Second Smallest and Second Largest Element in an Array

arr = [5, 2, 8, 1, 9]

smallest = arr[0]
second_smallest = arr[0]

largest = arr[0]
second_largest = arr[0]

for num in arr[1:]:

    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif second_smallest == smallest or num < second_smallest:
        second_smallest = num

    if num > largest:
        second_largest = largest
        largest = num

    elif second_largest == largest or num > second_largest:
        second_largest = num

print("Second Smallest =", second_smallest)
print("Second Largest =", second_largest)




# 4. Reverse a Given Array

arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)


# 5. Count Frequency of Each Element in an Array

arr = list(map(int, input().split()))
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
for key, value in freq.items():
    print(key, value)


# 6. Rearrange Array in Increasing-Decreasing Order

arr = list(map(int, input().split()))
arr.sort()
mid = len(arr) // 2
first = arr[:mid]
second = arr[mid:]
second.reverse()
print(first + second)


# 7. Calculate Sum of the Elements of the Array

arr = [1, 2, 3, 4, 5]

total = 0

for num in arr:
    total = total + num

print("Sum =", total)

# 8. Rotate Array by K Elements

arr = list(map(int, input().split()))
k = int(input())
k %= len(arr)
arr = arr[-k:] + arr[:-k]
print(arr)


# 9. Average of All Elements in an Array

arr = list(map(int, input().split()))
avg = sum(arr) / len(arr)
print(avg)


# 10. Find the Median of the Given Array

arr = sorted(list(map(int, input().split())))
n = len(arr)
if n % 2 == 0:
    median = (arr[n//2] + arr[n//2 - 1]) / 2
else:
    median = arr[n//2]
print(median)


# 11. Remove Duplicates from a Sorted Array

arr = list(map(int, input().split()))
result = []
for num in arr:
    if num not in result:
        result.append(num)
print(result)


# 12. Remove Duplicates from an Unsorted Array

arr = list(map(int, input().split()))
print(list(set(arr)))


# 13. Adding Element in an Array

arr = list(map(int, input().split()))
x = int(input())
arr.append(x)
print(arr)


# 14. Find All Repeating Elements in an Array

arr = list(map(int, input().split()))
seen = set()
repeating = set()
for num in arr:
    if num in seen:
        repeating.add(num)
    else:
        seen.add(num)
print(list(repeating))


# 15. Find All Non-Repeating Elements in an Array

arr = list(map(int, input().split()))
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
for key in freq:
    if freq[key] == 1:
        print(key, end=" ")
print()


# 16. Find All Symmetric Pairs in an Array

pairs = [(1, 2), (3, 4), (2, 1), (5, 6)]
s = set()
for a, b in pairs:
    if (b, a) in s:
        print((a, b))
    s.add((a, b))


# 17. Maximum Product Subarray in an Array
arr = [2, 3, -2, 4]

max_product = arr[0]

for i in range(len(arr)):
    product = 1

    for j in range(i, len(arr)):
        product *= arr[j]

        if product > max_product:
            max_product = product

print("Maximum Product =", max_product)

# 18. Replace Each Element of the Array by Its Rank

arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
rank = {}

for i, num in enumerate(sorted_arr):
    rank[num] = i + 1

for num in arr:
    print(rank[num], end=" ")
print()


# 19. Sorting Elements of an Array by Frequency

arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

result = []

sorted_keys = sorted(freq, key=freq.get, reverse=True)

for key in sorted_keys:
    for i in range(freq[key]):
        result.append(key)

print(result)


# 20. Rotation of Elements of Array - Left Rotation

arr = list(map(int, input().split()))
k = int(input())
k %= len(arr)
print(arr[k:] + arr[:k])


# 21. Rotation of Elements of Array - Right Rotation

arr = list(map(int, input().split()))
k = int(input())
k %= len(arr)
print(arr[-k:] + arr[:-k])


# 22. Finding Equilibrium Index of an Array

n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
left = 0

for i in range(n):
    total -= arr[i]

    if left == total:
        print(i)
        break

    left += arr[i]
else:
    print(-1)


# 23. Finding Circular Rotation of an Array by K Positions

arr = list(map(int, input().split()))
k = int(input())

k %= len(arr)

rotated = arr[-k:] + arr[:-k]
print(rotated)


# 24. Sort an Array According to the Order Defined by Another Array

arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
arr2 = [2, 1, 8, 3]

result = []

for num in arr2:
    while num in arr1:
        result.append(num)
        arr1.remove(num)

result.extend(sorted(arr1))
print(result)


# 25. Search an Element in an Array

arr = [10, 20, 30, 40, 50]
key = 30

found = False

for num in arr:
    if num == key:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")

# 26. Check if Array is a Subset of Another Array or Not

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 5]

is_subset = True

for num in arr2:
    if num not in arr1:
        is_subset = False
        break

if is_subset:
    print("Subset")
else:
    print("Not a Subset")