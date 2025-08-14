class Book:
    """Represents a book with public title/author and private availability flag."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book to available state. Return True if successful, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Library holds Book instances and manages check-out/return/listing."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self._books.append(book)

    def _find_book_by_title(self, title):
        """Return the Book instance matching the title, or None if not found."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """Attempt to check out a book by title. Return True on success, False otherwise."""
        book = self._find_book_by_title(title)
        if not book:
            return False
        return book.check_out()

    def return_book(self, title):
        """Attempt to return a book by title. Return True on success, False otherwise."""
        book = self._find_book_by_title(title)
        if not book:
            return False
        return book.return_book()

    def list_available_books(self):
        """Print each available book on its own line in 'Title by Author' format."""
        for book in self._books:
            if book.is_available():
                print(str(book))
