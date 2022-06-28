"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

"""


def longestPalindrome(s):
    longestPal = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            chunk = s[i:j]
            if palindrome(chunk) and len(chunk) > longestPal:
                longestPal = len(chunk)

    return longestPal


def palindrome(string):
    return string == string[::-1]


print(palindrome("abccccdd"))

print(longestPalindrome("abccccdd"))
