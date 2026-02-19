n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not palindrome number")
