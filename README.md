# Análise de Maceração: Temperatura ⇄ Tempo

## Sobre o Projeto

Este projeto apresenta uma **análise bidirecional
completa** da relação entre **Temperatura** e **Tempo de Maceração** no processo industrial.

### 🔬 Análise Realizada

- **Período**: Novembro/2024 - Janeiro/2026 (7 meses)
- **Processo**: Maceração A
- **Tipo**: Regressão Linear bidirecional

- **Correlação**: -0.684 (moderada a forte)

## Duas Perspectivas

### Perspectiva 1: Temperatura → Tempo

- Cada 1°C de aumento reduz ~5.74 minutos
- R² = 46.8%
- Recomendação: Setpoint de 50°C

### Perspectiva 2: Tempo → Temperatura

**Perda Térmica Passiva**: Processos longos causam perda de calor

- Taxa de resfriamento: 0.0815°C por minuto
- R² = 46.8%
- Recomendação: Isolamento térmico ou reaquecimento

## Visualizar Relatório

** Online (GitHub Pages)**: [Clique aqui para ver o relatório](https://wilian-lab.github.io/rastreio-maceracao/relatorios/relatorio_completo_tempo_temperatura_20260205_1622.html)

** Local**: Abra o arquivo `relatorio_completo_tempo_temperatura_20260205_1622.html` no navegador

## Conteúdo do Relatório

✅ Estatísticas descritivas completas  
✅ Gráficos de evolução temporal  
✅ Análise de regressão (ambas perspectivas)  
✅ Gráficos de dispersão com linha de tendência  
✅ Comparativo lado a lado  
✅ Recomendações operacionais estratégicas

## Tecnologias Utilizadas

- **Python 3.12**: Análise de dados
- **Pandas**: Manipulação de dados
- **Matplotlib & Seaborn**: Visualizações
- **Scipy**: Análise estatística
- **Jupyter Notebook**: Desenvolvimento interativo

## Estrutura do Projeto

```
Rastreio-masceracao/
│
├── tempo_x_temperatura.ipynb          # Notebook principal com análise
├── relatorio_completo_*.html          # Relatório completo gerado
├── index.html                         # Página inicial para GitHub Pages
├── README.md                          # Este arquivo
│
├── dados_brutos/                      # Dados originais
│   └── Dados maceração.xlsx
│
└── relatorios_anteriores/             # Versões anteriores (opcional)
```

## Como Usar

### Para Visualizar:

1. Clone o repositório
2. Abra o arquivo HTML no navegador
3. Ou acesse o link do GitHub Pages

### Para Reproduzir a Análise:

1. Abra `tempo_x_temperatura.ipynb` no Jupyter/VS Code
2. Execute as células sequencialmente
3. Novo relatório será gerado automaticamente

## Contato

Para dúvidas ou sugestões sobre a análise, entre em contato.

---

** Última Atualização**: 05/02/2026  
** Relatório Gerado**: Sistema de Análise Python
