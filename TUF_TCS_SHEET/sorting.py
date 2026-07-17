# ==========================================
# SORTING ALGORITHMS
# ==========================================

# 1. Bubble Sort

# Compares adjacent elements and swaps them if they are in the wrong order.
# After each pass, the largest element moves to its correct position.

arr = [5, 2, 8, 1, 9]

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Bubble Sort:", arr)

# Output:
# Bubble Sort: [1, 2, 5, 8, 9]


# ==========================================

# 2. Selection Sort

# Finds the smallest element from the unsorted part of the array.
# Places it at the beginning in every iteration.

arr = [5, 2, 8, 1, 9]

n = len(arr)

for i in range(n):

    minimum = i

    for j in range(i + 1, n):
        if arr[j] < arr[minimum]:
            minimum = j

    arr[i], arr[minimum] = arr[minimum], arr[i]

print("Selection Sort:", arr)

# Output:
# Selection Sort: [1, 2, 5, 8, 9]


# ==========================================

# 3. Insertion Sort

# Takes one element at a time and inserts it into its correct position.
# The left part of the array remains sorted after every iteration.

arr = [5, 2, 8, 1, 9]

for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Insertion Sort:", arr)

# Output:
# Insertion Sort: [1, 2, 5, 8, 9]


# ==========================================

# 4. Quick Sort
# Definition:
# Selects a pivot element and partitions the array into two parts.
# Recursively sorts the left and right partitions.

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for num in arr[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5, 2, 8, 1, 9]

print("Quick Sort:", quick_sort(arr))

# Output:
# Quick Sort: [1, 2, 5, 8, 9]


# ==========================================

# 5. Merge Sort
# Definition:
# Divides the array into smaller halves until each part has one element.
# Merges the sorted halves to produce the final sorted array.

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [5, 2, 8, 1, 9]

print("Merge Sort:", merge_sort(arr))

# Output:
# Merge Sort: [1, 2, 5, 8, 9]