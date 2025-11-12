# src/library.py
from datetime import date, timedelta
from .book import Book
from .borrower import Borrower

class Library:
    """
    This is the main class that manages the entire library system.
    
    It holds all the books and all the borrowers and contains all the
    logic for adding, searching, borrowing, and returning books.
    This class is the "orchestrator" or the "brain" of the app.
    """
    
    def __init__(self):
        """
        The constructor for the Library.
        
        We are using Dictionaries ({}) instead of lists to store
        books and borrowers. This makes finding a specific book (by ISBN)
        or a borrower (by ID) *much* faster.
        
        self.books will store data like:
        { "978-01": <BookObject for '1984'>, "978-02": <BookObject for 'Dune'> }
        """
        self.books = {}  # Key: ISBN, Value: Book Object
        self.borrowers = {}  # Key: Membership ID, Value: Borrower Object

    # --- Book Management ---
    
    def add_book(self, title, author, isbn, genre, quantity):
        """
        Adds a new book to the library's collection.
        """
        if isbn in self.books:
            print(f"Error: Book with ISBN {isbn} already exists. Use 'update' instead.")
        else:
            new_book = Book(title, author, isbn, genre, int(quantity))
            self.books[isbn] = new_book
            print(f"Success: Added '{title}' to the library.")
            
    def update_book_quantity(self, isbn, new_quantity):
        """
        Updates the quantity of an existing book.
        """
        if isbn not in self.books:
            print(f"Error: Book with ISBN {isbn} not found.")
        else:
            self.books[isbn].update_quantity(int(new_quantity))
            print(f"Success: Quantity updated for '{self.books[isbn].title}'.")

    def remove_book(self, isbn):
        """
        Removes a book from the library entirely (e.g., if lost or damaged).
        """
        if isbn not in self.books:
            print(f"Error: Book with ISBN {isbn} not found.")
        else:
            # We use .pop() to remove the item from the dictionary
            removed_book = self.books.pop(isbn)
            print(f"Success: Removed '{removed_book.title}' from the library.")

    # --- Borrower Management ---
    
    def add_borrower(self, name, contact, membership_id):
        """
        Registers a new member (borrower) in the system.
        """
        if membership_id in self.borrowers:
            print(f"Error: Borrower with ID {membership_id} already exists.")
        else:
            new_borrower = Borrower(name, contact, membership_id)
            self.borrowers[membership_id] = new_borrower
            print(f"Success: Registered new borrower '{name}'.")

    def update_borrower_contact(self, membership_id, new_contact):
        """
        Updates a borrower's contact information.
        """
        if membership_id not in self.borrowers:
            print(f"Error: Borrower with ID {membership_id} not found.")
        else:
            self.borrowers[membership_id].update_contact(new_contact)
            
    def remove_borrower(self, membership_id):
        """
        Removes a borrower from the system.
        """
        if membership_id not in self.borrowers:
            print(f"Error: Borrower with ID {membership_id} not found.")
        else:
            # Check if they have any outstanding books
            if self.borrowers[membership_id].borrowed_books:
                print(f"Error: Cannot remove '{self.borrowers[membership_id].name}'. "
                      "They still have books to return.")
            else:
                removed_borrower = self.borrowers.pop(membership_id)
                print(f"Success: Removed borrower '{removed_borrower.name}'.")

    # --- Core Library Functions ---

    def borrow_book(self, membership_id, isbn):
        """
        Handles the logic for a borrower to check out a book.
        """
        # 1. Find the borrower and the book
        borrower = self.borrowers.get(membership_id)
        book = self.books.get(isbn)

        # 2. Perform validation checks
        if not borrower:
            print(f"Error: Borrower ID {membership_id} not found.")
            return
        if not book:
            print(f"Error: Book with ISBN {isbn} not found.")
            return
        
        # 3. Check if the book is available
        if not book.available:
            print(f"Sorry: '{book.title}' is currently out of stock.")
            return
            
        # 4. If all checks pass, proceed with borrowing
        
        # Reduce quantity by 1
        book.update_quantity(book.quantity - 1)
        
        # Calculate due date (14 days from today)
        due_date = date.today() + timedelta(days=14)
        
        # Add the book to the borrower's personal list
        borrower.add_borrowed_book(book, due_date)
        
        print(f"Success: {borrower.name} borrowed '{book.title}'. Due on {due_date}.")

    def return_book(self, membership_id, isbn):
        """
        Handles the logic for a borrower to return a book.
        """
        # 1. Find the borrower and the book
        borrower = self.borrowers.get(membership_id)
        book = self.books.get(isbn)
        
        # 2. Validation
        if not borrower:
            print(f"Error: Borrower ID {membership_id} not found.")
            return
        if not book:
            print(f"Error: Book with ISBN {isbn} not found.")
            return
            
        # 3. Check if the borrower *actually* has this book
        book_found_in_records = False
        for record in borrower.borrowed_books:
            if record["book_isbn"] == isbn:
                book_found_in_records = True
                break
        
        if not book_found_in_records:
            print(f"Error: {borrower.name} does not seem to have borrowed this book.")
            return

        # 4. If all checks pass, proceed with returning
        
        # Increase quantity by 1
        book.update_quantity(book.quantity + 1)
        
        # Remove the book from the borrower's personal list
        borrower.remove_borrowed_book(book)
        
        print(f"Success: {borrower.name} returned '{book.title}'.")

    # --- Search & Display Functions ---

    def search_book(self, search_term, search_by="title"):
        """
        Searches for books by title, author, or genre.
        This is case-insensitive.
        """
        results = []
        search_term = search_term.lower() # Make search case-insensitive

        for book in self.books.values():
            if search_by == "title" and search_term in book.title.lower():
                results.append(book)
            elif search_by == "author" and search_term in book.author.lower():
                results.append(book)
            elif search_by == "genre" and search_term in book.genre.lower():
                results.append(book)
        
        # Display results
        if not results:
            print(f"No books found for '{search_term}' by {search_by}.")
        else:
            print(f"\n--- Search Results ({len(results)} found) ---")
            for book in results:
                # We use the handy __str__ method we defined in the Book class!
                print(book)
            print("-----------------------------")

    def show_all_books(self):
        """
        A helper function to display every book in the library.
        """
        if not self.books:
            print("The library has no books yet.")
            return
            
        print("\n--- All Books in Library ---")
        for book in self.books.values():
            print(book)
        print("----------------------------")

    def show_all_borrowers(self):
        """
        A helper function to display every registered borrower.
        """
        if not self.borrowers:
            print("There are no registered borrowers yet.")
            return
            
        print("\n--- All Registered Borrowers ---")
        for borrower in self.borrowers.values():
            print(borrower)
            # Also show what books they have
            borrower.print_borrowed_books()
        print("--------------------------------")