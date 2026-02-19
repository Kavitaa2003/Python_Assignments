#Sum of all elements
n = int(input("Number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Input element: "))
    numbers.append(num)

total = sum(numbers)
print("Sum of elements:", total)
