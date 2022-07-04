"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


"""


def canConstruct(ransomNote, magazine):
    def count(s):
        tempCount = {}
        for char in s:
            if char in tempCount:
                tempCount[char] += 1
            else:
                tempCount[char] = 1
        return tempCount
    ransomCount = count(ransomNote)
    magazineCount = count(magazine)

    for key in ransomCount:
        if key not in magazineCount or (ransomCount[key] > magazineCount[key]):
            return False
    return True


print(canConstruct("aa", "aab"))
