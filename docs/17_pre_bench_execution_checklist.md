# Checklist Final de Execução (Pre-Bench)

## Fase A: Preparação do Ambiente
- [ ] Câmara em regime UHV (< 10^-8 mbar).
- [ ] Criostato/Resfriamento estabilizado na temperatura alvo.
- [ ] Blindagem magnética/vibracional verificada.

## Fase B: Calibração do Aparato
- [ ] Alinhamento das três grades (Talbot-Lau) verificado via laser de referência.
- [ ] Medição de baseline com N=1 (visibilidade máxima esperada).
- [ ] Teste de ruído eletrônico dos detectores.

## Fase C: Execução da Corrida
- [ ] Carregamento da amostra mesoscópica (janela N=30-70).
- [ ] Configuração do tempo de integração tau = 1.0s.
- [ ] Monitoramento ativo de jitter durante a coleta.

## Fase D: Pós-Processamento Imediato
- [ ] Exportação dos dados para o formato `pre_bench_dataset_template.csv`.
- [ ] Verificação de integridade dos hashes de dados.
- [ ] Preenchimento do `pre_bench_run_report.md`.

## Fase E: Critério de Parada Instrumental
- [ ] Se P_chamber subir > 20% do baseline -> INTERROMPER.
- [ ] Se Jitter_metric > 0.1 -> DESCARTAR CORRIDA.
- [ ] Se V(N=1) cair < 0.8 -> RECALIBRAR ALINHAMENTO.

---
## Status Epistemológico
- **Categoria:** OPERAÇÃO TÉCNICA
- **Pertence ao Core:** NÃO
- **Função:** Garantir que a execução física siga o protocolo congelado.
