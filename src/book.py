# src/book.py

class Book:
    """
    This class represents a single Book in the library.
    
    Think of this as the "blueprint" for creating book objects.
    Each book object will have its own title, author, etc.
    """
    
    def __init__(self, title, author, isbn, genre, quantity):
        """
        This is the "constructor" method. It runs when we create a new Book object.
        It sets up all the book's properties.
        """
        self.title = title
        self.author = author
        self.isbn = isbn  # ISBN is the unique ID for a book
        self.genre = genre
        self.quantity = quantity
        self.available = quantity > 0  # A simple boolean to see if it's in stock

    def update_quantity(self, new_quantity):
        """
        A safe way to update the book's quantity.
        It also automatically updates the 'available' status.
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
            self.available = self.quantity > 0
        else:
            print(f"Error: Quantity cannot be negative for '{self.title}'.")

    def __str__(self):
        """
        This is a "magic method" that provides a human-readable string
        when we try to 'print()' a Book object. Super useful for debugging!
        """
        status = "Available" if self.available else "Out of Stock"
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
                f"Genre: {self.genre}, Quantity: {self.quantity} ({status})")