def runningSum(nums):
    runningSum = 0
    sumArr = []
    for item in nums:
        runningSum += item
        sumArr.append(runningSum)
    return sumArr


runningSum([1, 2, 3, 4])
