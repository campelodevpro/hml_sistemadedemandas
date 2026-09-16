# Visao da arquitetura

O sistema sera um portal web responsivo com backend em Python, banco PostgreSQL e uma camada visual moderna a definir em ADR. O primeiro ambiente sera local.

O quadro sera a origem dos dados operacionais. Os indicadores serao calculados por consultas agregadas no banco, respeitando o acesso por unidade, setor, projeto e demanda.

As areas principais serao:

1. Identidade e perfis.
2. Unidades, setores e equipes.
3. Projetos, demandas, tarefas e atividades.
4. Quadro, backlog, Gantt e importacao.
5. Horas, capacidade e indicadores.
6. Auditoria, historico e recuperacao.
