# Faixas de Viabilidade (Comparação com Literatura)

## Objetivo

Transformar a previsão operacional (`N*`, janela de `N`, alvo interferométrico) em uma **faixa de viabilidade auditável** ancorada em literatura primária, sem promover este material ao core.

---

## Escopo

Este documento compara, de forma conservadora:

- ordens de grandeza de massa/composição já interferidas;
- escalas de velocidade e tempo de voo/integração reportadas;
- níveis de visibilidade e regimes de decoerência;
- implicações práticas para a janela proposta no repositório (`30 < N < 70`, `tau ~ 1 s`).

---

## Evidências primárias selecionadas

### E1) Interferometria molecular em alta massa (Nature Physics, 2019)

- Interferência observada para moléculas com massa **acima de 25.000 Da**.
- Experimento em interferômetro Talbot–Lau de **2 m**.
- Franjas com **mais de 90% da visibilidade esperada**.

Leitura operacional: o regime mesoscópico já mostrou contraste alto quando a preparação de feixe e o controle instrumental são adequados.

### E2) KDTLI com C70 e controle cinemático (Nature Communications, 2015)

- Feixe de C70 centrado em **~180 m/s**.
- Distribuição de velocidade com FWHM reportada e resolução de seleção de velocidade na ordem de poucos por cento.

Leitura operacional: o controle de velocidade é uma alavanca crítica para manter contraste e interpretar transição entre sinal e perda de coerência.

### E3) Revisão experimental consolidada (RMP, 2012)

- Configurações Talbot–Lau operam com de Broglie até ~1 pm para referência de **10.000 amu a 40 m/s**.
- Revisão documenta perda progressiva de visibilidade por decoerência térmica e colisional.
- Para escalas de massa crescentes, mitigação de decoerência exige ambiente mais frio e melhor vácuo.

Leitura operacional: a janela de detectabilidade não depende apenas de massa; depende fortemente de envelope térmico/pressão e estabilidade mecânica.

### E4) Extensão recente para nanopartículas (Nature, publicado em 21 jan 2026)

- Experimento reporta varredura de interferência com integração por ponto de até **4 s**.
- Discussão explícita de visibilidade prevista vs massa e condição de Talbot.
- Texto aponta que velocidades mais baixas (ex.: ~25 m/s) ampliam capacidade de discriminação em massas maiores.

Leitura operacional: para empurrar fronteira de massa sem colapsar distinguibilidade, a engenharia de velocidade/tempo de interação é o parâmetro dominante.

---

## Tradução para as faixas do projeto

### Faixa A — Conservadora (pronta para bancada incremental)

- `N` alvo: **20–50**
- `tau` efetivo: **0,2–1,0 s**
- Critério de contraste: manter incerteza de medição abaixo de ~5–10%
- Racional: zona com menor risco de ambiguidades entre ruído instrumental e sinal de escalonamento.

### Faixa B — Alvo principal do repositório

- `N` alvo: **30–70**
- `tau` efetivo: **~1 s**
- Requisito adicional: controle explícito de decoerência (térmica + colisional) e de jitter temporal.
- Racional: compatível com a síntese pré-experimental atual, mas exige disciplina de estabilidade metrológica.

### Faixa C — Agressiva (fronteira)

- `N` alvo: **70–120**
- `tau` efetivo: **1–4 s** (dependente de taxa de contagem)
- Risco dominante: convergência entre predição quântica/clássica fora da condição ótima de Talbot e queda de SNR.
- Racional: plausível como trilha de P&D, não como baseline de validação inicial.

---

## Critérios de viabilidade auditável

Para declarar uma faixa como viável no contexto MPV-59, exigir checklist mínimo:

1. **Contraste reproduzível** em múltiplas rodadas independentes.
2. **Orçamento de decoerência** separado por canal (térmico, colisional, vibração/alinhamento).
3. **Rastreio de velocidade/tempo** com incertezas explícitas.
4. **Curva sinal vs ruído** por subfaixa de `N`.
5. **Registro de falhas** (run inválido, drift, outlier instrumental) para auditoria.

---

## Conclusão operacional de MPV-59

Com base na literatura primária, a faixa do projeto (`30 < N < 70`, `tau ~ 1 s`) é **plausível**, mas **condicional** a controle instrumental comparável ao estado da arte em interferometria de matéria: estabilidade mecânica, envelope térmico/vácuo e governança de velocidade do feixe.

Portanto, a recomendação para execução é:

- iniciar validação na Faixa A;
- migrar para Faixa B somente após fechar orçamento de decoerência;
- tratar Faixa C como trilha exploratória, não critério de sucesso inicial.

---

## Referências usadas nesta comparação

1. Fein et al., *Quantum superposition of molecules beyond 25 kDa*, Nature Physics (2019).
2. Nimmrichter et al., *Coherence in the presence of absorption and heating in a molecule interferometer*, Nature Communications (2015).
3. Hornberger et al., *Colloquium: Quantum interference of clusters*, Rev. Mod. Phys. 84, 157 (2012).
4. Nature (2026), *Probing quantum mechanics with nanoparticle matter-wave interferometry* (publicado em 21 janeiro 2026).
5. Stickler et al., *Matter-wave interferometry with composite quantum objects*, arXiv:1501.07770.

---

## Status Epistemológico

- Categoria: PREVISÃO / SUPORTE
- Pertence ao Core: NÃO
- Função: ancorar faixa operacional em literatura primária para decisão de bancada
