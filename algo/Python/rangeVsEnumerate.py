# Fizzbuzz example

# Enumerate

def fizz_buzz(numbers):
    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"
