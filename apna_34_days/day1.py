# LeetCode 169 - Majority Element

Input:
nums = [2, 2, 1, 1, 1, 2, 2]

Output:
2

Code:
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


nums = [2, 2, 1, 1, 1, 2, 2]
obj = Solution()
print(obj.majorityElement(nums))   # Output: 2



# LeetCode 2965 - Find Missing and Repeated Values

'''Input:
grid = [
    [1, 3],
    [2, 2]
]

Output:
[2, 4]
'''
class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        seen = {}

        for row in grid:
            for num in row:
                if num in seen:
                    seen[num] += 1
                else:
                    seen[num] = 1

        repeated = missing = -1

        for i in range(1, n * n + 1):
            if i in seen and seen[i] == 2:
                repeated = i
            elif i not in seen:
                missing = i

        return [repeated, missing]

grid = [
    [1, 3],
    [2, 2]
]

obj = Solution()
print(obj.findMissingAndRepeatedValues(grid))

Input:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

Output:
[1, 2, 2, 3, 5, 6]

class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

obj = Solution()
obj.merge(nums1, m, nums2, n)

print(nums1)


# LeetCode 136 - Single Number

Input:
nums = [4, 1, 2, 1, 2]

Output:
4

class Solution:
    def singleNumber(self, nums):
        for x in nums:
            if nums.count(x) == 1:
                return x

nums = [4, 1, 2, 1, 2]

obj = Solution()
print(obj.singleNumber(nums))



# Best Time to Buy and Sell Stock (LeetCode 121)

Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)

        return max_profit

prices = [7, 1, 5, 3, 6, 4]

obj = Solution()
print(obj.maxProfit(prices))

# LeetCode 50 - Pow(x, n)

Input:
x = 2.00000
n = 10

Output:
1024.00000

class Solution:
    def myPow(self, x, n):
        return pow(x, n)

x = 2.00000
n = 10

obj = Solution()
print(obj.myPow(x, n))