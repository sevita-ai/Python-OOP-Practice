class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self.available = True
class Library:
    def __init__ (self):
        self.books = []
    def add_book (self,book):
        self.books.append(book)
    def issue_book (self,title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    return "Book is issued"
                else:
                     return "Book is not available"   
        return "Book not found!"
    def return_book (self,title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    return "Book returned successfully"
                else:
                    return "Book is not returned"
        return "Book not found"
    def show_available_books (self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book.title)
        return available_books
b1 = Book("Python Fundamentals", "Guido")
b2 = Book("Data Science in AI", "Andrew")
b3 = Book("AI Basics", "Geoffrey")
library = Library()

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

print(library.issue_book("Python Fundamentals"))
print(library.issue_book("Python Fundamentals"))
print(library.return_book("Python Fundamentals"))
print(library.issue_book("Python Fundamentals"))

print("Available books:", library.show_available_books())
