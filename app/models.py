#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///scriptorium_base.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)

    borrowed_books = relationship('Borrow', back_populates='user')

class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    copies = Column(Integer)
    created_at = Column(TIMESTAMP)
    available = Column(Boolean)

class Request(Base):
    __tablename__ = 'requests'

    request_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    request_date = Column(TIMESTAMP)
    status = Column(String)

class Borrow(Base):
    __tablename__ = 'borrows'

    borrow_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    borrow_date = Column(TIMESTAMP)
    return_date = Column(TIMESTAMP)

# Create the database tables
Base.metadata.create_all(engine)