"""

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def lengthOfLongestSubstring(s):
    start = 0
    maxLen = 0
    lookup = {}

    for i, c in enumerate(s):
        if c in lookup and start <= lookup[c]:
            start = lookup[c] + 1
        else:
            maxLen = max(maxLen, i - start + 1)
        lookup[c] = i
    return maxLen


lengthOfLongestSubstring("abcabcbb")
