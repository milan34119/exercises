def rotate(xs, n):
    for _ in range(n):
        x = xs.pop(0)
        xs.append(x)

    return xs

def rotate(xs, n):
    n = n % len(xs)  # Ensure n is within the bounds of xs's length
    return xs[n:] + xs[:n]
