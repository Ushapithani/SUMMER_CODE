
# searchh a key element in nthe arrsy using binary search 
def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
key = 7
result = binary_search(arr, key)
print(result)


# write a program to print the index of first occurrence of a key element in the array using binary search
def first_occurrence(arr, key):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            result = mid
            right = mid - 1  
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return result
