def main():
    num = int(input("Enter the number : "))
    
    for i in range(2,num+1):
        if(i % 2 == 0):
            print(i,"\t")
        
if __name__ == "__main__":
    main()