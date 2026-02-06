# Análise de Maceração: Temperatura ⇄ Tempo

## Sobre o Projeto

Este projeto apresenta uma **análise estatística completa** dos processos de **Maceração A e B**, incluindo análise individual de cada processo e um **estudo comparativo** para identificar o processo mais eficiente.

### Análises Realizadas

#### 1️ Maceração A (Análise Original)

- **Período**: Novembro/2024 - Janeiro/2026 (7 meses)
- **Correlação**: -0.684 (moderada a forte)
- **Taxa de resfriamento**: 0.0815°C por minuto
- **Cada 1°C de aumento reduz ~5.74 minutos**

#### 2️⃣ Maceração B (Nova Análise)

- **Período**: Setembro/2024 - Janeiro/2026 (17 meses)
- **Correlação**: 0.312 (positiva)
- **Taxa de aquecimento**: +0.0331°C por minuto
- **Comportamento térmico oposto à Maceração A**

#### 3️⃣ Comparativo A vs B (Análise Estratégica)

- **Período Alinhado**: Setembro/2024 - Janeiro/2026 (17 meses)
- **Critérios Avaliados**: 4 (Controle Térmico, Eficiência, Previsibilidade, Estabilidade)
- **Processo Recomendado**: **Maceração A** (superior em 3 de 4 critérios)
- **Achado Crítico**: Comportamentos térmicos opostos (A perde temp, B ganha temp)

## Visualizar Relatórios

### Maceração A

**Online (GitHub Pages)**: [Clique aqui para ver o relatório](https://wilian-lab.github.io/rastreio-maceracao/relatorios/Maceracao_A/relatorio_completo_tempo_temperatura_20260205_1622.html)

**Local**: Abra `relatorios/Maceracao_A/relatorio_completo_tempo_temperatura_*.html` no navegador

### Maceração B

**Local**: Abra `relatorios/Maceracao_B/relatorio_completo*.html` no navegador

### Análise Comparativa A vs B

**Online**: [Relatório Executivo Comparativo](https://wilian-lab.github.io/rastreio-maceracao/relatorios/Comparativo/relatorio_executivo_A_vs_B_20260205_2127.html)

**Local**: Abra `relatorios/Comparativo/relatorio_executivo_A_vs_B_*.html` no navegador

## Conteúdo dos Relatórios

### Relatórios Individuais (A e B)

    Estatísticas descritivas completas
    Gráficos de evolução temporal
    Análise de regressão bidirecional
    Gráficos de dispersão com linha de tendência
    Análise de correlação (Tempo ↔ Temperatura)
    Recomendações operacionais específicas

### Relatório Comparativo (A vs B)

    Resumo  com processo recomendado
    Avaliação por 4 critérios técnicos
    Indicadores-chave de desempenho (KPIs)
    Análise estatística detalhada (t-test, F-test)
    Análise de regressão comparativa
    Observações críticas sobre comportamento térmico
    Recomendações técnicas e gerenciais
    Formato profissional sem gráficos (ideal para executivos)

## Tecnologias Utilizadas

- **Python 3.12**: Análise de dados
- **Pandas**: Manipulação e agregação de dados
- **Matplotlib & Seaborn**: Visualizações gráficas
- **Scipy**: Análise estatística e testes de hipótese
- **Jupyter Notebook**: Desenvolvimento interativo
- **NumPy**: Operações numéricas

## Estrutura do Projeto

```
Rastreio-masceracao/
│
├── notbooks/
│   ├── maceracao_A/
│   │   ├── Analise_tempo_masceracao.ipynb
│   │   └── maceracao_A_temperatura.ipynb
│   └── maceracao_B/
│       ├── maceracao_B_temperatura.ipynb
│       └── tempo_x_temperatura_B.ipynb
│
├── Comparativo/
│   └── comparativo_A_vs_B.ipynb          # Análise comparativa completa
│
├── relatorios/
│   ├── Maceracao_A/                      # HTMLs da Maceração A
│   ├── Maceracao_B/                      # HTMLs da Maceração B
│   └── Comparativo/                      # Relatório executivo A vs B
│
├── dados/                                # Dados originais
│   └── Dados maceração.xlsx
│
├── index.html                            # Página inicial GitHub Pages
├── README.md                             # Este arquivo
└── INSTRUCOES_GITHUB.md                  # Guia de publicação
```

## Como Usar

### Para Visualizar os Relatórios:

1. Clone o repositório
   ```bash
   git clone https://github.com/wilian-lab/rastreio-maceracao.git
   ```
2. Navegue até a pasta `relatorios/`
3. Abra os arquivos HTML no navegador:
   - `Maceracao_A/` - Análise da Maceração A
   - `Maceracao_B/` - Análise da Maceração B
   - `Comparativo/` - Comparação A vs B
4. Ou acesse os links do GitHub Pages (seção acima)

### Para Reproduzir ou Modificar as Análises:

#### Maceração A:

1. Abra `notbooks/maceracao_A/maceracao_A_temperatura.ipynb`
2. Execute as células sequencialmente
3. Relatório será gerado em `relatorios/Maceracao_A/`

#### Maceração B:

1. Abra `notbooks/maceracao_B/tempo_x_temperatura_B.ipynb`
2. Execute as células sequencialmente
3. Relatório será gerado em `relatorios/Maceracao_B/`

#### Análise Comparativa:

1. Certifique-se de ter executado as análises A e B primeiro
2. Abra `Comparativo/comparativo_A_vs_B.ipynb`
3. Execute as células sequencialmente
4. Relatório executivo será gerado em `relatorios/Comparativo/`

### Pré-requisitos:

```bash
pip install pandas matplotlib seaborn scipy numpy jupyter
```

## Principais Insights

### Diferenças Fundamentais entre A e B:

| Aspecto                   | Maceração A                         | Maceração B                         |
| ------------------------- | ----------------------------------- | ----------------------------------- |
| **Comportamento Térmico** | Perda de temperatura (-0.028°C/min) | Ganho de temperatura (+0.033°C/min) |
| **Controle Térmico**      | ±2.48°C (melhor)                    | ±3.04°C                             |
| **Tempo Médio**           | 62.9 min                            | 61.7 min (7.9% mais rápido)         |
| **Previsibilidade**       | R² = 12.7% (melhor)                 | R² = 9.7%                           |
| **Estabilidade Térmica**  | 0.028°C/min (melhor)                | 0.033°C/min                         |

### Recomendação Final:

    **Maceração A** é o processo recomendado (superior em 3 de 4 critérios)

⚠️ **Ponto de Atenção**: Comportamento térmico divergente requer investigação das causas raiz

## Contato

Para dúvidas ou sugestões sobre a análise, entre em contato.

---

** Última Atualização**: 05/02/2026  
** Análises Completas**: Maceração A, Maceração B e Comparativo A vs B  
** Sistema de Análise**: Python + Pandas + SciPy
