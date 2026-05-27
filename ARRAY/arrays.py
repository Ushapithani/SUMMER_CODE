# 1. Smallest Element in Array using if else

n = int(input())
arr = list(map(int, input().split()))

small = arr[0]

for i in arr:
    if i < small:
        small = i
    else:
        small = small

print(small)


# 2. Largest Element in array 

n = int(input())
arr = list(map(int, input().split()))

large = arr[0]

for i in arr:
    if i > large:
        large = i
    else:
        large = large

print(large)


# 3. Second Smallest Element  

n = int(input())
arr = list(map(int, input().split()))

small = arr[0]
second = arr[0]

for i in arr:

    if i < small:
        second = small
        small = i

    elif i < second and i != small:
        second = i

print(second)

# 4. Second Largest Element  

n = int(input())
arr = list(map(int, input().split()))

large = arr[0]
second = arr[0]

for i in arr:

    if i > large:
        second = large
        large = i

    elif i > second and i != large:
        second = i

print(second)


# 5. Reverse Array  

n = int(input())
arr = list(map(int, input().split()))

result = []

for i in range(n-1, -1, -1):
    result.append(arr[i])

print(*result)



# 6. Frequency of Elements

n = int(input())
arr = list(map(int, input().split()))

freq = {}

for i in arr:

    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

for key in freq:
    print(key, freq[key])


# 7. Remove Duplicates

n = int(input())
arr = list(map(int, input().split()))

result = []

for i in arr:

    if i not in result:
        result.append(i)

    else:
        pass 

print(*result)


# 8 Rotate Array  by k places 

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

result = arr[k:] + arr[:k]

print(*result)


# 9. Find Repeating Elements

n = int(input())
arr = list(map(int, input().split()))

freq = {}

for i in arr:

    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

for key in freq:

    if freq[key] > 1:
        print(key, end=" ")




# 10. Find Non-Repeating Elements

n = int(input())
arr = list(map(int, input().split()))

freq = {}

for i in arr:

    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

for key in freq:

    if freq[key] == 1:
        print(key, end=" ")


# 11. Equilibrium Index

n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
left = 0

for i in range(n):

    total = total - arr[i]

    if left == total:
        print(i)
        break

    else:
        left = left + arr[i]

else:
    print(-1)




# 12 . maax product subarray 
n = int(input())
arr = list(map(int, input().split()))

max_product = arr[0]

for i in range(n):
    product = 1
    for j in range(i, n):
        product *= arr[j]
        max_product = max(max_product, product)

print(max_product)



# 13.median of array 
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if n % 2 == 1:
    print(arr[n // 2])
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    print(median)


    id

# 14.array subset

n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

subset = True

for i in range(n2):
    if arr2[i] in arr1:
        pass
    else:
        subset = False
        break

if subset:
    print("Yes")
else:
    print("No")


# 15 search element 

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

for i in arr:
    if i == target:
        print("Found")
        break
else:
    print("Not Found")


# 16 symmetric pairs 

n = int(input())

s = set()
res = []

for _ in range(n):
    a, b = map(int, input().split())

    if (b, a) in s:
        res.append((b, a))
    else:
        s.add((a, b))

for i in res:
    print(i[0], i[1])



# 17 missing number 
n = int(input())
arr = list(map(int, input().split()))

total = n * (n + 1) // 2
sum_arr = sum(arr)

print(total - sum_arr)






# 18 leaders in an array 
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    leader = True

    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            leader = False
            break
        else:
            pass

    if leader:
        print(arr[i], end=" ")





