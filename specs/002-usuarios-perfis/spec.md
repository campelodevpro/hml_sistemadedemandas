# T002: Usuarios, perfis, unidades e setores

## Objetivo

Modelar usuarios, perfis, unidades e setores para permitir participacao e gerencia em varios setores, formando a base do isolamento de dados e permissoes.

## Escopo

- Unidade como agrupador simples e setor vinculado a uma unidade.
- Participacao de usuario em varios setores.
- Gerencia de usuario em varios setores, independente da participacao.
- Perfis Administrador, Gerente e Responsavel com as permissoes definidas no ticket.
- Visibilidade de tarefas por participacao ou gerencia do setor.
- Tela de gerenciar equipe para administradores e gerentes do setor.

## Fora de escopo

- Hierarquia entre setores.
- Permissoes granulares por acao.
- Movimentacao em lote entre setores.

## Criterios de aceite

- Usuario com varios setores ve as tarefas combinadas desses setores.
- Gerente edita equipe apenas nos setores que gerencia.
- Superusuario acessa gerenciar equipe sem restricao.
- Migracao preserva o setor de perfis ja existentes como participacao e, quando o perfil for gerente, como gerencia.
- As cinco validacoes do projeto passam.
