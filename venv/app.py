from models import User
from sqlalchemy.orm import sessionmaker
from db import engine

session = sessionmaker(bind=engine)()

# user_one = User(name="John")
# user_two = User(name="Jane")
# user_three = User(name="Joe")

# session.add_all([user_one, user_two, user_three])

# session.commit()

# users = session.query(User).all()
# user = session.query(User).filter(User.id == 3).first()

# print(user)
# print(len(users))

# updated_user = session.query(User).filter(User.id == 1).first()
# updated_user.name = "Omar"
# session.commit()
# print(updated_user)

deleted_user = session.query(User).filter(User.id == 2).first()
session.delete(deleted_user)
session.commit()
