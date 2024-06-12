
# Write a function `repeat(function, n)` that simply calls `function` `n` times.
# You can assume `function` takes no arguments and returns nothing useful.


def function():
    print('Hello world fucker')
def repeat(function, n):
    for _ in range(n):
        function()

repeat(function, 5)