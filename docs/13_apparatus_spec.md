# Especificação de Aparato Experimental (Setup Mínimo)

## Objetivo

Definir um **setup mínimo de bancada** para testar, de forma auditável e reproduzível, a distinção entre os regimes de decaimento de visibilidade $V(N)$ linear ($N$) e quadrático ($N^2$).

---

## Escopo e fronteira epistemológica

- Este documento especifica **infraestrutura de medição** (aparato), não validação física final.
- Não promove nenhuma previsão ao status de resultado confirmado.
- Mantém separação entre:
  - **core** (derivações locais);
  - **support/previsão** (ponte para bancada).

---

## Arquitetura mínima do aparato

Sistema-alvo: **interferometria molecular mesoscópica** (faixa operacional com maior separação prevista entre modelos).

### Blocos obrigatórios

1. **Fonte molecular estável**
   - Emissão controlada e repetível.
   - Dispersão de velocidade monitorada por janela de aquisição.

2. **Interferômetro de três grades (Talbot-Lau/KDTLI compatível)**
   - Grade 1: preparação de coerência transversal efetiva.
   - Grade 2: modulação de fase (ou equivalente óptico).
   - Grade 3 + leitura: amostragem de contraste/franjas.

3. **Câmara de vácuo em regime UHV**
   - Pressão-alvo operacional: ordem de $10^{-8}$ a $10^{-9}$ mbar.
   - Objetivo: reduzir colisões residuais e decoerência basal.

4. **Controle térmico e de vibração**
   - Isolamento vibracional da bancada.
   - Controle térmico contínuo dos componentes críticos.

5. **Detecção e aquisição de dados**
   - Leitura de intensidade com resolução suficiente para estimar
     $V = (I_{max}-I_{min})/(I_{max}+I_{min})$.
   - Registro sincronizado de metadados de ambiente por corrida.

6. **Camada de controle e auditoria experimental**
   - Script versionado para sequência automática de corridas.
   - Geração de artefatos reproduzíveis (CSV/JSON + relatório).
   - Trilhas de auditoria com hash dos arquivos gerados.

---

## Envelope operacional mínimo

- **Janela de N:** 30 a 70.
- **Pontos mínimos em N:** 5 valores distintos (ideal: 7).
- **Tempo por corrida ($\tau$):** ~1.0 s.
- **Repetições por ponto:** mínimo 10.
- **Erro relativo de visibilidade:** alvo < 5%.

---

## Variáveis monitoradas por corrida

- ID da corrida e timestamp UTC.
- Valor de $N$ configurado.
- Pressão da câmara.
- Temperatura local dos blocos críticos.
- Métrica de jitter temporal.
- Intensidades $I_{max}$ e $I_{min}$.
- Visibilidade calculada $V$.
- Flag de qualidade (pass/fail) por critérios pré-registrados.

---

## Critérios de aceitação do setup (pronto para campanha)

O aparato é considerado apto quando todos os itens abaixo forem satisfeitos:

1. **Estabilidade ambiental**
   - Pressão e temperatura dentro das bandas definidas em >95% das corridas de qualificação.

2. **Repetibilidade instrumental**
   - Variação intra-ponto de $V$ compatível com erro relativo < 5%.

3. **Integridade de dados**
   - 100% das corridas com metadados completos e hash registrado.

4. **Auditabilidade**
   - Capacidade de reproduzir os gráficos e ajustes a partir apenas dos artefatos versionados.

---

## Artefatos obrigatórios de saída

Para cumprir a regra operacional do projeto (outputs reproduzíveis + validação auditável), cada campanha deve produzir:

- `raw_runs.csv`: dados brutos por corrida.
- `run_metadata.json`: parâmetros, versão de script, ambiente e hashes.
- `fit_report.md`: ajuste comparativo dos modelos linear e quadrático.
- `readiness_report.md`: checklist de prontidão e não conformidades.

---

## Riscos operacionais mínimos e mitigação

- **Deriva térmica:** recalibração em blocos temporais fixos.
- **Jitter mecânico:** monitor dedicado + descarte criterioso de corrida.
- **Perda de contraste por contaminação de grade:** rotina de inspeção e limpeza.
- **Subamostragem estatística:** bloqueio automático de relatório se repetições < mínimo.

---

## Referências técnicas usadas para o setup mínimo

- Configurações de interferometria de matéria com três grades em geometria Talbot-Lau/KDTLI.
- Exigências práticas de vácuo ultra-alto e estágios de bombeamento diferencial em experimentos mesoscópicos recentes.

(Referências externas são suporte de engenharia de aparato; não alteram o status epistemológico do core.)

---

## Status Epistemológico

- Categoria: SUPORTE À PREVISÃO
- Pertence ao Core: NÃO
- Função: especificar infraestrutura mínima para teste auditável
