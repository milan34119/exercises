# Write your code here
def drop_nth(xs, n):
    left = xs[:n]
    right = xs[n+1:]
    return left+right