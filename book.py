class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"

        print(
            f"{self.book_id} | "
            f"{self.title} | "
            f"{self.author} | "
            f"{status}"
        )