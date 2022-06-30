"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 

typically using all the original letters exactly once.


"""


def isAnagram(s, t):
    sCount = {}
    tCount = {}
    for char in s:
        if char in sCount:
            sCount[char] += 1
        else:
            sCount[char] = 1

    for char in t:
        if char in tCount:
            tCount[char] += 1
        else:
            tCount[char] = 1

    for key in tCount:
        if key in sCount:
            if sCount[key] != tCount[key]:
                return False
        else:
            return False

    for key in sCount:
        if key in tCount:
            if sCount[key] != tCount[key]:
                return False
        else:
            return False

    return True

# Alt solution, sort both list. If the sorted lists are the same, the two strings are an anagram.


def isAnagramSort(s, t):
    return "".join(sorted(s)) == "".join(sorted(t))


isAnagram("a", "ab")
isAnagramSort("a", "ab")
