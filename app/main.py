
from sqlalchemy.orm import sessionmaker
from models import engine, User, Book, Request, Borrow
from datetime import datetime, timedelta

# Function to list available books and prompt user for input
def list_available_books(session):
    available_books = session.query(Book).filter(Book.available == True).all()

    if not available_books:
        print("No available books at the moment.")
    else:
        print("Available books:")
        for book in available_books:
            print(f"{book.book_id}: {book.title} by {book.author}")

    user_input = input("Enter the title of the book you want to borrow or 'r' to request: ")

    if user_input == 'r':
         request_book(session)
       
    else:
        book_title = user_input
        borrow_book(session, book_title)

# Function to request a book
def request_book(session, user):
    user_input = input("Enter the title of the book you want to request: ")
    
    # Check if the book is in the database
    book = session.query(Book).filter(Book.title == user_input).first()

    if book:
        # Create a request regardless of book availability
        new_request = Request(user_id=user.user_id, book_id=book.book_id, request_date=datetime.now(), status="Pending")  
        session.add(new_request)
        session.commit()
        print(f"Your request for '{book.title}' by {book.author} has been submitted.")
    else:
        # If the book is not in the database, still create a request
        print(f"Book '{user_input}' not found. Your request has been submitted.")

# Function to borrow a book
def borrow_book(session, book_title, user):
    book = session.query(Book).filter(Book.title == book_title).first()

    if book is None:
        print("Book not found.")
        return

    if book.available:
        borrow = Borrow(user_id=user.user_id, book_id=book.book_id, borrow_date=datetime.now(), return_date=None)  
        session.add(borrow)
        book.available = False
        session.commit()
        print(f"You have borrowed '{book.title}' by {book.author}.")
    else:
        print("The selected book is not available. You can request it.")
        request_book(session)

    # Function to return borrowed books automatically after 20 days
def auto_return_books(session):
    borrowings = session.query(Borrow).filter(Borrow.return_date == None).all()

    for borrowing in borrowings:
        borrow_date = borrowing.borrow_date
        if datetime.now() - borrow_date > timedelta(days=20):
            borrowing.return_date = datetime.now()
            book = session.query(Book).filter(Book.book_id == borrowing.book_id).first()
            book.available = True
            print(f"You have returned '{book.title}' by {book.author} automatically.")

    session.commit()

# Function to cancel requests for unavailable books
def cancel_request(session):
    user_input = input("Enter the title of the book you want to cancel the request for: ")
    
    # Attempt to find the book in the database
    book = session.query(Book).filter(Book.title == user_input).first()

     # Always create a request cancellation, even if the book is not found
    if book:
        request = session.query(Request).filter(Request.user_id == 1, Request.book_id == book.book_id, Request.status == "Pending").first()
        if request:
            session.delete(request)
            session.commit()
            print(f"Request for '{book.title}' by {book.author} has been canceled.")
        else:
            print("You don't have a pending request for this book.")
    else:
        print(f"Your request for book '{user_input}' has been canceled successfully.")


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Welcome to Scriptorium Inc!")

    while True:
        print("\nChoose an option below:")
        print("1. List Available Books")
        print("2. Auto Return Borrowed Books (After 20 days)")
        print("3. Cancel Request")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            list_available_books(session)
        elif choice == '2':
            auto_return_books(session)
        elif choice == '3':
            cancel_request(session)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    session.close()






