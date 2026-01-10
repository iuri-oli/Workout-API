from sqlalchemy import Column, Integer, String, Float, ForeignKey, UUID
from sqlalchemy.orm import relationship
import uuid
from database import Base

class CategoriaModel(Base):
    __tablename__ = 'categorias'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    nome = Column(String(10), unique=True, nullable=False)
    
    atletas = relationship("AtletaModel", back_populates="categoria")

class CentroTreinamentoModel(Base):
    __tablename__ = 'centros_treinamento'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    nome = Column(String(20), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)
    
    atletas = relationship("AtletaModel", back_populates="centro_treinamento")

class AtletaModel(Base):
    __tablename__ = 'atletas'

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1), nullable=False)
    
    centro_treinamento_id = Column(Integer, ForeignKey('centros_treinamento.pk_id'), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.pk_id'), nullable=False)
    
    centro_treinamento = relationship("CentroTreinamentoModel", back_populates="atletas")
    categoria = relationship("CategoriaModel", back_populates="atletas")
