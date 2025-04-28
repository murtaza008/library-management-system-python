# Book class banai gayi hai jismein title, author aur ISBN store hota hai
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


# Custom Exception agar koi book available na ho
class BookNotAvailableException(Exception):
    pass


# Library class banai gayi hai jismein books ka management hota hai
class Library:
    def __init__(self):
        self.books = []          # yahan available books store hoti hain
        self.lent_books = []     # yahan lent books store hoti hain

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' has been removed from the library.")
                return
        print("No book with this ISBN found in the library.")

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.lent_books.append(book)
                print(f"Book '{book.title}' has been lent.")
                return
        raise BookNotAvailableException("This book is currently not available.")

    def return_book(self, isbn):
        for book in self.lent_books:
            if book.isbn == isbn:
                self.lent_books.remove(book)
                self.books.append(book)
                print(f"Book '{book.title}' has been returned to the library.")
                return
        print("This book was not lent from the library.")

    def available_books(self):
        return [book for book in self.books]

    # Custom iterator taake books pe loop lag sake
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


# DigitalLibrary class banai gayi hai jo Library se inherit karti hai
class DigitalLibrary(Library):
    def __init__(self):
        super().__init__()
        self.ebooks = []  # yahan e-books aur unka size store hota hai

    def add_ebook(self, book, download_size):
        self.ebooks.append((book, download_size))
        print(f"E-book '{book.title}' (size: {download_size}MB) has been added to the digital library.")

    def remove_ebook(self, isbn):
        for ebook, size in self.ebooks:
            if ebook.isbn == isbn:
                self.ebooks.remove((ebook, size))
                print(f"E-book '{ebook.title}' has been removed from the digital library.")
                return
        print("No e-book with this ISBN found in the digital library.")

    def view_ebooks(self):
        if not self.ebooks:
            print("No e-books in the digital library.")
        else:
            print("\nAvailable E-Books:")
            for ebook, size in self.ebooks:
                print(f"{ebook.title} by {ebook.author} (ISBN: {ebook.isbn}, Size: {size}MB)")


# Generator function jo specific author ki books return karta hai
def books_by_author(library, author):
    for book in library.available_books():
        if book.author == author:
            yield book


# Program ka main function
def main():
    library = DigitalLibrary()  # DigitalLibrary ka object banaya gaya hai

    # 3 books manually add ki gayi hain
    library.add_book(Book("The Lord of the Rings", "Muhammad Bilal", "978-05449"))
    library.add_book(Book("Rich Dad Poor Dad", "Robert Kiyosaki", "978-01414"))
    library.add_book(Book("The Godfather", "Mario Puzo", "978-04515"))

    # 2 e-books manually add ki gayi hain
    library.add_ebook(Book("Introduction To Python", "Muhammad Bilal", "978-15932"), "15")
    library.add_ebook(Book("Harry Potter", "Murtaza Butt", "978-77881"), "20")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. View Available Books")
        print("6. View Books by Author")
        print("7. Add E-Book")
        print("8. Remove E-Book")
        print("9. View Available E-Books")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(Book(title, author, isbn))

        elif choice == '2':
            isbn = input("Enter ISBN of book to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            isbn = input("Enter ISBN of book to lend: ")
            try:
                library.lend_book(isbn)
            except BookNotAvailableException as e:
                print(e)

        elif choice == '4':
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)

        elif choice == '5':
            print("\nAvailable Books:")
            for book in library:
                print(book)

        elif choice == '6':
            author = input("Enter author name: ")
            print(f"\nBooks by {author}:")
            for book in books_by_author(library, author):
                print(book)

        elif choice == '7':
            title = input("Enter e-book title: ")
            author = input("Enter e-book author: ")
            isbn = input("Enter e-book ISBN: ")
            size = input("Enter download size in MB: ")
            library.add_ebook(Book(title, author, isbn), size)

        elif choice == '8':
            isbn = input("Enter ISBN of e-book to remove: ")
            library.remove_ebook(isbn)

        elif choice == '9':
            library.view_ebooks()

        elif choice == '10':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Program yahan se start hota hai
if __name__ == "__main__":
    main()
