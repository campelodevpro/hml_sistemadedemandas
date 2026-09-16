# RESUMO COMPACTO (ler primeiro)
- Projeto: Portal de gestao da UTIC | Perfil: Co-piloto | Harness: Medio | Cobertura: REFORCADO | Fase: implementacao
- Ticket atual: T001 | Proximo passo: concluir movimentacao e edicao das tarefas | ORQUESTRADOR: v5
- Riscos e dividas abertas: convite por e-mail, equipes, importacao de planilha, Gantt e indicadores completos permanecem pendentes

---
# DETALHE COMPLETO
- Ultima atualizacao: 2026-09-16
- Modo: teste rapido com possibilidade de crescimento
- Plataforma / Stack: Django, PostgreSQL, Django Templates, HTMX, Bootstrap 5, JavaScript minimo, monolito modular, Django ORM, Windows e localhost
- Dados pessoais tratados: a definir
- Pilares ativos: 1, 2, 3, 4, 5, 6, 9, 14, 15, 16, 17, 18, 19; 7 por uso em celular
- Capacidades E1-E6 ativas: E1.1, E1.3, E2.3, E2.4, E3.1, E3.2 se houver integracao, E5.2, E5.3, E6.1 completo, E6.2, E6.3, E6.4 responsivo e offline parcial
- Stack confirmada: Python com Django, PostgreSQL, Django Templates, HTMX, Bootstrap 5, JavaScript somente quando necessario, monolito modular, Django Authentication, Django ORM, pytest, pytest-django, Ruff, Black e mypy; execucao inicial em Windows e localhost.
- Autenticacao: e-mail unico e senha; banco local recriado em 2026-09-16 antes de receber dados reais.

## Regras de negocio-chave
- O administrador configura usuarios, perfis, equipes, unidades, parametros, mensagens, alertas e regras do sistema.
- O gerente gerencia uma equipe e acompanha responsaveis, atividades, horas alocadas, projetos, demandas soltas e demandas vinculadas a projetos.
- O gerente deve ter relatorios, dashboard e monitoramento completo da equipe.
- O responsavel visualiza seu board, dashboard e relatorios, e pode cadastrar demandas e projetos e vincular demandas a projetos.
- Todos os perfis podem consultar cronograma Gantt de um projeto e uma visao macro dos projetos por equipe.
- Gerentes e responsaveis pertencem a uma unidade.
- Cada unidade e setor deve visualizar apenas suas atividades, processos, documentos, fluxos e anexos.
- O acesso deve respeitar a unidade, o setor, o projeto e a demanda do usuario.
- Alteracoes e exclusoes devem ter um estagio seguro para recuperar atividades ou demandas.
- O foco principal da primeira versao e evidenciar a capacidade de execucao da equipe e da unidade, considerando nivel tecnico e horas disponiveis.
- Para a primeira versao, o usuario nao indicou nenhuma funcao especifica para ficar de fora.
- O portal deve apresentar dashboards e um monitor ativo das atividades em andamento.
- Projetos devem poder ser vistos em cards ou em listagem completa, com cores, indicadores, tabelas e listas personalizadas.
- A equipe tem 4 analistas, 2 assistentes e 3 estagiarios na UTIC.
- O sistema deve controlar projetos, demandas avulsas e atividades que nao sao abertas no GLPI.
- O sistema deve acompanhar responsavel, equipe, atividade em execucao ou pendente, datas previstas e reais, horas trabalhadas e prazos.
- Cada colaborador deve ter no maximo 30 horas semanais disponiveis para planejamento.
- O sistema deve oferecer visao resumida dos projetos em andamento, com contexto, impacto, importancia e prioridade.
- A operacao trata aproximadamente 450 chamados por mes e mais de 60 projetos concorrentes.

## MVP
- [ ] Ainda nao definido.

## Progresso (checkpoint por ticket)
- Concluidos / Em andamento / Proximo: triagem e perfil concluidos; camada de seguranca definida; entrevista em andamento pelo Bloco A.

## Suposicoes do agente pendentes de validacao
- Nenhuma ate o momento.

