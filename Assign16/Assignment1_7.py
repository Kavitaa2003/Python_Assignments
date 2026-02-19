def DivByFive(no):
    if no % 5 == 0:
        return True
    else:
        return False

num = int(input("Enter number: "))
print(DivByFive(num))
