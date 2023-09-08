from sqlalchemy.orm import sessionmaker
from models import engine, User, Book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='Neema')
user2 = User(name='Jabez')
user2 = User(name='Robert')
user2 = User(name='Faith')
user2 = User(name='Collins')
user2 = User(name='Ammon')
user2 = User(name='Jurgen')
user2 = User(name='Ian')


book1 = Book(title='To Kill a Mockingbird', author='Harper Lee', copies=5, created_at=datetime.now(), available=True)
book2 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', copies=9, created_at=datetime.now(), available=True)
book3 = Book(title='Pride and Prejudice', author='Jane Austen', copies=3, created_at=datetime.now(), available=True) 
book4 = Book(title='1984', author='George Orwell', copies=9, created_at=datetime.now(), available=True)
book5 = Book(title='The Catcher in the Rye', author='J.D. Salinger', copies=2, created_at=datetime.now(), available=True)
book6 = Book(title='The Lord of the Rings', author='J.R.R. Tolkien', copies=6, created_at=datetime.now(), available=True)
book7 = Book(title='One Hundred Years of Solitude', author='Gabriel García Márquez', copies=8, created_at=datetime.now(), available=True)
book8 = Book(title='The Diary of Anne Frank', author='Anne Frank', copies=3, created_at=datetime.now(), available=True)
book9 = Book(title='The Book Thief', author='Markus Zusak', copies=3, created_at=datetime.now(), available=True)
book10 = Book(title='The Kite Runner', author='Khaled Hosseini', copies=12, created_at=datetime.now(), available=True)
book11 = Book(title='Beloved', author='Toni Morrison', copies=10, created_at=datetime.now(), available=True)
book12 = Book(title='The Hunger Games', author='Suzanne Collins', copies=6, created_at=datetime.now(), available=True)
book13 = Book(title='The Handmaid\'s Tale', author='Margaret Atwood', copies=5, created_at=datetime.now(), available=True)
book14 = Book(title='The Girl with the Dragon Tattoo', author='Stieg Larsson', copies=17, created_at=datetime.now(), available=True)
book15 = Book(title='The Grapes of Wrath', author='John Steinbeck', copies=6, created_at=datetime.now(), available=True)

# Add instances to the session and commit
session.add_all([user1, user2, book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15])
session.commit()

# Close the session when done
session.close()