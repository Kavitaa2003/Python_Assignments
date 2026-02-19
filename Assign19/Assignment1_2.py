# Lambda to multiply two numbers
multiply = lambda x, y: x * y

a, b = map(int, input("Enter two numbers: ").split())
print("Output:", multiply(a, b))
