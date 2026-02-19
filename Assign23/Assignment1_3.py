import math

class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(math.sqrt(self.Value)) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        factors = [i for i in range(1, self.Value + 1) if self.Value % i == 0]
        print(f"Factors of {self.Value}: {factors}")
        return factors

    def SumFactors(self):
        return sum(self.Factors())

    def ChkPerfect(self):
        sum_of_factors = sum([i for i in range(1, self.Value) if self.Value % i == 0])
        return sum_of_factors == self.Value

num1 = Numbers(6)
print(f"{num1.Value} is prime? {num1.ChkPrime()}")
num1.Factors()
print(f"Sum of factors: {num1.SumFactors()}")
print(f"{num1.Value} is perfect? {num1.ChkPerfect()}")

print("----")

num2 = Numbers(13)
print(f"{num2.Value} is prime? {num2.ChkPrime()}")
num2.Factors()
print(f"Sum of factors: {num2.SumFactors()}")
print(f"{num2.Value} is perfect? {num2.ChkPerfect()}")
