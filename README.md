# Web-Server

Projeto académico de Administração de Sistemas com Django.

## Objetivo
Desenvolver uma aplicação Django com separação entre ambiente de desenvolvimento e produção, usando Git/GitHub, variáveis de ambiente, MySQL, Docker e Docker Compose.

## Configuração de base de dados MySQL
1. Copiar `.env.example` para `.env`.
2. Ajustar os valores das variáveis.
3. Executar migrações com `python manage.py migrate`.

Variáveis MySQL usadas pela aplicação:
- `DB_ENGINE=django.db.backends.mysql`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_CHARSET` (default `utf8mb4`)
- `DB_INIT_COMMAND` (default `SET sql_mode='STRICT_TRANS_TABLES'`)

## Docker Compose
1. Copiar `.env.example` para `.env` e atualizar passwords.
2. Construir e iniciar serviços:
   `docker compose up --build`
3. A aplicação fica em `http://localhost:8000`.

Serviços incluídos:
- `web`: aplicação Django
- `db`: MySQL 8.4 com volume persistente
