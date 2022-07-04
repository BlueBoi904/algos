"""

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
   
    
"""


def search(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = round(left + ((right - left) / 2))
        num = nums[mid]
        if num == target:
            return mid
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
