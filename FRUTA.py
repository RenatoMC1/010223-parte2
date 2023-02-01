import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = db.create_engine("mysql+pymysql://root:@localhost:3306/aula02")

Base = declarative_base()

class Frutas(Base):
    __tablename__ = 'frutas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    corprincipal = Column(String(60))

Base.metadata.create_all(engine)

'''frutas = []

for i in range(1,4):
    nomefruta = input(f"Digite o nome {i}° da fruta: ")
    corfruta = input(f"Digite a cor principal da {i}° fruta: ")
    f1 = Frutas(nome=nomefruta, corprincipal=corfruta)
    frutas.append(f1)'''

Session = sessionmaker(bind=engine)
session = Session()

'session.add_all([ frutas[0], frutas[1], frutas[2] ])'

session.commit()

'''consulta = session.query(Frutas).all()

for fruta in consulta:
    print(fruta.id, fruta.nome, fruta.corprincipal)'''