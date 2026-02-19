class BankAccount:
    ROI = 10.5  # Class variable: Rate of Interest

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder: {self.Name}, Balance: {self.Amount}")

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt
        print(f"Deposited {amt}. New Balance: {self.Amount}")

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt > self.Amount:
            print("Insufficient balance!")
        else:
            self.Amount -= amt
            print(f"Withdrawn {amt}. New Balance: {self.Amount}")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current balance: {interest}")
        return interest


# Example usage
acc1 = BankAccount("Alice", 5000)
acc1.Display()
acc1.Deposit()
acc1.Withdraw()
acc1.CalculateInterest()

print("----")

acc2 = BankAccount("Bob", 10000)
acc2.Display()
acc2.Deposit()
acc2.Withdraw()
acc2.CalculateInterest()
