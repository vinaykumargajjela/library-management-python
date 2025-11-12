# main.py
from src.library import Library

def print_menu():
    """
    Helper function to just print the menu options.
    Keeps the main loop cleaner.
    """
    print("\n========= 📚 Library Management System ==========")
    print("1.  Add a new book")
    print("2.  Update book quantity")
    print("3.  Remove a book")
    print("4.  Register a new borrower")
    print("5.  Update borrower contact")
    print("6.  Remove a borrower")
    print("7.  Borrow a book")
    print("8.  Return a book")
    print("9.  Search for a book (by title, author, or genre)")
    print("10. Show all books")
    print("11. Show all borrowers (and their borrowed books)")
    print("0.  Exit")
    print("==================================================")

def main():
    """
    The main function that runs the application.
    It contains the main loop.
    """
    # Create one instance of the Library. This object will manage everything.
    library = Library()

    # --- Pre-populate with some sample data to make testing easier ---
    print("Loading sample data...")
    library.add_book("1984", "George Orwell", "978-0451524935", "Dystopian", 5)
    library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", "Fiction", 3)
    library.add_borrower("Alice Smith", "alice@email.com", "M001")
    library.add_borrower("Bob Johnson", "bob@email.com", "M002")
    # --- End of sample data ---

    while True:
        print_menu()
        choice = input("Enter your choice (0-11): ")

        try:
            # --- Book Management ---
            if choice == '1':
                print("\n--- Add New Book ---")
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                genre = input("Enter genre: ")
                quantity = int(input("Enter quantity: ")) # Use int() to convert string to number
                library.add_book(title, author, isbn, genre, quantity)

            elif choice == '2':
                print("\n--- Update Book Quantity ---")
                isbn = input("Enter ISBN of book to update: ")
                quantity = int(input("Enter new total quantity: "))
                library.update_book_quantity(isbn, quantity)
                
            elif choice == '3':
                print("\n--- Remove Book ---")
                isbn = input("Enter ISBN of book to remove: ")
                library.remove_book(isbn)

            # --- Borrower Management ---
            elif choice == '4':
                print("\n--- Register New Borrower ---")
                name = input("Enter name: ")
                contact = input("Enter contact (email/phone): ")
                member_id = input("Enter new membership ID (e.g., M003): ")
                library.add_borrower(name, contact, member_id)
                
            elif choice == '5':
                print("\n--- Update Borrower Contact ---")
                member_id = input("Enter membership ID: ")
                contact = input("Enter new contact info: ")
                library.update_borrower_contact(member_id, contact)
                
            elif choice == '6':
                print("\n--- Remove Borrower ---")
                member_id = input("Enter membership ID to remove: ")
                library.remove_borrower(member_id)

            # --- Library Operations ---
            elif choice == '7':
                print("\n--- Borrow Book ---")
                member_id = input("Enter your membership ID: ")
                isbn = input("Enter the ISBN of the book to borrow: ")
                library.borrow_book(member_id, isbn)

            elif choice == '8':
                print("\n--- Return Book ---")
                member_id = input("Enter your membership ID: ")
                isbn = input("Enter the ISBN of the book to return: ")
                library.return_book(member_id, isbn)

            # --- Search & View ---
            elif choice == '9':
                print("\n--- Search for Book ---")
                print("Search by: (1) Title, (2) Author, (3) Genre")
                search_type = input("Enter search type (1, 2, or 3): ")
                search_term = input("Enter search term: ")
                
                if search_type == '1':
                    library.search_book(search_term, "title")
                elif search_type == '2':
                    library.search_book(search_term, "author")
                elif search_type == '3':
                    library.search_book(search_term, "genre")
                else:
                    print("Invalid search type. Please enter 1, 2, or 3.")

            elif choice == '10':
                library.show_all_books()

            elif choice == '11':
                library.show_all_borrowers()

            # --- Exit ---
            elif choice == '0':
                print("Thank you for using the Library Management System. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 0 and 11.")

        except ValueError:
            # This is simple error handling. It catches errors if the user
            # types 'five' instead of '5' for a quantity.
            print("\nError: Invalid input. Please enter numbers where required (like quantity).")
        except Exception as e:
            # A general catch-all for any other unexpected errors.
            print(f"\nAn unexpected error occurred: {e}")

# This is a standard Python convention.
# It means "only run the main() function if this file is executed directly."
if __name__ == "__main__":
    main()