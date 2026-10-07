from book import Book
class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def issue_book(self, book_id, member_id):

        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            print("Book not found.")
            return

        if member is None:
            print("Member not found.")
            return

        if not book.available:
            print("Book is already issued.")
            return

        book.available = False
        member.borrow_book(book)

        print("Book issued successfully.")

    def return_book(self, book_id, member_id):

        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book and member:
            book.available = True
            member.return_book(book)

            print("Book returned successfully.")

    def find_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def find_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def show_books(self):

        for book in self.books:
            book.display()

    def load_books(self, filepath):
        with open(filepath) as f:
            for line in f:
                book_id, title, author = line.strip().split(",")
                self.add_book(Book(int(book_id), title, author))