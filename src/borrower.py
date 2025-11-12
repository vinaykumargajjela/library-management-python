# src/borrower.py
from datetime import date

class Borrower:
    """
    This class represents a single Borrower (library member).
    
    This blueprint holds their personal info and a list of books
    they've currently borrowed.
    """
    
    def __init__(self, name, contact, membership_id):
        """
        The constructor for a Borrower.
        """
        self.name = name
        self.contact = contact
        self.membership_id = membership_id  # Unique ID for the borrower
        
        # This list will store tuples of (book, due_date)
        self.borrowed_books = [] 

    def update_contact(self, new_contact):
        """
        A simple method to update the borrower's contact info.
        """
        self.contact = new_contact
        print(f"Contact updated for {self.name} to {self.contact}.")

    def add_borrowed_book(self, book, due_date):
        """
        Adds a book and its due date to the borrower's personal list.
        """
        self.borrowed_books.append({"book_isbn": book.isbn, "due_date": due_date})

    def remove_borrowed_book(self, book):
        """
        Removes a book from the borrower's list when they return it.
        We find the book by its ISBN.
        """
        book_to_remove = None
        for record in self.borrowed_books:
            if record["book_isbn"] == book.isbn:
                book_to_remove = record
                break
        
        if book_to_remove:
            self.borrowed_books.remove(book_to_remove)
        else:
            # This is a safety check, should ideally not happen if logic is correct
            print(f"Error: {self.name} does not seem to have borrowed {book.title}.")

    def __str__(self):
        """
        A human-readable string for printing a Borrower object.
        """
        return f"Member: {self.name}, ID: {self.membership_id}, Contact: {self.contact}"
    
    def print_borrowed_books(self):
        """
        A helper to show all books currently borrowed by this person.
        """
        if not self.borrowed_books:
            print(f"{self.name} has no books borrowed.")
            return

        print(f"\n--- Books borrowed by {self.name} ---")
        today = date.today()
        for record in self.borrowed_books:
            status = "OVERDUE" if record['due_date'] < today else "On time"
            print(f"  - ISBN: {record['book_isbn']}, Due: {record['due_date']} ({status})")
        print("---------------------------------")