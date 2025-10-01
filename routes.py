from fastapi import APIRouter, HTTPException
from database import db
from models import Jogador
from schemas import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId

router = APIRouter()

@router.get("/")
def inicio():
    return "Bem-vindo à página oficial!"

@router.get("/jogadores")
def lista_jogadores():
    jogadores = db["jogadores"].find()
    return listaJogadoresEntidade(jogadores)

@router.get("/jogadores/{jogador_id}")
def busca_jogador(jogador_id: str):
    if not ObjectId.is_valid(jogador_id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    jogador = db["jogadores"].find_one({"_id": ObjectId(jogador_id)})

    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogadorEntidade(jogador)

@router.post("/jogadores")
def cadastra_jogador(jogador: Jogador):
    resultado = db["jogadores"].insert_one(jogador.dict())
    jogador_inserido = db["jogadores"].find_one({"_id": resultado.inserted_id})
    return jogadorEntidade(jogador_inserido)

@router.put("/jogadores/{jogador_id}")
def atualiza_jogador(jogador_id: str, jogador: Jogador):
    if not ObjectId.is_valid(jogador_id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    resultado = db["jogadores"].find_one_and_update(
        {"_id": ObjectId(jogador_id)},
        {"$set": jogador.dict()},
        return_document = True
    )
    if not resultado:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogadorEntidade(resultado)

@router.delete("/jogadores/{jogador_id}")
def delete_jogador(jogador_id: str):
    if not ObjectId.is_valid(jogador_id):
        raise HTTPException(status_code=400, detail="ID inválido")

    jogador = db["jogadores"].find_one_and_delete({"_id": ObjectId(jogador_id)})

    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogadorEntidade(jogador)