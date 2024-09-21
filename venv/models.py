from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from db import engine, Base

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     uname = Column(String(20), nullable=False, unique=True)
#     password = Column(String(20), nullable=False)
#     profile = relationship("Profile", backref="user", uselist=False, cascade="all, delete, save-update")
#     def __repr__(self) -> str:  
#         return f"Hello, {self.uname}!)"
    
# class Profile(Base):
#     __tablename__ = "profiles"
#     id = Column(Integer, primary_key=True)
#     fname = Column(String(20))
#     lname = Column(String(20))
#     user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE", onupdate = "CASCADE"))
#     def __repr__(self) -> str:
#         return f"Hello, {self.fname} {self.lname}!"

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     uname = Column(String(30), nullable=False, unique=True)
#     posts = relationship("Post", back_populates="user", cascade="all, delete, save-update")
#     def __repr__(self) -> str:
#         return f"Hello, {self.uname}!"
    
# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(50), nullable=False)
#     content = Column(String(255), nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate = "CASCADE"))
#     user = relationship("User", back_populates="posts")

group_user = Table(
    "group_users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True),
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uname = Column(String(30), nullable=False, unique=True)
    groups = relationship("Group", secondary=group_user, back_populates="users")
    def __repr__(self) -> str:
        return f"Hello, {self.uname}!"
    
class Group(Base): 
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    g_name = Column(String(30), nullable=False)
    users = relationship("User", secondary=group_user, back_populates= "groups")
    def __repr__(self) -> str:
        return f"Hello, {self.g_name}!"

Base.metadata.create_all(bind = engine)