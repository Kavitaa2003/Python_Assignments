#Two threads: EvenList and OddList
import threading

def even_list(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even elements: {evens}, Sum: {sum(evens)}")

def odd_list(numbers):
    odds = [x for x in numbers if x % 2 != 0]
    print(f"Odd elements: {odds}, Sum: {sum(odds)}")

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

t1 = threading.Thread(target=even_list, args=(numbers,), name="EvenList")
t2 = threading.Thread(target=odd_list, args=(numbers,), name="OddList")

t1.start()
t2.start()

t1.join()
t2.join()
