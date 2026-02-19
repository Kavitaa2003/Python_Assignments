def main():
    num = int(input("Enter the number : "))
    count = 0

    if num <= 1:
        print("Not a prime number")
        return
        
    for i in range(2,num):
        if(num % i == 0 ):
            print("Not a prime number")
            return
    
    print("Number is prime")

    
        
if __name__ == "__main__":
    main()