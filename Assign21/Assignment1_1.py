#Two threads: Prime and NonPrime numbers from a list
import threading
import math

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_thread(numbers):
    primes = [x for x in numbers if is_prime(x)]
    print(f"Prime numbers: {primes}")

def non_prime_thread(numbers):
    non_primes = [x for x in numbers if not is_prime(x)]
    print(f"Non-prime numbers: {non_primes}")

# Input list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

t1 = threading.Thread(target=prime_thread, args=(numbers,), name="PrimeThread")
t2 = threading.Thread(target=non_prime_thread, args=(numbers,), name="NonPrimeThread")

t1.start()
t2.start()

t1.join()
t2.join()
