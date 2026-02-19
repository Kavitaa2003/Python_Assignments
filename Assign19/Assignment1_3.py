from functools import reduce

numbers = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# Filter numbers between 70 and 90
filtered = list(filter(lambda x: 70 <= x <= 90, numbers))

# Add 10 to each number
mapped = list(map(lambda x: x + 10, filtered))

# Product of all numbers
product = reduce(lambda x, y: x * y, mapped)

print("Filtered List:", filtered)
print("Mapped List:", mapped)
print("Output of reduce:", product)
