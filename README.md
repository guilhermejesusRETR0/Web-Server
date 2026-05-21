# Web-Server

Projeto académico de Administração de Sistemas com Django.

## Objetivo
Desenvolver uma aplicação Django com separação entre ambiente de desenvolvimento e produção, usando Git/GitHub, variáveis de ambiente, MySQL, Docker e Docker Compose.

## Configuração de base de dados MySQL
1. Copiar `.env.example` para `.env`.
2. Descomentar as variáveis MySQL e ajustar os valores.
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
