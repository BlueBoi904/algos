def isBadVersion(num):
    return True


def firstBadVersion(n):
    firstBad = n
    left, right = 0, n

    while left <= right:
        mid = round(left + ((right - left) / 2))

        if isBadVersion(mid):
            firstBad = mid
            right = mid - 1
        else:
            left = mid + 1
    return firstBad
