def isSubsequence(s, t):
    left_bound, right_bound = len(s), len(t)
    left = right = 0

    while left < left_bound and right < right_bound:
        # move both pointers or just the right pointer
        if s[left] == t[right]:
            left += 1
        right += 1

    return left == left_bound
