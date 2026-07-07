def BruteForceSum(arr):
    max_sum = arr[0]
    min_sum = arr[0]
    for i in range(len(arr)):
        curr_sum = 0 
        for j in range(i, len(arr)):
            curr_sum *= arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < min_sum:
                min_sum = curr_sum
    print("max_sum:", max_sum)
    print("min_sum:", min_sum)

nums = list(map(int, input("Enter the numbers: ").split()))
BruteForceSum(nums)
