# Tradução de Parâmetros (a, b → físico)

## Objetivo

Converter os parâmetros abstratos do modelo de visibilidade em taxas físicas de decoerência, mantendo rastreabilidade auditável entre calibração numérica e projeção experimental.

---

## Definições operacionais

Modelos de contraste usados na trilha de previsão:

- Regime linear: \(V(N,\tau)=\exp(-a\,N\,\tau/2)\)
- Regime quadrático: \(V(N,\tau)=\exp(-b\,N^2\,\tau/2)\)

Para um alvo de visibilidade \(V_\*\) em \(N_\*\) e tempo de observação \(\tau\), a taxa total exigida é:

\[\gamma_\*= -\frac{2\ln(V_\*)}{\tau}\]

e a calibração mínima:

\[a=\frac{\gamma_\*}{N_\*}, \qquad b=\frac{\gamma_\*}{N_\*^2}\]

---

## Configuração de referência auditável

Parâmetros de referência (alinhados ao notebook 12):

- \(N_\*=100\)
- \(V_\*=0.5\)
- \(\tau=1.0\,\mathrm{s}\)

Resultado calibrado:

- \(\gamma_\*\approx 1.386\,\mathrm{s^{-1}}\)
- \(a\approx 1.386\times10^{-2}\,\mathrm{s^{-1}}\) por componente
- \(b\approx 1.386\times10^{-4}\,\mathrm{s^{-1}}\) por componente²

---

## Projeção para sistemas físicos

Com os parâmetros acima:

| Sistema | N típico | \(\gamma\) referência (s^-1) | \(\gamma_{linear}=aN\) (s^-1) | \(\gamma_{quadrático}=bN^2\) (s^-1) |
| :--- | ---: | :--- | ---: | ---: |
| Gases frios (BEC em armadilha) | 10000 | 0.1–10 | 138.6 | 13862.9 |
| Interferometria molecular | 50 | 1–100 | 0.693 | 0.347 |
| Átomos de Rydberg | 30 | 1e3–1e5 | 0.416 | 0.125 |

Leitura operacional:

1. Em **N** muito alto, o termo \(N^2\) domina rapidamente e impõe tempos de observação curtos.
2. Em faixa mesoscópica (\(N\sim 30\)–70), os regimes ainda são comparáveis e distinguíveis por ajuste estatístico.
3. Para plataformas com decoerência basal alta (ex.: Rydberg), é necessária recalibração dedicada de \((a,b)\) para o hardware específico.

---

## Reprodutibilidade

Script canônico para reprodução da tradução:

```bash
python scripts/parameter_translation.py
python scripts/parameter_translation.py --json
```

Esse artefato implementa:

- validação de entrada (
  \(N_\*>0\), \(0<V_\*<1\), \(\tau>0\)
);
- cálculo determinístico de \(\gamma_\*\), \(a\) e \(b\);
- projeção padronizada para sistemas de referência.

---

## Status Epistemológico

- Categoria: PREVISÃO
- Pertence ao Core: NÃO
- Função: traduzir parâmetros abstratos em ordem de grandeza física auditável
