def max(lst):
    max_num = -float('inf')
    # Breakpoint, use 'n' in terminal to progress through each line of code after breakpoint
    breakpoint()
    for num in lst:
        print(num, max_num)
        if num > max_num:
            max_num = num

    return max_num


name = 'Bob'
age = 10
print(f'My name is {name}. I am {age} years old.')
