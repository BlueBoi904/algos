# Nested loop, find every possible sub arr.

# def maxSubArray(nums):
#     if nums == []:
#         return 0

#     maxSum = nums[0]
#     for i in range(len(nums) + 1):
#         for j in range(i):
#             tempSum = sum(nums[j: i])
#             if tempSum > maxSum:
#                 maxSum = tempSum
#     return maxSum


# Dynamic programming, kadane algorithm

def maxSubArray(nums):
    max_sum, cur_sum = float('-inf'), 0
    for n in nums:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(max_sum, cur_sum)
    return max_sum


maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
