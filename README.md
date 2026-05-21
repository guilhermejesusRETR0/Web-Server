# Web-Server

Projeto académico de Administração de Sistemas com Django.

## Objetivo
Desenvolver uma aplicação Django com separação entre ambiente de desenvolvimento e produção, usando Git/GitHub, variáveis de ambiente, MySQL, Docker e Docker Compose.

## Ambientes
Desenvolvimento local:
- `python -m venv .venv`
- `.\.venv\Scripts\python -m pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

Produção/containers (simulação):
- `docker compose up --build`
- App: `http://localhost:8000`
- Base de dados: MySQL em `db:3306`

## Variáveis de ambiente
1. Copiar `.env.example` para `.env`.
2. Atualizar os valores sensíveis no `.env`.
3. Nunca commitar `.env`.

Principais variáveis:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DB_ENGINE`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_CHARSET`
- `DB_INIT_COMMAND`
- `MYSQL_ROOT_PASSWORD`

## Docker Compose
Serviços incluídos:
- `web`: aplicação Django
- `db`: MySQL 8.4 com volume persistente

## Funcionalidades da aplicação
- Página inicial `/`
- Feed global `/feed/`
- Página de publicações por utilizador `/utilizador/<username>/`
- Dados obtidos da base de dados com modelos `Profile`, `Post` e `Comment`

## Checklist de requerimentos
- Git + GitHub com commits por etapa
- Ambiente virtual Python
- Aplicação Django
- Variáveis de ambiente
- Base de dados MySQL
- Dockerfile
- Docker Compose com `web` + `db`
