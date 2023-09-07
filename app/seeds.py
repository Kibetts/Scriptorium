from sqlalchemy.orm import sessionmaker
from models import engine, User, Book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()