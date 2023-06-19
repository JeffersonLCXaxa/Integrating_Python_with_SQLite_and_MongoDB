# Implementing SQLite integration using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String, Binary, Decimal
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create a connection to the SQLite database
engine = create_engine('sqlite:///database.db', echo=True)

# Create the base class for table definitions
Base = declarative_base()

# Client class
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))
    contas = relationship('Conta')

# Account class
class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Binary, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Decimal)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a minimal set of data for manipulation
cliente1 = Cliente(nome='João', cpf='123456789', endereco='Rua A')
cliente2 = Cliente(nome='Maria', cpf='987654321', endereco='Rua B')

conta1 = Conta(tipo='Corrente', agencia='001', num=123, saldo=1000)
conta2 = Conta(tipo='Poupança', agencia='002', num=456, saldo=5000)

cliente1.contas.append(conta1)
cliente2.contas.append(conta2)

session.add_all([cliente1, cliente2])
session.commit()

# Execute data retrieval methods
# Example: Retrieve all clients
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'ID: {cliente.id}, Name: {cliente.nome}, CPF: {cliente.cpf}, Address: {cliente.endereco}')
    for conta in cliente.contas:
        print(f'    Account - Type: {conta.tipo}, Agency: {conta.agencia}, Number: {conta.num}, Balance: {conta.saldo}')
