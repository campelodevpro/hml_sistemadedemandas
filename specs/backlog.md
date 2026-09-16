# Backlog inicial

O backlog abaixo e uma proposta para aprovacao do MVP. Nenhum ticket deve ser codificado antes da Definition of Ready.

| ID | Titulo | Prioridade | Regra | Tamanho | Dependencias | Status |
|---|---|---|---|---|---|---|
| T001 | Quadro de tarefas e ciclo de vida | 1 | RN-001, RN-002, RN-005 | G | T002 | Em andamento |
| T002 | Usuarios, perfis, unidades e setores | 2 | RN-006 | G | Nenhuma | Bloqueado |
| T003 | Painel de indicadores e semaforo | 3 | RN-003, RN-004 | G | T001, T002 | Proposto |
| T004 | Capacidade, horas e nivel tecnico | 4 | RN-007 | G | T002 | Proposto |
| T005 | Importacao de tarefas por planilha | 5 | RN-001 | M | T001 | Proposto |
| T006 | Projetos, Gantt e visao macro | 6 | RN-001 | G | T001, T002 | Proposto |

## Definition of Ready

Um ticket so pode comecar quando tem regra vinculada, exemplo validado, criterio testavel e dependencias resolvidas.

## Bloqueios registrados

### T002 - Usuarios, perfis, unidades e setores

Faltam objetivo detalhado, escopo, fora de escopo, exemplos e criterios de aceite. A RN-006 define apenas o isolamento por unidade e setor, sem definir como equipes devem ser modeladas, se uma pessoa pode participar de mais de uma equipe ou quais telas e permissoes devem existir. Esses pontos precisam ser decididos antes da implementacao.
