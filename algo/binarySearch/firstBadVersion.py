def isBadVersion(num):
    return True


def firstBadVersion(n):
    # Perform a binary search on the sorted list, find the first bad version.
    left, right = 0, n
    firstBad = n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            firstBad = mid
            right = mid - 1
        else:
            left = mid + 1
