from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

DataBase = declarative_base()


class News(DataBase):
    __tablename__ = 'news_table'
    id = Column(Integer, primary_key=True)
    author = Column(String)
    post_text = Column(String)

    def __init__(self, author, post_text):
        self.author = author
        self.post_text = post_text

    def __repr__(self):
        return "<User('%s','%s')>" % (self.author, self.post_text)


class User(DataBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer)

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.surname, self.phone_number)


class Categories(DataBase):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    cat_name = Column(String)
    quantity_followers = Column(Integer)

    def __init__(self, cat_name, quantity_followers):
        self.cat_name = cat_name
        self.quantity_followers = quantity_followers

    def __repr__(self):
        return "<User('%s','%s')>" % (self.cat_name, self.quantity_followers)


DataBase.metadata.create_all(engine)
news_table = News.__table__
user_table = User.__table__
categories_table = Categories.__table__
metadata = DataBase.metadata

Session = sessionmaker(bind=engine)  # создаём подключение к бд
Session.configure(bind=engine)  # соединяем подключение к базе данных с сессией
session = Session()

post_1 = News("Егор Кириллов", "Я кирилл егоров вабщета")
session.add(post_1)
post_2 = News("Дмитрий Каракулов", "Пофиг, попозже")
session.add(post_2)
post_3 = News("Данил Харитулькин", "куцидаё дотера нани шока")
session.add(post_3)

user_1 = User("Buldozer", "Lama", "89349562718")
session.add(user_1)
user_2 = User("Stiv", "Broke", "89437483487")
session.add(user_2)
user_3 = User("Polyana", "Mellow", "89663654893")
session.add(user_3)

category_1 = Categories("Humor", 732746)
session.add(category_1)
category_2 = Categories("ICT", 546253)
session.add(category_2)
category_3 = Categories("physics", 523456)
session.add(category_3)
category_4 = Categories("math", 877552)
session.add(category_4)
category_5 = Categories("biology", 0)
session.add(category_5)

session.commit()
print(post_1.id)
