import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = db.create_engine("mysql+pymysql://root@localhost:3306/aula02")

Base = declarative_base()

class Friends(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    personagem = Column(String(60))

Base.metadata.create_all(engine)

p1 = Friends(nome="Jennifer Aniston", personagem="Rachel Green")
p2 = Friends(nome="Courteney Cox", personagem="Monica Geller")
p3 = Friends(nome="Lisa Kudrow", personagem="Phoebe Buffay")
p4 = Friends(nome="Matt LeBlanc", personagem="Joey Tribbiani")
p5 = Friends(nome="Matthew Perry", personagem="Chandler Bing")
p6 = Friends(nome="David Schwimmer", personagem="Ross Geller")

Session = sessionmaker(bind=engine)
session = Session()

session.add(p1)
session.add_all([p2, p3, p4, p5, p6])

session.commit()