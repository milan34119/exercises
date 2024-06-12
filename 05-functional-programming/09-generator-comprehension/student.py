def is_prime(n):
    return n >= 2 and all(n % k != 0 for k in range(2, n))

