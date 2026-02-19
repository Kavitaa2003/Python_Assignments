def CheckGreater(no1,no2):
    if no1 < no2 :
        print("The greater number is : ",no2)
    else:
        print("The greater number is : ",no1)

def main():

    no1 = int(input("Enter the first number  : "))
    no2 = int(input("Enter the second number : "))

    CheckGreater(no1,no2)

if __name__ == "__main__":
    main()