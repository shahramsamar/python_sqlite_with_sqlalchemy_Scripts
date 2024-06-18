from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker
import random
from pydantic import BaseModel, ConfigDict
# url for connecting to postgres db
# postgres://YourUserName:YourPassword@localHost:5432/YourDatabaseName
# mysql://YourUserName:YourPassword@localhost:3306/YourDatabaseName


# declaring database properties
engine = create_engine(f'sqlite:///mydatabase.db')

# Define the base class
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    
    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"
    
# Create all tables
Base.metadata.create_all(engine)


# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# data entry based on user model
# name_list = ["ali","shahram","mohamad","jafar","sasan"]
# for name in name_list:
#     new_user = User(name=name, age=random.randint(20,30))
#     session.add(new_user)    
# session.commit()

# query the database to find all users
# users = session.query(User).all()
# for user in users:
#     print(user)

# find based on the mathematic filter
# shahram = session.query(User).filter(User.name=="shahram").one() # all() # one_or_none()
# print(shahram)     


# find based on the mathematic filter
# users = session.query(User).filter(User.age >22,User.name.startswith("a")).all() # one() # one_or_none()

# un case sensetive
# users = session.query(User).filter(User.age >22,User.name.ilike("%a%")).all() # one() # one_or_none()

# case sensetive
# users = session.query(User).filter(User.age >22,User.name.like("%a%")).all() # one() # one_or_none()
# for user in users:
#     print(user)

# edith the name  attributes
# shahram = session.query(User).filter(User.id==4).one_or_none()
# shahram.name='shari'
# commit the changes to the database
# session.commit()


# shahram = session.query(User).filter(User.id==5).one_or_none()

# deleting the object from the session
# session.delete(shahram)

# commit the changes to the database
# session.commit()


    
    
# shahram = session.query(User).filter(User.id == 5).one_or_none()
   
# user_schema_obj = UserSchema.model_validate(shahram)     

# Query the user object from the database
class UserSchema(BaseModel):
    id :int
    name :str
    age:int
    
    model_config = ConfigDict(from_attributes=True)

# Query the user object from the database
user_from_db = session.query(User).filter(User.id == 5).one_or_none()

user_schema = UserSchema.model_validate(user_from_db)
print(user_schema.name)



# user_schema_obj = UserSchema(id=1,name="ali",age=30)
# print(user_schema_obj)
# print(user_schema_obj.model_json_schema())
# print(user_schema_obj.model_dump_json())
# print(user_schema_obj.model_dump())
# print(user_schema_obj.name)

