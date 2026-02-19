#Two threads with synchronization (Thread1 and Thread2)i
import threading

def thread1_func():
    for i in range(1, 51):
        print(f"Thread1: {i}")

def thread2_func():
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")

# Thread1 executes first
t1 = threading.Thread(target=thread1_func, name="Thread1")
t2 = threading.Thread(target=thread2_func, name="Thread2")

t1.start()
t1.join()  # Ensure Thread1 finishes before Thread2 starts

t2.start()
t2.join()
