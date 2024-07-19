import re

class Genre:
    def __init__(self):
        self.genre = {}

    def genre_menu(self):
        genre_choice = input("Enter a specific number for the action you'd like to take for Genre Operations:\n1. Add a new genre\n2. View genre details\n3. Display all genres\n")
        if genre_choice == '1':
            self.add_genre()
        elif genre_choice == '2':
            self.view_genre()
        elif genre_choice == '3':
            self.display_genre()
        else:
            print('Please enter a valid choice')

    def add_genre(self):
        genre_name = input("What genre would you like to add?").lower()
        genre_description = input("Give a brief description of the genre")
        genre_category = input("What is the genre categorized as? (Fiction, Non-Fiction, Poetry etc)")
        self.genre[genre_name] = {'Description': genre_description, 'Category': genre_category}
        print(f'The genre: {genre_name} has been added to our files!')

    def view_genre(self):
        search = input("Enter the name of the genre you'd like to find information about").lower()
        if search in self.genre:
            genre_details = self.genre[search]
            print(f'Here are the details of the genre you were looking into:\nName: {search}\nCategory: {genre_details["Category"]}\nDescription: {genre_details["Description"]}')

    def display_genre(self):
        if self.genre:
            print(f'Here is the list of genres we have on file:')
            for name, details in self.genre.items():
                print(f'Name: {name}\nCategory: {details["Category"]}\nDescription: {details["Description"]}\n')
        else:
            print('\nNo genres found in the database\n')

            
class Book(Genre):
    def __init__(self):
        super().__init__()
        self.books = {}


    def book_menu(self):
        choice = input("Enter a specific number for the action you'd like to take for Book Operations:\n1. Add a new book\n 2. Borrow a book\n 3. Return a book\n 4. Search for a book\n 5. Display all books")
        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.borrow()
        elif choice == '3':
            self.return_book()
        elif choice == '4':
            self.search()
        elif choice == '5':
            self.display_all()
        else:
            print('Please enter a valid choice')
            
    
    def add_book(self):
        try:
            book = input("What book would you like to add to the library?").strip()
            if not book:
                raise ValueError("Title cannot be empty.")
            author = input("Who is the author of this book?").strip()
            if not author:
                raise ValueError("Author cannot be empty.")
            
            isbn = input("What is ISBN number of this book").strip()
            if not re.match(r'^\d{3}-\d{10}$', isbn):
                raise ValueError("Invalid ISBN format. Use XXX-XXXXXXXXXX.")
            
            publication = input('When was this book published?').strip()
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', publication):
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")

            genre_name = input("Enter genre name: ").strip()
            genre_description = input("Enter genre description: ").strip()
            genre_category = input("Enter genre category: ").strip()

            if genre_name not in self.genre:
                self.genre[genre_name] = {'Description': genre_description, 'Category': genre_category}


            available = True
            self.books[book] = {
                'Author': author,
                'ISBN':isbn,
                'Availability':available, 
                'Publication Date': publication, 
                'Genre': genre_name
            }

            print(f'You have added {book} to the library')
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def borrow(self):
        book_borrow = input("What book would you like to borrow?")
        if book_borrow in self.books and self.books[book_borrow]['Availability']:
            self.books[book_borrow]['Availability'] = False
            print(f'You have borrowed {book_borrow}')
        else:
            print(f'The book: {book_borrow} does not exist in our library or is currently unavailable!')
        

    def return_book(self):
        book_return = input("What book are you returning?")
        if book_return in self.books:
            self.books[book_return]['Availability'] = True
            print(f"Thank you for returning {book_return} to us!")
        else:
            print(f'The book: {book_return} does not exist in our library or is currently unavailable!')
    

    def search(self):
        pattern = r'^\d{13}$'
        book_option = input('Would you like to search for a book by its ISBN or the Title?(Input Title/ISBN)').lower()
        book_search_id = ''
        if book_option == 'title':
            book_search = input("Enter the title of the book you are looking for")
            if book_search in self.books:
                print(f'The book: {book_search} has been located!')
                print(self.books[book_search])
            else:
                print("We could not find the book you are looking for!")
        elif book_option == 'isbn':
            book_search_id = input('Enter the 13 digit ISBN of the book you are looking for')
            if re.match(pattern, book_search_id):
                if book_search_id in self.books:
                    print(f'The book: {book_search_id} has been located!')
                    print(self.books[book_search_id])
                else:
                    print("We could not find the book you are looking for!")
            else:
                print('Please enter a valid ISBN number')
        else:
            print('Invalid option. Please input "Title" or "ISBN.')

    def display_all(self):
        if self.books:
            for book, details in self.books.items():
                availability = 'Available' if details['Availability'] else 'Not Available'
                print(f'Book: {book}\nAuthor: {details["Author"]}\nISBN: {details["ISBN"]}\nPublication Date: {details["Publication Date"]}\nGenre: {details["Genre"]}\nAvailability: {availability}\n')
        else:
            print('No books available currently')




