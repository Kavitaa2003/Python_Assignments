def main():
    num = int(input("Enter the number : "))
    fact = 1

    for i in range(1,num+1):
        fact = fact * i

    print("The factorial is : ",fact)
        
if __name__ == "__main__":
    main()