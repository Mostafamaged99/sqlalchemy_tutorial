from models import User, Group
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

# deleted_user = session.query(User).filter(User.id == 2).first()
# session.delete(deleted_user)
# session.commit()

#user_1 = User(uname="Omar", password="123456")
# session.add(user_1)
# session.commit()
# u1 = session.query(User).filter_by(id=1).first()

# # profile_1 = Profile(fname= "omar",lname = "ali", user = u1)
# # session.add(profile_1)
# # session.commit()
# # p1 = session.query(Profile).filter_by(id=1).first()
# print(u1.profile.fname)
# u1.profile.fname = "sara"
# u1.profile.lname = "omr"
# session.commit()
# session.delete(u1)
# session.commit()

# user_1 = User(uname="Omar")
# session.add(user_1)
# session.commit()
# u1 = session.query(User).filter_by(id=1).first()
# # print(u1)
# # posts = [
# #     {
# #         "title": "post 1",
# #         "content": "content 1"
# #     },
# #     {
# #         "title": "post 2",
# #         "content": "content 2"
# #     },
# #     {
# #         "title": "post 3",
# #         "content": "content 3"
# #     }
# # ]
# # for post_data in posts:
# #     post = Post(title=post_data["title"], content=post_data["content"], user=u1)
# #     session.add(post)
# #     session.commit()
# u1.posts[0].title = "new title 1"
# session.commit()
# session.delete(u1)
# session.commit()

# session.add_all([
#     User(uname="Omar"),
#     User(uname="Ahmed"),
#     User(uname="Sara"),
#     Group(g_name= "python"),
#     Group(g_name= "javascript"),
#     Group(g_name= "C++")
# ])
# session.commit()
u1 = session.query(User).filter_by(id=1).first()
u2 = session.query(User).filter_by(id=2).first()
u3 = session.query(User).filter_by(id=3).first()
g1 = session.query(Group).filter_by(id=1).first()
g2 = session.query(Group).filter_by(id=2).first()
g3 = session.query(Group).filter_by(id=3).first()
u1.groups.append(g1)
u1.groups.append(g2)
u1.groups.append(g3)
u2.groups.append(g3)
u3.groups.append(g2)
print(u1.groups)
session.commit()

