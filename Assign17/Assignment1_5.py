num = int(input("Enter number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("It is Prime Number")
else:
    print("It is Not Prime Number")
