# Regras de negocio

| ID | Regra | Gatilho | Excecao | Dono | Exemplos | Status | Ticket |
|---|---|---|---|---|---|---|---|
| RN-001 | Demanda completa entra no backlog por padrao | Cadastro concluido | Pode iniciar em outra etapa escolhida | UTIC | E1, E2 | Confirmada | T001 |
| RN-002 | Rascunho incompleto e privado | Cadastro incompleto | Nao aparece no board nem exige aprovacao | Criador | E3 | Confirmada | T001 |
| RN-003 | Semaforo vermelho indica atraso | Prazo util passou | Tarefa concluida nao fica vermelha | Gerente | A1 | Confirmada | T003 |
| RN-004 | Semaforo amarelo indica risco | Restam 20% ou menos ou 3 dias sem movimento | Demais casos ficam verdes | Gerente | A2, A3 | Confirmada | T003 |
| RN-005 | Rascunho aparece somente ao criador | Item incompleto | Ao completar, entra no fluxo | Criador | E3 | Confirmada | T001 |
| RN-006 | Acesso respeita unidade e setor | Consulta ou alteracao | Administrador tem visao definida pelo perfil | Administrador | Acesso | Confirmada | T002 |
| RN-007 | Limite semanal de capacidade e 30 horas | Planejamento | Nenhuma definida | Gerente | Capacidade | Confirmada | T004 |

## Exemplos vinculados

E1: scripts de migracao em Python, Carlos, prazo de 3 dias, inicia em Em Andamento.

E2: Integracao de Login Unico, prioridade maxima, entra no backlog com tarefas em Concluido, Em Andamento e A Fazer.

E3: Melhorar Avisos, criado por Leonardo, incompleto, Rascunho Privado e fora do board.

A1: prazo passou e tarefa nao concluida, semaforo vermelho.

A2: tarefa de 10 dias com 2 dias uteis restantes e ainda A Fazer, semaforo amarelo.

A3: tarefa Em Andamento sem status, comentario ou atualizacao por 3 dias, semaforo amarelo.
