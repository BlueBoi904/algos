"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 

characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


"""

import re


def isPalindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase

    # check if s == s.reverse()
    new = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return new[::-1] == new


isPalindrome("A man, a plan, a canal: Panama")
