# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


# Child class
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        # Call parent constructor
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    # Override method (shows only title and author)
    def display_book_details(self):
        super().display_book_details()

    def display_issued_book_details(self):
        # Calling parent method using inheritance
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# Create object
book1 = IssuedBook(
    "The Power",
    "John Smith",
    "Parvathi",
    "04-02-2026"
)

# Display all details
book1.display_issued_book_details()