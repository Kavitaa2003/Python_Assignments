from functools import reduce

numbers = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

# Filter even numbers
filtered = list(filter(lambda x: x % 2 == 0, numbers))

# Square each number
squared = list(map(lambda x: x**2, filtered))

# Sum of all numbers
total = reduce(lambda x, y: x + y, squared)

print("Filtered List:", filtered)
print("Mapped List:", squared)
print("Output of reduce:", total)
