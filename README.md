# Workout-API

Este repositório contém uma API RESTful desenvolvida com FastAPI para gerenciar categorias de treino, centros de treinamento e atletas. A API permite a criação, listagem, recuperação, atualização e exclusão de dados relacionados a esses modelos.

## Estrutura do Projeto

O projeto está organizado na seguinte estrutura de diretórios:

- `Workout_API/main.py`: Contém a aplicação FastAPI principal e as definições de rotas.
- `Workout_API/models.py`: Define os modelos de banco de dados SQLAlchemy para Categorias, Centros de Treinamento e Atletas.
- `Workout_API/schemas.py`: Define os schemas Pydantic para validação de dados de entrada e serialização de saída.
- `Workout_API/database.py`: Configura a conexão com o banco de dados e fornece uma sessão de banco de dados.
- `Workout_API/requirements.txt`: Lista todas as dependências Python necessárias para o projeto.

## Tecnologias Utilizadas

- **FastAPI**: Framework web de alta performance para construir APIs.
- **SQLAlchemy**: Toolkit SQL e Object-Relational Mapper (ORM) para interagir com o banco de dados.
- **Pydantic**: Biblioteca para validação de dados e gerenciamento de configurações usando type hints Python.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **SQLite**: Banco de dados leve e baseado em arquivo (configuração padrão).

## Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Criar e Ativar um Ambiente Virtual

É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

```bash
python -m venv .venv
venv\Scripts\activate  # No Windows
# source venv/bin/activate  # No Linux/macOS
```

### 3. Instalar as Dependências

Instale todas as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

Inicie o servidor Uvicorn a partir do diretório raiz do projeto:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`. Você pode acessar a documentação interativa (Swagger UI) em `http://127.0.0.1:8000/docs`.

## Endpoints da API

A seguir estão os principais endpoints disponíveis:

### Categorias

- `POST /categorias`: Cria uma nova categoria de treino.
- `GET /categorias`: Lista todas as categorias de treino.

### Centros de Treinamento

- `POST /centros_treinamento`: Cria um novo centro de treinamento.
- `GET /centros_treinamento`: Lista todos os centros de treinamento.

### Atletas

- `POST /atletas`: Cria um novo atleta.
- `GET /atletas`: Lista todos os atletas.
- `GET /atletas/{id}`: Retorna os detalhes de um atleta específico pelo ID.
- `PATCH /atletas/{id}`: Atualiza parcialmente os dados de um atleta pelo ID.
- `DELETE /atletas/{id}`: Exclui um atleta pelo ID.

