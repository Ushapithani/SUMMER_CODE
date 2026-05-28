def productExceptSelf(nums):
    n = len(nums)

    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

nums = [1,2,3,4]

print(productExceptSelf(nums))



def twoSum(nums, target):

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))



def findMedian(nums1, nums2):

    arr = nums1 + nums2
    arr.sort()

    n = len(arr)

    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) / 2

    return arr[n//2]

nums1 = [1,3]
nums2 = [2]

print(findMedian(nums1, nums2))




def search(nums, target):

    for i in range(len(nums)):

        if nums[i] == target:
            return i

    return -1

nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums, target))



def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:

        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))


def trap(height):

    n = len(height)

    left = [0] * n
    right = [0] * n

    left[0] = height[0]

    for i in range(1, n):
        left[i] = max(left[i-1], height[i])

    right[n-1] = height[n-1]

    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], height[i])

    water = 0

    for i in range(n):
        water += min(left[i], right[i]) - height[i]

    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))



def threeSum(nums):

    nums.sort()

    result = []

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == 0:

                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))