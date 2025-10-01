from pydantic import BaseModel

class Jogador(BaseModel):
    jogador_nome: str
    jogador_numero: int
    jogador_time: str