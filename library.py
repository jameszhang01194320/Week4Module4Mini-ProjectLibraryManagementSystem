class Book:
    def __init__(self, title, author, genre, publication_date):
        self._title = title
        self._author = author
        self._genre = genre
        self._publication_date = publication_date
        self._is_borrowed = False

    def __str__(self):
        return f"{self.get_title()} by {self._author} ({self._genre}, {self._publication_date}) - {'Borrowed' if self._is_borrowed else 'Available'}"

    def get_title(self):
        return self._title

    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False

class User:
    def __init__(self, name, email, library_id):
        self._name = name
        self._email = email
        self._library_id = library_id
        self._borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed():
            self._borrowed_books.append(book)
            book.borrow()
        else:
            print(f"The book '{book.get_title()}' is already borrowed.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"The book '{book.get_title()}' is not borrowed by you.")

    def __str__(self):
        return f"Name: {self._name}, Email: {self._email}, Library ID: {self._library_id}, Borrowed Books: {[book.get_title() for book in self._borrowed_books]}"

class Author:
    def __init__(self, name, biography):
        self._name = name
        self._biography = biography

    def __str__(self):
        return f"{self._name}: {self._biography}"

class Genre:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __str__(self):
        return f"Genre: {self._name}, Description: {self._description}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, book):
        if any(b.get_title().lower() == book.get_title().lower() for b in self.books):
            print(f"A book with the title '{book.get_title()}' already exists.")
        else:
            self.books.append(book)
            print(f"Book '{book.get_title()}' added successfully.")

    def display_all_books(self):
        if not self.books:
            print("No books found in the library.")
        else:
            for book in self.books:
                print(book)

    def add_user(self, name, email):
        if any(u._email.lower() == email.lower() for u in self.users):
            print(f"A user with the email '{email}' already exists.")
        else:
            library_id = len(self.users) + 1
            user = User(name, email, library_id)
            self.users.append(user)
            print(f"User '{name}' added successfully with library ID {library_id}.")

    def display_all_users(self):
        if not self.users:
            print("No users found in the library.")
        else:
            for user in self.users:
                print(user)

    def add_author(self, name, biography):
        if any(a._name.lower() == name.lower() for a in self.authors):
            print(f"An author with the name '{name}' already exists.")
        else:
            author = Author(name, biography)
            self.authors.append(author)
            print(f"Author '{name}' added successfully.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors found in the library.")
        else:
            for author in self.authors:
                print(author)

    def view_author_details(self, name):
        for author in self.authors:
            if author._name.lower() == name.lower():
                print(author)
                return
        print("Author not found.")

    def add_genre(self, name, description):
        if any(g._name.lower() == name.lower() for g in self.genres):
            print(f"A genre with the name '{name}' already exists.")
        else:
            genre = Genre(name, description)
            self.genres.append(genre)
            print(f"Genre '{name}' added successfully.")

    def display_all_genres(self):
        if not self.genres:
            print("No genres found in the library.")
        else:
            for genre in self.genres:
                print(genre)

    def view_genre_details(self, name):
        for genre in self.genres:
            if genre._name.lower() == name.lower():
                print(genre)
                return
        print("Genre not found.")

    def borrow_book(self, user_library_id, book_title):
        user = next((u for u in self.users if u._library_id == user_library_id), None)
        if user is None:
            print("User not found.")
            return

        book = next((b for b in self.books if b.get_title().lower() == book_title.lower()), None)
        if book is None:
            print("Book not found.")
            return

        if book.is_borrowed():
            print(f"The book '{book.get_title()}' is already borrowed.")
        else:
            user.borrow_book(book)
            print(f"Book '{book.get_title()}' borrowed successfully by user '{user._name}'.")

    def return_book(self, user_library_id, book_title):
        user = next((u for u in self.users if u._library_id == user_library_id), None)
        if user is None:
            print("User not found.")
            return

        book = next((b for b in user._borrowed_books if b.get_title().lower() == book_title.lower()), None)
        if book is None:
            print("Book not found or not borrowed by user.")
            return

        user.return_book(book)
        print(f"Book '{book.get_title()}' returned successfully by user '{user._name}'.")
