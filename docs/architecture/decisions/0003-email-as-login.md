# ADR 0003: E-mail como identificador de acesso

## Status

Aceita.

## Decisao

O Sismon possui um modelo proprio de usuario. O e-mail e unico e e usado para entrar no sistema. Nomes de usuario nao serao usados.

## Consequencias

Convites e recuperacao de acesso poderao usar o mesmo e-mail cadastrado. Como a mudanca ocorreu antes do uso real, o banco local anterior foi recriado para evitar dados inconsistentes.
