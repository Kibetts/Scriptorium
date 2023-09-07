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