from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Estrutura do Usuário
class User(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

# Banco de dados simulado
users = []
next_id = 1  # ID inicial gerado automaticamente

# 1. Cadastro de Usuários
@app.post("/users", response_model=dict)
def cadastrar_usuario(nome: str, email: str, telefone: str):
    global next_id
    novo_usuario = User(id=next_id, nome=nome, email=email, telefone=telefone)
    users.append(novo_usuario)
    next_id += 1
    return {"message": "Usuário cadastrado com sucesso!", "user": novo_usuario}

# 2. Listar Usuários
@app.get("/users", response_model=dict)
def listar_usuarios():
    if not users:
        return {"message": "Nenhum usuário cadastrado no sistema.", "users": []}
    return {"message": "Lista de usuários recuperada com sucesso!", "users": users}

# 3. Editar Usuários
@app.put("/users/{user_id}", response_model=dict)
def editar_usuario(user_id: int, nome: Optional[str] = None, email: Optional[str] = None, telefone: Optional[str] = None):
    for user in users:
        if user.id == user_id:
            if nome:
                user.nome = nome
            if email:
                user.email = email
            if telefone:
                user.telefone = telefone
            return {"message": "Usuário atualizado com sucesso!", "user": user}
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")

# 4. Remover Usuários
@app.delete("/users/{user_id}", response_model=dict)
def remover_usuario(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "Usuário removido com sucesso!", "user": user}
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")

# 5. Filtrar Usuários
@app.get("/users/filter", response_model=dict)
def filtrar_usuarios(email: Optional[str] = Query(None), telefone: Optional[str] = Query(None)):
    resultados = [user for user in users if (email and user.email == email) or (telefone and user.telefone == telefone)]
    if not resultados:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado com os filtros fornecidos.")
    return {"message": "Usuários filtrados com sucesso!", "users": resultados}
