

def leaders(arr):
    ans = []
    max_right = arr[-1]

    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= max_right:
            ans.append(arr[i])
            max_right = arr[i]

    print(ans[::-1])

arr = [16, 17, 4, 3, 5, 2]
leaders(arr)