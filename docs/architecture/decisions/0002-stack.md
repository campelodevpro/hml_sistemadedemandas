# ADR 0002: Stack oficial do Sismon

## Status

Aceita.

## Decisao

O backend usara Python com Django. O banco oficial sera PostgreSQL, acessado pelo Django ORM. A interface usara Django Templates, HTMX e Bootstrap 5, com JavaScript somente quando necessario.

A arquitetura sera um monolito modular. A autenticacao usara Django Authentication. Os testes usarao pytest e pytest-django. A qualidade sera verificada com Ruff, Black e mypy.

O primeiro ambiente sera Windows e localhost.

## Consequencias

O projeto tera poucas partes para manter e podera funcionar localmente sem servicos pagos. O PostgreSQL sera exigido no ambiente oficial. Um fallback SQLite podera ser usado somente para testes locais quando DATABASE_URL nao estiver definida.
