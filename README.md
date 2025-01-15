# Gerenciamento de Usuários com FastAPI

Este projeto é uma API REST desenvolvida com **FastAPI** para gerenciar usuários. A API permite realizar operações de CRUD (“Create, Read, Update, Delete”) em um banco de dados simulado, armazenado em memória. Os IDs dos usuários são gerados automaticamente e a aplicação inclui mensagens claras de sucesso e erro em suas respostas.

## Funcionalidades

1. **Cadastrar Usuários**
    - Adiciona um novo usuário ao sistema com os seguintes campos:
        - `ID` (gerado automaticamente)
        - `Nome`
        - `Email`
        - `Telefone`
    - Endpoint: `POST /users`

2. **Listar Usuários**
    - Retorna uma lista de todos os usuários cadastrados.
    - Endpoint: `GET /users`

3. **Editar Usuários**
    - Atualiza os campos de nome, email ou telefone de um usuário específico pelo ID.
    - Endpoint: `PUT /users/{user_id}`

4. **Remover Usuários**
    - Remove um usuário do sistema pelo ID.
    - Endpoint: `DELETE /users/{user_id}`

5. **Filtrar Usuários**
    - Permite buscar usuários filtrando por email ou telefone.
    - Endpoints:
        - `GET /users/filter?email={email}`
        - `GET /users/filter?telefone={telefone}`

## Tecnologias Utilizadas

- **Python** 3.9+
- **FastAPI**
- **Uvicorn**

## Como Executar o Projeto

### 1. Instalar Dependências
Certifique-se de que o Python está instalado no seu sistema. Em seguida, instale as dependências necessárias:

```bash
pip install fastapi uvicorn
```

### 2. Executar o Servidor

Salve o código da API em um arquivo chamado `main.py` e inicie o servidor com o comando:

```bash
uvicorn main:app --reload
```

### 3. Testar a API

Acesse a documentação interativa do FastAPI em:

```
http://127.0.0.1:8000/docs
```

Lá, você poderá testar todos os endpoints.

## Exemplos de Uso

### 1. Cadastrar um Novo Usuário
**Endpoint**: `POST /users`

**Corpo da Requisição** (JSON):
```json
{
  "nome": "João Silva",
  "email": "joao@example.com",
  "telefone": "11987654321"
}
```

**Resposta** (JSON):
```json
{
  "message": "Usuário cadastrado com sucesso!",
  "user": {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com",
    "telefone": "11987654321"
  }
}
```

### 2. Listar Todos os Usuários
**Endpoint**: `GET /users`

**Resposta** (JSON):
```json
{
  "message": "Lista de usuários recuperada com sucesso!",
  "users": [
    {
      "id": 1,
      "nome": "João Silva",
      "email": "joao@example.com",
      "telefone": "11987654321"
    }
  ]
}
```

### 3. Editar um Usuário
**Endpoint**: `PUT /users/{user_id}`

**Corpo da Requisição** (JSON):
```json
{
  "nome": "João Pedro Silva",
  "email": "joaopedro@example.com",
  "telefone": "11999887766"
}
```

**Resposta** (JSON):
```json
{
  "message": "Usuário atualizado com sucesso!",
  "user": {
    "id": 1,
    "nome": "João Pedro Silva",
    "email": "joaopedro@example.com",
    "telefone": "11999887766"
  }
}
```

### 4. Remover um Usuário
**Endpoint**: `DELETE /users/{user_id}`

**Resposta** (JSON):
```json
{
  "message": "Usuário removido com sucesso!",
  "user": {
    "id": 1,
    "nome": "João Pedro Silva",
    "email": "joaopedro@example.com",
    "telefone": "11999887766"
  }
}
```

### 5. Filtrar Usuários
**Endpoint**: `GET /users/filter?email=joaopedro@example.com`

**Resposta** (JSON):
```json
{
  "message": "Usuários filtrados com sucesso!",
  "users": [
    {
      "id": 1,
      "nome": "João Pedro Silva",
      "email": "joaopedro@example.com",
      "telefone": "11999887766"
    }
  ]
}
```


