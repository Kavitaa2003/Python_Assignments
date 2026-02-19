num = int(input("Enter number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

print(sum)
