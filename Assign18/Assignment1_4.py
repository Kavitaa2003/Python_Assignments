#Frequency of an element
n = int(input("Number of elements: "))
numbers = [int(input("Input element: ")) for _ in range(n)]

x = int(input("Element to search: "))
frequency = numbers.count(x)
print("Frequency of", x, "is:", frequency)
