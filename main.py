from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,  Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

#Tabelas do banco
class Motorista(Base):
    __tablename__ = "motoristas"


    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    avaliacao = Column(String(100), nullable=False)
    salario = Column(Float, nullable=False )

    viagem = relationship("Viagem", back_populates= "Motoristas")

    def __init__(self, nome ):
        self.nome = nome 


    def __repr__(self):
        return f"Motorista: id={self.id} - nome={self.nome}"

    
class Viagem(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    destino = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    categoria = Column(String(100), nullable=False)


    motorista_id = Column(Integer, ForeignKey("motoristas.id"))


        #relacionamento
    motorista = relationship("Motorista", back_populates= "Viagens")

    def __init__(self, nome, destino, preco, categoria):
        self.nome = nome 
        self.destino = destino
        self.preco = preco
        self.categoria = categoria
        

    def __repr__(self):
        return f"Viagens = id={self.id} - nome={self.nome} - destino={self.destino} - preco={self.preco} - categoria={self.categoria}"
    

engine = create_engine("sqlite:///corrida.db")


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

def cadastrar_motorista():

    nome = input("Digite o nome do motorista: ")
    destino = input("Digite o Destino: ")
    preco = input("Digite o Preço: ")
    categoria = input("Digite a cadegoria")
    with Session() as session:
        try:
            motoristas_existente = session.query(Motorista).filter_by(nome=nome, destino=destino).first()
            if motoristas_existente == None:
                novo_motorista = Motorista(nome, destino, preco, categoria)
                session.add(novo_motorista)
                session.commit()
            else:
                print(f"Já existe esse motorista!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro! {erro}")
        

    


    

