import threading

# Function to print first 10 even numbers
def print_even():
    for i in range(2, 21, 2):
        print(f"Even Thread: {i}")

# Function to print first 10 odd numbers
def print_odd():
    for i in range(1, 20, 2):
        print(f"Odd Thread: {i}")

# Create threads
even_thread = threading.Thread(target=print_even, name="EvenThread")
odd_thread = threading.Thread(target=print_odd, name="OddThread")

# Start threads
even_thread.start()
odd_thread.start()

# Wait for threads to complete
even_thread.join()
odd_thread.join()

print("Main thread exits")
