"""
    
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array.


"""


def majorityElement(nums):
    # Return the majority element in the nums arr.
    counts = {}
    for item in nums:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0]


print(majorityElement([3, 2, 3]))
