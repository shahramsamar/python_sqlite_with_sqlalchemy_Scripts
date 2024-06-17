from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL 
database_url ='sqlite:///my_database_sqlalchemy.db'

# create the engine
engine = create_engine(database_url, echo=True)

# Define the declarative base
base = declarative_base()

# define the user class
class User(base):
    __tablename__= 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
# create the table in the database
base.metadata.create_all(engine)

# create a configured "session" class
Session = sessionmaker(bind=engine)


# create a session
session = Session()

# example of how to add a new user
new_user = User(username='john', email='johnwick@gmail.com', password='securepassword')
session.add(new_user)
# session.commit()
    
    
# query the database
Users = session.query(User).all()   
for user in Users:
    print(user.id, user.username, user.email, user.password)
    