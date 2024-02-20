# Write your code here
# def digit_sum(x):
#     string_x = str(x)
#     sum = 0
#     for number in string_x:
#         sum += int(number)
#     print(sum)
# digit_sum(5189)

def last_digit(x):
    return x % 10

def remove_last_digit(x):
    return x // 10

def digit_sum(x):
    