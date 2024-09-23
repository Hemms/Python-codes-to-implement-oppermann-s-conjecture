import math

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    max_divisor = math.isqrt(num) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate a list of prime numbers up to a given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def check_oppermann_conjecture(n):
    """Check Oppermann's Conjecture for a given value of n."""
    primes = generate_primes(n * n)

    for i in range(n * n - n, n * n + n + 1):
        if is_prime(i):
            if i < n * n:
                print(f"{i} is prime in range {i} * ({i} - 1)")
            elif i > n * n:
                print(f"{i} is prime in range {i} * ({i} + 1)")

# Test with n = 5
n = 5
check_oppermann_conjecture(n)
