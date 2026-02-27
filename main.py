from library import Library

library = Library("data.txt")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")