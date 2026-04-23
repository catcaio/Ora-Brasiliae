# Simulação de Coleta com Erro

## Objetivo

Registrar o desenho mínimo de simulação de coleta para o issue **MPV-54**, com ruído de medição explícito, saídas reproduzíveis e critérios auditáveis de distinção entre os regimes linear e quadrático.

---

## Artefato principal

- `notebooks/18_measurement_simulation.ipynb`

O notebook gera uma campanha sintética de medições de visibilidade em função de $N$, com:

- janela operacional fixa: $N \in \{30,40,50,60,70\}$;
- 10 corridas por ponto;
- erro de medição aditivo gaussiano com desvio-padrão configurável;
- semente determinística (`SEED=42`) para reprodutibilidade integral.

---

## Estratégia de validação auditável

A validação segue quatro blocos rastreáveis:

1. **Geração de dados sintéticos**
   - Curva "verdadeira" definida pelo regime quadrático com parâmetros de referência da trilha preditiva.
   - Aplicação de ruído de medição ponto a ponto, com truncamento físico em $V \in (0,1]$.

2. **Agregação por ponto de coleta**
   - Cálculo de média e desvio-padrão de $V$ para cada valor de $N$.

3. **Ajuste dos modelos concorrentes**
   - Ajuste do parâmetro linear ($a$) e quadrático ($b$) em espaço logarítmico operacional.
   - Reconstrução das curvas previstas para cada modelo.

4. **Critério de decisão**
   - Comparação via RMSE entre modelo linear e quadrático.
   - Classificação: `quadratic`, `linear` ou `inconclusive` com margem relativa mínima de 5%.

---

## Resultado esperado do bloco MPV-54

- Simulação reproduzível de campanha de coleta com erro instrumental;
- Métrica objetiva de separação de modelos para alimentar o pipeline de fitting (MPV-55);
- Evidência auditável de prontidão metodológica, sem promover previsão a validação experimental.

---

## Restrições epistemológicas

- Documento de **simulação operacional** (não de medição real);
- Não altera status do core;
- Não constitui validação experimental do efeito $N^2$.

---

## Status Epistemológico

- Categoria: PREVISÃO
- Pertence ao Core: NÃO
- Função: ponte entre protocolo e pipeline de ajuste
