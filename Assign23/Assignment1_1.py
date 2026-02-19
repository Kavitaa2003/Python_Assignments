class BookStore:
    NoOfBooks = 0  # Class variable

    def __init__(self, Name, Author):
        self.Name = Name          # Instance variable
        self.Author = Author      # Instance variable
        BookStore.NoOfBooks += 1  # Increment class variable

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


# Example usage
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()

Obj3 = BookStore("Python Programming", "Guido van Rossum")
Obj3.Display()
