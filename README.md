# Teoria de Ora Brasiliae - Repositório de Pesquisa

## 1. O que é
Este repositório contém a formulação mínima, a classificação epistemológica e a infraestrutura de auditoria simbólica do programa local baseado em entropia generalizada em diamantes causais.

## 2. Status atual
O núcleo mínimo local foi isolado. Resultados condicionais e completamentos consistentes foram separados do core. Nenhuma previsão empírica está validada. Nenhuma hipótese externa é tratada como derivação.

## 3. Claim mínimo irredutível
Em um diamante causal local, a estacionariedade de S_gen, combinada com a primeira lei do entrelaçamento e com Raychaudhuri linearizada, implica a projeção nulo-local da equação de Einstein.

Forma local:
G_{mu nu} k^mu k^nu = (8 pi G / c^4) <T_{mu nu}> k^mu k^nu

## 4. O que está derivado
- domínio causal local e superfície de bifurcação;
- definição de S_gen;
- operador variacional projetado;
- primeira lei do entrelaçamento em primeira ordem;
- Raychaudhuri linearizada;
- projeção nulo-local da equação de Einstein.

## 5. Hipóteses externas
- cutoff UV em escala de Planck;
- qualquer identificação UV completa;
- qualquer interpretação física global do coeficiente do GAP-10.

## 6. Aberturas empíricas
- observable V(tau) formalizado em docs/13_observable_formalization.md;
- fronteira N*;
- distinção observacional frente a GR / teorias escalar-tensoriais;
- qualquer fenomenologia cosmológica ou de ondas gravitacionais.

## 7. Estrutura
- /core/: núcleo mínimo irredutível
- /gaps/: fechamentos condicionais e completamentos consistentes
- /notebooks/: auditoria simbólica e numérica
- /appendices/: histórico e exploração
- /docs/: escopo, ledger, glossário, mapeamento e formalização observacional
- /bibliography/: fontes por confiança

## 8. Uso
Ler docs/01_claim_minimo_irredutivel.md e docs/02_epistemic_ledger.md antes de qualquer notebook. Executar notebooks em ordem numérica. Não usar resultados de /gaps/ como se fossem parte do core sem verificar hipóteses.

## 9. Regras de leitura epistemológica
- DERIVADO: segue de definições e identidades padrão no domínio local.
- FECHADO CONDICIONALMENTE: exige hipótese explícita.
- COMPLETAMENTO CONSISTENTE: não quebra a teoria, mas não é inevitável.
- HIPÓTESE EXTERNA: não derivada do núcleo.
