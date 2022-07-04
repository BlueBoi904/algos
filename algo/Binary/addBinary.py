"""

Given two binary strings a and b, return their sum as a binary string.
 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
    
    
"""


def addBinary(a, b):

    output = int(a) + int(b)
    return "{:b}".format(output)


addBinary('11', '1')