class User:
    def __init__(self):
        self.users = {}

    def user_menu(self):
        user_choice = input("Enter a specific number for the action you'd like to take for User Operations:\n1. Add a new user\n2. Search for a user\n3. Display all users\n")
        if user_choice == '1':
            self.add_user()
        elif user_choice == '2':
            self.search_user()
        elif user_choice == '3':
            self.display_all_users()
        else:
            print('Please enter a valid choice')


    def add_user(self):
        name = input("What is your first and last name?")
        __id = input("Enter a random 8 digit number sequence")

        try:
            self.set_user_id(__id)
        except ValueError as e:
            print(e)
            return
        
        if self.get_user_by_id(__id) in self.users:
            print("The User ID is already taken, please enter a different one")
            return
        
        self.users[__id] = {'Name': name, 'Library ID': __id, 'Borrowed Books': 'N/A'}
        print(f'User {name} has been added successfully!')

    def search_user(self):
        search = input('Enter your User ID to find your details')
        user = self.get_user_by_id(search)
        if user:
            print(f'Here are your account details: {user}')
        else:
            print('User not found!')

    def display_all_users(self):
        if self.users:
            print(f'Here are all our current users in the database:')
            for user_id, details in self.users.items():
                print(f'{user_id}: {details}')
        else:
            print('No users found in the database')

    def get_user_id(self):
        return self._user_id
    
    def set_user_id(self, __id):
        pattern = r'^\d{8}$'
        if not re.match(pattern, __id):
            raise ValueError('Please Enter a valid ID number')
        self._user_id = __id

    def get_user_by_id(self, __id):
        return self.users.get(__id)
                

class Author:
    def __init__(self):
        self.author = {}

    def author_menu(self):
        author_choice = input("Enter a specific number for the action you'd like to take for Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\n")
        if author_choice == '1':
            self.add_author()
        elif author_choice == '2':
            self.view_author()
        elif author_choice == '3':
            self.display_authors()
        else:
            print('Please enter a valid choice')


    def add_author(self):
        name = input("Who is the author you'd like to add").lower()
        biography = input("Enter his biography here")
        self.author[name] = biography
        print(f'The author {name} has been added!')

    def view_author(self):
        find = input("Enter the name of the author you'd like to find information about").lower()
        if find in self.author:
            print(f'Here are the details about the author you wanted to find: {find}:\n {self.author[find]}')

    def display_authors(self):
        if self.author:
            print(f'Here is the list of our current authors:')
            for name, biography in self.author.items():
                print(f'Name: {name}\n Biography: {biography}\n')
        else:
            print('No authors found in the database')









class MainMenu:

    def __init__(self):
        self.book = Book()
        self.user = User()
        self.author = Author()
        self.genre = Genre()


    def start_app(self):
        while True:
            main_choice = input("Welcome to the new Library Management System!\nEnter a specific number to navigate the Main Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Exit\n")
            if main_choice == '1':
                self.book.book_menu()
            elif main_choice == '2':
                self.user.user_menu()
            elif main_choice == '3':
                self.author.author_menu()
            elif main_choice == '4':
                self.genre.genre_menu()
            elif main_choice == '5':
                print("Exiting the Library Management System. Thank you!")
                break
            else:
                print("Please enter a valid choice")

if __name__ == '__main__':
    ui = MainMenu()
    ui.start_app()




        

