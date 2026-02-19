#Two threads: EvenFactor and OddFactor
import threading

# EvenFactor thread function
def even_factors(n):
    evens = [i for i in range(1, n+1) if n % i == 0 and i % 2 == 0]
    print(f"Even factors of {n}: {evens}, Sum: {sum(evens)}")

# OddFactor thread function
def odd_factors(n):
    odds = [i for i in range(1, n+1) if n % i == 0 and i % 2 != 0]
    print(f"Odd factors of {n}: {odds}, Sum: {sum(odds)}")

num = int(input("Enter a number: "))

# Create threads
t1 = threading.Thread(target=even_factors, args=(num,), name="EvenFactor")
t2 = threading.Thread(target=odd_factors, args=(num,), name="OddFactor")

# Start threads
t1.start()
t2.start()

# Wait for both threads
t1.join()
t2.join()

print("Exit from main")
