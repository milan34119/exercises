# Write your code here
def rotate(xs, n):
    n = n % len(xs)  # Ensure n is within the bounds of xs's length
    return xs[n:] + xs[:n]