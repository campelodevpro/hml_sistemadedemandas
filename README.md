# Sismon

Portal para monitorar demandas, projetos, tarefas, horas e capacidade de execucao do TIME.

## Situacao atual

O primeiro quadro visual de tarefas esta em desenvolvimento. O acesso usa e-mail e senha; a criacao de usuarios e equipes sera ampliada nas proximas etapas.

## Objetivos da primeira versao

1. Quadro visual de tarefas.
2. Cadastro com perfis e acesso por unidade e setor.
3. Indicadores por perfil.
4. Importacao de tarefas por planilha padronizada.

## Stack escolhida

Python com Django, PostgreSQL como banco oficial, Django Templates, HTMX e Bootstrap 5. Em localhost, sem `DATABASE_URL`, o projeto usa SQLite apenas para desenvolvimento.

## Primeiro acesso local

Depois de executar as migracoes, crie o administrador com:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

Informe um e-mail e uma senha. Esse e-mail sera usado para entrar no Sismon.
