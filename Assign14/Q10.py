largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest:", largest(a, b,))