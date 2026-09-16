# T001: Quadro de tarefas e ciclo de vida

## Objetivo de negocio

Dar visibilidade do trabalho em andamento e evitar que demandas longas sejam esquecidas.

## Regras vinculadas

RN-001, RN-002 e RN-005.

## Criterios de aceite

- [ ] Demanda completa entra no backlog por padrao.
- [ ] Demanda completa pode iniciar em uma etapa escolhida.
- [ ] Demanda incompleta pode ser salva como rascunho.
- [ ] Rascunho exibe campos faltantes e fica privado para o criador.
- [ ] Demanda completa aparece no quadro oficial.
- [ ] O quadro mostra responsavel, prazo, status e prioridade.
- [ ] O sistema evita sobrescrever uma edicao concorrente.

## Cenarios BDD

### Entrada padrao no backlog

Given uma demanda com informacoes obrigatorias preenchidas
When o usuario conclui o cadastro sem escolher uma etapa
Then a demanda aparece no backlog

### Entrada direta em andamento

Given uma demanda completa e um fluxo configurado
When o usuario escolhe Em Andamento no cadastro
Then a demanda aparece em Em Andamento

### Rascunho privado

Given uma demanda com informacoes faltantes
When o criador salva o cadastro
Then o sistema salva como rascunho, mostra os faltantes e oculta de outros usuarios
