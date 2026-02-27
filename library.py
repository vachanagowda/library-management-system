class Library:
    def __init__(self, filename):
        self.filename = filename

    def add_book(self, book_name):
        with open(self.filename, "a") as file:
            file.write(book_name + "\n")
        print("Book added successfully.")

    def view_books(self):
        try:
            with open(self.filename, "r") as file:
                books = file.readlines()
                if books:
                    print("\nAvailable Books:")
                    for book in books:
                        print("- " + book.strip())
                else:
                    print("No books available.")
        except FileNotFoundError:
            print("No books available.")

    def remove_book(self, book_name):
        try:
            with open(self.filename, "r") as file:
                books = file.readlines()

            with open(self.filename, "w") as file:
                for book in books:
                    if book.strip() != book_name:
                        file.write(book)

            print("Book removed successfully.")
        except FileNotFoundError:
            print("No books found.")