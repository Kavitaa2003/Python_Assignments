def main():
    num = int(input("Enter the number: "))
    rev = 0

    while num != 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num //10

    if num < 0:
        rev = -rev

    print("Reversed number:", rev)

if __name__ == "__main__":
    main()
