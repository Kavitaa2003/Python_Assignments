class Circle:
    PI = 3.14  # Class variable

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")


# Create multiple Circle objects
circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

print("----")

circle2 = Circle()
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()
