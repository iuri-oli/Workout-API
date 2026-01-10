from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated, Optional
from uuid import UUID

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True

class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID, Field(description='Identificador da categoria')]

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua X, 123', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Marcos', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID, Field(description='Identificador do centro de treinamento')]

class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678901', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaOut(AtletaIn):
    id: Annotated[UUID, Field(description='Identificador do atleta')]

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
