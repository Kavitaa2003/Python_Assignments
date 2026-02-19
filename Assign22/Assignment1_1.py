class Demo:
    Value = 100  # Class variable

    def __init__(self, no1, no2):
        self.no1 = no1  # Instance variable
        self.no2 = no2  # Instance variable

    def Fun(self):
        print(f"Fun() -> no1: {self.no1}, no2: {self.no2}")

    def Gun(self):
        print(f"Gun() -> no1: {self.no1}, no2: {self.no2}")


# Create objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Call methods in the given sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
