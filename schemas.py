def jogadorEntidade(db_item) -> dict:
    if not db_item:
        return {}
    return {
        "id": str(db_item['_id']),
        "nome": db_item['jogador_nome'],
        "numero": db_item['jogador_numero'],
        "time": db_item['jogador_time']
    }

def listaJogadoresEntidade(db_item) -> list:
    lista_jogadores = []
    for item in db_item:
        lista_jogadores.append(jogadorEntidade(item))
    return lista_jogadores