## Pendencias
- Entrevista Bloco A: objetivo, perfis de acesso e limites funcionais confirmados; sem prazo ou limite de custo definido.
- Entrevista Bloco B: tipos de usuario identificados; forma de entrada ainda pendente.
- O cadastro sera iniciado por e-mail informado no sistema e concluido pela pessoa por meio de um link de convite enviado por e-mail.
- O acesso nao depende de aprovacao adicional depois do cadastro completo.
- O administrador ou gerente informa a area ou setor no convite; o e-mail fica vinculado ao gerente e a pessoa e incluida no setor escolhido.
- Ao concluir o cadastro, o acesso e liberado automaticamente.
- A pessoa podera recuperar a senha por e-mail.
- Confirmacao em duas etapas nao sera usada na primeira versao; fica planejada para depois da homologacao.
- Bloco B concluido: convite por e-mail, cadastro automatico por setor, recuperacao por e-mail e segunda etapa de seguranca adiada.
- Bloco C em andamento: dados pessoais adicionais ainda pendentes.
- Nao foram indicados telefone, documentos ou outros dados delicados para a primeira versao.
- A importacao de atividades e tarefas deve aceitar uma planilha com layout pre-definido.
- O cadastro manual deve continuar disponivel.
- Integracao direta com GLPI, ERP ou outro sistema nao foi definida neste momento.
- Bloco C aguardando confirmacao do resumo.
- Bloco C concluido: dados, importacao por planilha e cadastro manual definidos; integracoes externas ainda nao definidas.
- Bloco D em andamento: identidade visual pendente.
- A identidade visual inicial deve usar tema azul pastel.
- O quadro de tarefas e a primeira fatia implementavel do T001.
- Tela prioritariamente visual ainda pendente de definicao.
- O quadro de tarefas e a tela prioritaria da primeira versao.
- O idioma inicial sera portugues, sem necessidade de recurso especial de acessibilidade alem do basico.
- Bloco D aguardando confirmacao do resumo.
- Bloco D concluido: tema azul pastel, uso em computador e celular, quadro de tarefas prioritario e idioma portugues.
- Bloco E em andamento: local de funcionamento ainda pendente.
- A primeira versao sera executada inicialmente na maquina do usuario.
- O historico do projeto, incluindo decisoes, alteracoes e versoes, deve ser guardado desde o inicio.
- A manutencao futura sera responsabilidade do usuario.
- O acesso da equipe a partir de outros computadores e celulares ainda precisara ser definido com seguranca.
- Bloco E aguardando confirmacao do resumo.
- Bloco E concluido: execucao inicial na maquina do usuario, historico desde o inicio e manutencao pelo usuario.
- Bloco F em andamento: preferencias de ferramentas pendentes.
- Preferencia tecnica: Python no sistema principal, PostgreSQL como banco e interface moderna, estavel, performatica e visual, inspirada em Monday e Asana.
- A primeira versao deve usar apenas ferramentas e servicos gratuitos.
- Bloco F aguardando confirmacao do resumo.
- Nova necessidade registrada: o sistema deve poder criar APIs e consumir APIs de outros sistemas.
- APIs acionam controle de acesso, validacao de entrada, limite contra abusos, auditoria e contratos de integracao.
- Pedido de sincronizacao com o repositorio remoto https://github.com/campelodevpro/hml_sistemadedemandas.git registrado para a etapa de scaffolding e primeiro envio autorizado.
- Bloco F confirmado com alteracao de escopo; escopo de exposicao das APIs pendente.
- Decisao atual: APIs nao fazem parte do escopo do Sismon neste momento. A necessidade foi removida antes da implementacao.
- Bloco G em andamento: regras de negocio para o ciclo de vida das demandas pendentes.
- Regra provisoria: toda demanda nova entra no backlog por padrao; o cadastro pode escolher outra etapa inicial dentro do fluxo Scrum ou Kanban.
- Demandas incompletas podem ser salvas, mas devem exibir alerta amarelo ou icone de exclamacao com os itens faltantes.
- Correcao de entendimento no Bloco G: a demanda pode ser salva incompleta como rascunho com alerta; para entrar no fluxo normal, deve estar completa.
- Rascunhos de demandas, tarefas e atividades nao precisam de aprovacao e ficam visiveis somente para quem os criou.
- Nao foram definidos prazos ou limites especiais para rascunhos, horas ou prioridades nesta regra inicial.
- Duas pessoas nao deverao editar a mesma demanda ao mesmo tempo; a forma de evitar perda de alteracoes sera definida tecnicamente.
- Regra critica aguardando exemplos concretos: demanda completa no backlog, entrada direta em etapa e rascunho incompleto.
- Exemplo pendente de classificacao: "Criacao dos scripts de migracao em Python", responsavel Carlos, prazo de 3 dias, status Em Andamento.
- Exemplo 1 validado: "Criacao dos scripts de migracao em Python", responsavel Carlos, prazo de 3 dias, pode iniciar diretamente em Em Andamento.
- Exemplo 2 registrado: "Integracao de Login Unico (SSO) com Provedor de Identidade", prioridade maxima, entra no backlog com tarefas em Concluido, Em Andamento e A Fazer, cada uma com responsavel, sprint e prazo.
- Exemplo 3 registrado: "Melhorar Avisos", criado por Leonardo, incompleto, salvo como Rascunho Privado, fora do board e do backlog oficial e visivel somente ao autor.
- Bloco G aguardando confirmacao do conjunto de regras e exemplos.
- Nova funcionalidade: painel de indicadores de desempenho como segunda prioridade, depois do quadro de tarefas.
- Indicadores propostos: capacidade da equipe, cycle time medio, throughput, risco de prazo e carga de trabalho por pessoa.
- Os indicadores devem ser calculados a partir dos dados do proprio quadro e do PostgreSQL, sem API externa, BI pago ou servico pago.
- Visao por perfil: responsavel ve seus itens; gerente ve o setor; administrador ve a comparacao entre setores, projetos em risco e adocao.
- O painel deve informar dados insuficientes, sinalizar dados faltantes como excecao e registrar alteracoes que impactem os indicadores.
- Fora do escopo inicial: alertas por e-mail ou push, BI externo e previsoes com IA.
- A ordem sugerida e quadro de tarefas, cadastro e permissoes, painel de indicadores e depois recursos completos de backlog, Kanban, Scrum e Gantt. Ainda falta confirmar essa ordem.
- Dados de desempenho associados a pessoas exigem cuidado adicional de privacidade e controle de acesso.
- Regra do semaforo de prazo ainda pendente de definicao.
- Regra inicial do semaforo definida sem usar estimativa de horas: vermelho quando o prazo passou e a tarefa nao esta concluida; amarelo quando restam 20% ou menos do prazo e a tarefa esta por fazer, ou quando esta em andamento sem movimentacao por 3 dias; verde nos demais casos.
- Movimentacao inclui troca de status, comentario ou atualizacao.
- A regra de semaforo podera evoluir na v2 para considerar horas estimadas restantes e horas disponiveis.
- Tipo de contagem do prazo, dias corridos ou dias uteis, ainda pendente.
- Prazo do semaforo usara dias uteis simples, de segunda a sexta, sem tabela de feriados na primeira versao.
- A regra de jornada por setor ainda precisa ser confirmada; por padrao seguro, sera igual para todos se confirmado.
- A regra de jornada sera igual para todos os setores, de segunda a sexta, sem considerar feriados na primeira versao.
- Bloco G aguardando confirmacao final das regras de fluxo, rascunho, concorrencia e semaforo.
- Bloco G concluido: fluxo de demandas, rascunhos privados, exemplos, semaforo por dias uteis, regras de movimentacao e historico confirmados.
- Fase atual: proposta de harness; aguardando escolha entre Simplificado, Medio e Hard.
- Ponte de traducao preparada: decisoes do usuario separadas de pontos tecnicos ainda pendentes.
- Decisoes confirmadas: portal web responsivo, Python, PostgreSQL, tema azul pastel, quadro de tarefas prioritario, perfis com acesso por unidade e setor, convite por e-mail, recuperacao por e-mail, sem segunda etapa na primeira versao, fluxo backlog/Kanban/Scrum/Gantt, rascunho privado, importacao por planilha, controle de capacidade, servicos gratuitos, execucao inicial local, historico, manutencao pelo usuario, APIs fora do escopo e sincronizacao posterior com o repositorio informado.
- Suposicoes pendentes: tecnologia visual, campos obrigatorios e forma segura de acesso da equipe a maquina inicial.
- Stack confirmada: Python com Django, PostgreSQL, Django Templates, HTMX, Bootstrap 5, JavaScript somente quando necessario, monolito modular, Django Authentication, Django ORM, pytest, pytest-django, Ruff, Black e mypy; Windows e localhost.
- Implementacao T001 iniciada: autenticacao, modelos de unidade, setor, perfil, projeto e tarefa, cadastro de demanda, rascunho privado, semaforo e quadro responsivo.
- Verificacoes aprovadas em 2026-09-16: Django check, 3 testes pytest, Ruff, Black, mypy e login HTTP local com status 200.
- T001 ainda em andamento: faltam movimentacao de tarefas, edicao, auditoria e campos obrigatorios finais.
- Checkpoint 2026-09-16: primeira fatia validada, commit 958b98d enviado para origin/main.
