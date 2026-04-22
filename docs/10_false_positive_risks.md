# Riscos de Falso Positivo

## Objetivo

Mapear mecanismos que poderiam imitar artificialmente uma assinatura aparente de escalonamento quadrático sem que o efeito previsto esteja realmente presente.

---

## Fontes de Risco

### Decoerência ambiental mal modelada
Se a decoerência ambiental externa (colisões, radiação térmica) escalar de forma não linear com o tamanho do sistema de forma desconhecida, ela pode ser confundida com o efeito $N^2$ intrínseco.

### Drift instrumental
Variações lentas nos parâmetros de controle (ex: intensidade de laser ou campo magnético) durante a varredura de $N$ podem simular decaimentos de visibilidade anômalos.

### Jitter temporal
Imprecisões no tempo de observação $\tau$ que cresçam com o tamanho da amostra podem introduzir erros que imitem a dependência quadrática.

### Dependência oculta de parâmetros coletivos
Interações atômicas padrão de muitos corpos (não relacionadas ao modelo) podem gerar perdas de coerência que escalam com o número de partículas.

### Erros de normalização do contraste
Falhas na calibração do contraste interferométrico base ($V=1$ para $N=1$) podem distorcer a curva de decaimento percebida.

### Seleção enviesada da janela de N
A escolha arbitrária de uma janela muito estreita de $N$ onde as curvas linear e quadrática são próximas pode levar a falsas identificações de regime por flutuação estatística.

---

## Consequência

Qualquer alegação futura de compatibilidade experimental deve comparar explicitamente o modelo previsto com esses mecanismos de fundo, demonstrando que a assinatura observada supera estatisticamente essas fontes de erro.

---

## Status Epistemológico

- Categoria: SUPORTE À PREVISÃO
- Pertence ao Core: NÃO
- Função: blindar a interpretação futura contra overclaim
