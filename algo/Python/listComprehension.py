# Example 1

lst = [1, 2, -5, 4]


def square(x):
    return x * x


def isOdd(x):
    return x % 2 == 1


oddResult = list(map(isOdd, lst))
result = list(map(square, lst))
print(result)
# Example 2
result2 = []
for num in lst:
    result2.append(square(num))
print(result2)
# Example 3 (List Comprehension)

print([square(num) for num in lst])
