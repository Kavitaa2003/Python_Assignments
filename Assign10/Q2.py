def main():
    num = int(input("Enter the number : "))
    sum = 0

    for i in range(1,num+1):
        sum = sum + i
    print("The sum is : ",sum)
        
if __name__ == "__main__":
    main()