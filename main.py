from library import Library, Book, User, Author, Genre
from error_handling import *
import datetime
import re

def main_menu(library):
    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations(library)
        elif choice == '2':
            user_operations(library)
        elif choice == '3':
            author_operations(library)
        elif choice == '4':
            genre_operations(library)
        elif choice == '5':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations(library):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            borrow_book(library)
        elif choice == '3':
            return_book(library)
        elif choice == '4':
            search_book(library)
        elif choice == '5':
            library.display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book(library):
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        publication_date = get_valid_date_input("Enter book publication date (YYYY-MM-DD): ")
        library.add_book(Book(title, author, genre, publication_date))
    except Exception as e:
        handle_add_book_error(e)
def borrow_book(library):
    try:
        library_id_input = input("Enter user library ID: ")
        if not library_id_input.isdigit():
            raise ValueError("Library ID must be a number.")
        library_id = int(library_id_input)
        book_title = input("Enter the book title to borrow: ")
        library.borrow_book(library_id, book_title)
    except Exception as e:
        print(f"An error occurred while borrowing the book: {e}")

def return_book(library):
    try:
        library_id_input = input("Enter user library ID: ")
        if not library_id_input.isdigit():
            raise ValueError("Library ID must be a number.")
        library_id = int(library_id_input)
        book_title = input("Enter the book title to return: ")
        library.return_book(library_id, book_title)
    except Exception as e:
        print(f"An error occurred while returning the book: {e}")

def search_book(library):
    book_title = input("Enter the book title to search: ")
    book = next((b for b in library.books if b.get_title().lower() == book_title.lower()), None)
    if book:
        print(book)
    else:
        print("Book not found.")

def user_operations(library):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_user(library)
        elif choice == '2':
            view_user_details(library)
        elif choice == '3':
            library.display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user(library):
    try:
        name = input("Enter user name: ")
        email = get_valid_email_input("Enter user email: ")
        library.add_user(name, email)
    except Exception as e:
        print(f"An error occurred while adding the user: {e}")

def view_user_details(library):
    try:
        library_id_input = input("Enter user library ID: ")
        if not library_id_input.isdigit():
            raise ValueError("Library ID must be a number.")
        library_id = int(library_id_input)
        user = next((u for u in library.users if u._library_id == library_id), None)
        if user:
            print(user)
        else:
            print("User not found.")
    except Exception as e:
        print(f"An error occurred while viewing user details: {e}")

def author_operations(library):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_author(library)
        elif choice == '2':
            view_author_details(library)
        elif choice == '3':
            library.display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_author(library):
    try:
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        library.add_author(name, biography)
    except Exception as e:
        print(f"An error occurred while adding the author: {e}")

def view_author_details(library):
    try:
        name = input("Enter author name to view details: ")
        library.view_author_details(name)
    except Exception as e:
        print(f"An error occurred while viewing author details: {e}")

def genre_operations(library):
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_genre(library)
        elif choice == '2':
            view_genre_details(library)
        elif choice == '3':
            library.display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_genre(library):
    try:
        name = input("Enter genre name: ")
        description = input("Enter genre description: ")
        library.add_genre(name, description)
    except Exception as e:
        print(f"An error occurred while adding the genre: {e}")

def view_genre_details(library):
    try:
        name = input("Enter genre name to view details: ")
        library.view_genre_details(name)
    except Exception as e:
        print(f"An error occurred while viewing genre details: {e}")

def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def get_valid_email_input(prompt):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input(prompt)
        if re.match(email_pattern, email):
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

if __name__ == "__main__":
    library = Library()
    main_menu(library)
