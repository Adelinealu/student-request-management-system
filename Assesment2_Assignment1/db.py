from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Configure the database connection (replace with your database URL)
DB_URL = 'mysql+mysqlconnector://root:new password@localhost/security'

# Create the database engine
engine = create_engine(DB_URL)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define your database models (e.g., User, Request, Feedback)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)


class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category = Column(String(50), nullable=False)
    content = Column(String(255), nullable=False)
    feedbacks = relationship('Feedback', back_populates='request')

class Feedback(Base):
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True)
    facilitator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_id = Column(Integer, ForeignKey('requests.id'), nullable=False)
    content = Column(String(255), nullable=False)
    request = relationship('Request', back_populates='feedbacks')

# Create the database and tables
Base.metadata.create_all(engine)

if __name__ == '__main__':
    # Example: Create a new user
    session = Session()
    new_user = User(username='john_doe', password='password123')
    session.add(new_user)
    session.commit()
    session.close()
