# Runbook inicial

## Estado

Ainda nao ha aplicacao publicada.

## Execucao local

A forma final de iniciar o sistema sera documentada quando a stack visual e as dependencias forem aprovadas.

## Retorno para a versao anterior

Antes de qualquer atualizacao, manter uma copia da versao atual e do banco. Em caso de falha, parar o sistema, restaurar a copia do banco, voltar para a versao anterior e executar o smoke test do quadro de tarefas em ate cinco minutos.

## Incidente

Nao expor stack trace ao usuario. Registrar somente informacoes sanitizadas e consultar o historico de auditoria.
