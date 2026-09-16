# Modelo de dados inicial

## Entidades

| Entidade | Finalidade |
|---|---|
| usuario | Identidade, perfil, unidade, setor e gerente |
| unidade | Limite organizacional de acesso |
| setor | Grupo de trabalho dentro da unidade |
| equipe | Conjunto de colaboradores gerenciado |
| projeto | Objetivo, contexto, impacto, prioridade e prazos |
| demanda | Necessidade de trabalho, podendo estar solta ou ligada a projeto |
| tarefa | Trabalho executavel com etapa, responsavel e prazo |
| apontamento_hora | Registro de tempo trabalhado |
| capacidade_semanal | Horas disponiveis por colaborador e semana |
| movimento | Historico de status, comentario e atualizacao |
| auditoria | Quem, quando e o que mudou |

## Dicionario de dados inicial

| Campo | Tipo | PII ou sensibilidade | Origem | Validacao |
|---|---|---|---|---|
| usuario.nome_completo | texto | PII basica | Convite e cadastro | Obrigatorio, tamanho limitado |
| usuario.email | texto | PII basica | Convite | Obrigatorio, formato e unicidade |
| usuario.perfil | enumeracao | Organizacional | Administrador ou gerente | Valor permitido |
| usuario.unidade_id | identificador | Organizacional | Administrador ou gerente | Unidade existente |
| usuario.setor_id | identificador | Organizacional | Administrador ou gerente | Setor compatível |
| usuario.nivel_tecnico | enumeracao | Desempenho potencial | Usuario autorizado | Valores definidos em spec |
| projeto.contexto | texto | Negocio | Usuario autorizado | Tamanho limitado |
| projeto.impacto | enumeracao | Negocio | Usuario autorizado | Valores definidos em spec |
| projeto.prazo | data | Negocio | Usuario autorizado | Data valida |
| tarefa.status | enumeracao | Operacional | Quadro | Etapa existente |
| tarefa.responsavel_id | identificador | PII indireta | Usuario autorizado | Pessoa no escopo |
| tarefa.horas_trabalhadas | decimal | Desempenho | Apontamento | Nao negativa |
| capacidade_semanal.horas_disponiveis | decimal | Desempenho | Gerente ou administrador | Entre 0 e 30 |
| auditoria.valor_anterior | texto estruturado | Pode conter PII | Sistema | Sanitizar e restringir acesso |

Dados pessoais e de desempenho devem ter finalidade, minimizacao, retencao e acesso documentados antes do uso em producao.
