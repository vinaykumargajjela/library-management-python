# 📚 Simple Library Management System

This is a simplified, console-based library management system created as a technical challenge. It is built with Python and demonstrates core Object-Oriented Programming (OOP) principles.

## ✨ Core OOP Concepts Demonstrated

* **Encapsulation:** Data (like a book's `title` or a borrower's `name`) is bundled with the methods that operate on it (like `update_quantity()` or `update_contact()`).
* **Abstraction:** The main logic in `main.py` is simple. It just calls methods like `library.borrow_book()`. It doesn't need to know *how* the borrowing logic works, only that it *does* work.
* **Classes & Objects:** The system is built around "blueprints" (classes) for `Book`, `Borrower`, and the `Library` itself.
* **Data Structures:** This implementation intentionally uses **dictionaries** for storing books (keyed by ISBN) and borrowers (keyed by Membership ID). This provides fast $O(1)$ lookups, which is more efficient than searching through lists.

## 🚀 Features

* **Book Management:** Add, remove, and update the quantity of books.
* **Borrower Management:** Register, remove, and update borrower information.
* **Borrowing & Returning:**
    * Borrowers can check out available books.
    * Due dates are automatically set for 14 days.
    * Returning a book updates its available quantity.
* **Search & Availability:**
    * Search for books by title, author, or genre.
    * All book listings show the current quantity and availability status.
    * View all borrowers and the specific books they have checked out (including overdue status).

## 📁 Project Structure