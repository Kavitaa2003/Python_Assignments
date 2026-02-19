#Two threads: Maximum and Minimum from list
import threading

def max_thread(numbers):
    print(f"Maximum element: {max(numbers)}")

def min_thread(numbers):
    print(f"Minimum element: {min(numbers)}")

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

t1 = threading.Thread(target=max_thread, args=(numbers,), name="MaxThread")
t2 = threading.Thread(target=min_thread, args=(numbers,), name="MinThread")

t1.start()
t2.start()

t1.join()
t2.join()
