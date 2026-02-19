import MarvellousNum

def ListPrime(numbers):
    total = 0
    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            total += num
    return total

# Main
n = int(input("Number of elements: "))
numbers = [int(input("Input element: ")) for _ in range(n)]
sum_primes = ListPrime(numbers)
print("Sum of prime numbers:", sum_primes)
