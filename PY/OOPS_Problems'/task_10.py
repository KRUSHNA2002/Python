class Book:

    def __init__(self,book_id,title,author,available=True):

        self.book_id=book_id
        self.title=title
        self.author=author
        self.available=available
    
class Library:

    def __init__(self):
        self.books=[]
        
    def add_book(self,book):        
        self.books.append(book)

    def show_book(self):
        for book in self.books:
            print(f"{book.book_id} {book.title} {book.author} {'Book is available ' if book.available else 'Book is not available'}")



class User:

    def __init__(self,name):
        self.name=name
        self.borrowed_books = []

    def issue_book(self, library, book_id):
        for book in library.books:
            if book_id == book.book_id:
                if book.available:  # check if book is available
                    book.available = False  # mark as borrowed
                    self.borrowed_books.append(book)  # store the book object
                    print(f"Book '{book.title}' issued successfully")
                    return
                else:
                    print("Book is not available")
                    return
        print("Book ID not found")

    def return_book(self, book_id):
        for book in self.borrowed_books:
            if book_id == book.book_id:
                    book.available = True
                    self.borrowed_books.remove(book)
                    print(f"Book '{book.title}' returned successfully")
                    return
                    
        print("Book ID not found")

book1=Book(1,"Biology","Krushna")
book2=Book(2,"Math","Krushna",False)

lab=Library()

lab.add_book(book1)
lab.add_book(book2)

lab.show_book()
user1=User("Amit")
user1.issue_book(lab,1)
lab.show_book()

user1.issue_book(lab,2)
lab.show_book()
user1.return_book(1)
lab.show_book()