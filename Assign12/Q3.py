def add(a, b):
    print("Addition:", a + b)

def sub(a, b):
    print("Subtraction:", a - b)

def mul(a, b):
    print("Multiplication:", a * b)

def div(a, b):
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division not possible")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add(a, b)
sub(a, b)
mul(a, b)
div(a, b)
