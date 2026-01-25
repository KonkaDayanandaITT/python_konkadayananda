class Book:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def describe(self):
        print(f"The {self.name} book is {self.status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the Library")
            return

        for book in self.books:
            book.describe()

    def lend_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                if book.status == "available":
                    book.status = "issued"
                    print(f"The book {book.name} has been issued")
                else:
                    print(f"The book {book.name} is not available")
                return

        print(f"Book not found in library")

    def receive_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                if book.status == "issued":
                    book.status = "available"
                    print(f"The book {book.name} has been returned")
                else:
                    print(f"The book {book.name} was not issued")
                return

        print(f"This book does not belong to this library")


book1 = Book("C language", "available")
book2 = Book("Python", "available")
book3 = Book("Java", "available")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n---- Library Books -----")
library.display_books()

print("\n---- Lending a book ----")
library.lend_book("Python")

print("\n---- After Lending ----")
library.display_books()

print("\n---- Receiving a book ---- ")
library.receive_book("Python")

print("\n---- Final Library books ----")
library.display_books()
