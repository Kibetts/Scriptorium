from sqlalchemy.orm import sessionmaker
from models import engine, User, Book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='Neema')
user2 = User(name='Jabez')

book1 = Book(title='To Kill a Mockingbird', author='Harper Lee', copies=5, created_at=datetime.now(), available=True)
book2 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', copies=9, created_at=datetime.now(), available=True)
book3 = Book(title='Pride and Prejudice', author='Jane Austen', copies=3, created_at=datetime.now(), available=True) 
book4 = Book(title='1984', author='George Orwell', copies=9, created_at=datetime.now(), available=True)
book5 = Book(title='The Catcher in the Rye', author='J.D. Salinger', copies=2, created_at=datetime.now(), available=True)
book6 = Book(title='The Lord of the Rings', author='J.R.R. Tolkien', copies=6, created_at=datetime.now(), available=True)