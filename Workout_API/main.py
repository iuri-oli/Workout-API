from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from database import get_db, engine, Base
from models import AtletaModel, CategoriaModel, CentroTreinamentoModel
from schemas import AtletaIn, AtletaOut, AtletaUpdate, CategoriaIn, CategoriaOut, CentroTreinamentoIn, CentroTreinamentoOut

app = FastAPI(title="WorkoutAPI")

# Criar tabelas ao iniciar
Base.metadata.create_all(bind=engine)

# --- Rotas de Categorias ---
@app.post("/categorias", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
def create_categoria(categoria: CategoriaIn, db: Session = Depends(get_db)):
    db_categoria = CategoriaModel(nome=categoria.nome)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@app.get("/categorias", response_model=List[CategoriaOut])
def list_categorias(db: Session = Depends(get_db)):
    return db.query(CategoriaModel).all()

# --- Rotas de Centros de Treinamento ---
@app.post("/centros_treinamento", response_model=CentroTreinamentoOut, status_code=status.HTTP_201_CREATED)
def create_centro(centro: CentroTreinamentoIn, db: Session = Depends(get_db)):
    db_centro = CentroTreinamentoModel(**centro.model_dump())
    db.add(db_centro)
    db.commit()
    db.refresh(db_centro)
    return db_centro

@app.get("/centros_treinamento", response_model=List[CentroTreinamentoOut])
def list_centros(db: Session = Depends(get_db)):
    return db.query(CentroTreinamentoModel).all()

# --- Rotas de Atletas ---
@app.post("/atletas", response_model=AtletaOut, status_code=status.HTTP_201_CREATED)
def create_atleta(atleta: AtletaIn, db: Session = Depends(get_db)):
    # Verificar se categoria existe
    categoria = db.query(CategoriaModel).filter(CategoriaModel.nome == atleta.categoria.nome).first()
    if not categoria:
        raise HTTPException(status_code=400, detail=f"Categoria {atleta.categoria.nome} não encontrada")
    
    # Verificar se centro de treinamento existe
    centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.nome == atleta.centro_treinamento.nome).first()
    if not centro:
        raise HTTPException(status_code=400, detail=f"Centro de treinamento {atleta.centro_treinamento.nome} não encontrado")

    try:
        atleta_data = atleta.model_dump(exclude={'categoria', 'centro_treinamento'})
        db_atleta = AtletaModel(
            **atleta_data,
            categoria_id=categoria.pk_id,
            centro_treinamento_id=centro.pk_id
        )
        db.add(db_atleta)
        db.commit()
        db.refresh(db_atleta)
        return db_atleta
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=303, detail="Já existe um atleta cadastrado com este CPF")

@app.get("/atletas", response_model=List[AtletaOut])
def list_atletas(db: Session = Depends(get_db)):
    return db.query(AtletaModel).all()

@app.get("/atletas/{id}", response_model=AtletaOut)
def get_atleta(id: uuid.UUID, db: Session = Depends(get_db)):
    atleta = db.query(AtletaModel).filter(AtletaModel.id == id).first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return atleta

@app.patch("/atletas/{id}", response_model=AtletaOut)
def update_atleta(id: uuid.UUID, atleta_up: AtletaUpdate, db: Session = Depends(get_db)):
    db_atleta = db.query(AtletaModel).filter(AtletaModel.id == id).first()
    if not db_atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    update_data = atleta_up.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_atleta, key, value)
    
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

@app.delete("/atletas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_atleta(id: uuid.UUID, db: Session = Depends(get_db)):
    db_atleta = db.query(AtletaModel).filter(AtletaModel.id == id).first()
    if not db_atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    db.delete(db_atleta)
    db.commit()
    return None
