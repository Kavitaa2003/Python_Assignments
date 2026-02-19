from functools import reduce

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = [2, 70, 11, 10, 17, 23, 31, 77]

# Filter prime numbers
primes = list(filter(is_prime, numbers))

# Multiply each prime by 2
mapped = list(map(lambda x: x * 2, primes))

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, mapped)

print("Filtered List:", primes)
print("Mapped List:", mapped)
print("Output of reduce:", maximum)
