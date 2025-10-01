# FastAPI + MongoDB - CRUD de Jogadores ⚽

Este projeto é uma API REST construída com **FastAPI** e **MongoDB**, implementando um CRUD completo para gerenciamento de jogadores.

---

## 🚀 Tecnologias
- [FastAPI](https://fastapi.tiangolo.com/) (framework web)
- [MongoDB](https://www.mongodb.com/) (banco de dados NoSQL)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) (driver MongoDB para Python)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)

---

## ⚙️ Funcionalidades
- **GET** `/jogadores` → lista todos os jogadores
- **GET** `/jogadores/{id}` → busca jogador por ID
- **POST** `/jogadores` → cadastra novo jogador
- **PUT** `/jogadores/{id}` → atualiza jogador existente
- **DELETE** `/jogadores/{id}` → remove jogador do banco

---

## ▶️ Como rodar

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/fastapi-mongodb-crud.git
   cd fastapi-mongodb-crud  
   
2. Crie e ative um ambiente virtual:
  ```bash
  python -m venv venv
  venv\Scripts\activate      # Windows  

3. Instale as dependências:
  ```bash
  pip install -r requirements.txt  

4. Rode a aplicação:
  ```bash
  uvicorn main:app --reload


