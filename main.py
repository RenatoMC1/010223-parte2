import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = db.create_engine("mysql+pymysql://root:@localhost:3306/aula02")

Base = declarative_base()

class Friends(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    personagem = Column(String(60))

Base.metadata.create_all(engine)

p1 = Friends(nome='Matt LeBlanc',personagem='Joey Tribbiani')
p2 = Friends(nome='Lisa Kudrow',personagem='Phoebe Buffay')
p3 = Friends(nome='Courteney Cox',personagem= 'Monica Geller')
p4 = Friends(nome='Jennifer Aniston',personagem='Rachel Green')
p5 = Friends(nome='David Schwimmer',personagem='Ross Geller')
p6 = Friends(nome='Matthew Perry',personagem='Chandler Bing')

Session = sessionmaker(bind=engine)
session = Session()

#session.add(p1)
#session.add_all([p2,p3,p4,p5,p6])

#session.commit()

consulta = session.query(Friends).filter(Friends.id == 1).first()
consulta.nome = "Rita Lee"
session.delete(consulta)
session.commit()



