#Three threads: Small, Capital, and Digits
import threading

def count_lowercase(s):
    count = sum(1 for ch in s if ch.islower())
    print(f"[{threading.get_ident()}] {threading.current_thread().name}: Lowercase count = {count}")

def count_uppercase(s):
    count = sum(1 for ch in s if ch.isupper())
    print(f"[{threading.get_ident()}] {threading.current_thread().name}: Uppercase count = {count}")

def count_digits(s):
    count = sum(1 for ch in s if ch.isdigit())
    print(f"[{threading.get_ident()}] {threading.current_thread().name}: Digits count = {count}")

text = input("Enter a string: ")

t1 = threading.Thread(target=count_lowercase, args=(text,), name="Small")
t2 = threading.Thread(target=count_uppercase, args=(text,), name="Capital")
t3 = threading.Thread(target=count_digits, args=(text,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
