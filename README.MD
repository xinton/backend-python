# Prova Admissional - Backend

Este repositório contém a solução para os 5 exercícios propostos na prova para a vaga de desenvolvedor backend.

## Como executar os exercícios

1. Tenha o Python 3 instalado. Você pode verificar com:
   ```bash
   python --version
   ```

2. Execute cada exercício conforme instruções específicas abaixo.

## Descrição dos exercícios

### 1. Análise de PLD (1_maior_valor_pld/)
Pacote Python para análise de preços PLD por submercado. Ver instruções detalhadas em `1_maior_valor_pld/README.md`
```bash
cd 1_maior_valor_pld
pip install -e .
python pld_analyzer/maior_valor_pld.py
```

### 2. Implementação de Pilha (2_pilha.py)
Implementa uma pilha com operações básicas usando lista nativa:
```bash
python3 2_pilha.py
```

### 3. Contador de Palavras (3_contar_palavras.py)
Lê palavras do terminal ou arquivo .txt:
```bash
python3 3_contar_palavras.py
```

### 4. Fibonacci (4_fibonacci.py)
Calcula números da sequência de Fibonacci:
```bash
python3 4_fibonacci.py
```

### 5. Sistema de Inventário (5_inventorio/)
Sistema completo de gerenciamento de inventário. Ver instruções detalhadas em `5_inventorio/README.md`
```bash
cd 5_inventorio
pip install -e .
inventorio --help
```

## Estrutura do Projeto

```
prova_backend/
├── 1_maior_valor_pld/     # Pacote de análise PLD
├── 2_pilha.py            # Implementação de pilha
├── 3_contar_palavras.py  # Contador de palavras
├── 4_fibonacci.py        # Calculadora Fibonacci
├── 5_inventorio/         # Sistema de inventário
└── README.md            # Este arquivo
```

## Ambiente Virtual (recomendado)

Para melhor isolamento, use um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate
```

## Dependências Globais

Algumas dependências comuns a múltiplos exercícios:
```bash
pip install pandas openpyxl pytest typer
```

---

Cada exercício possui sua própria documentação detalhada quando relevante. Consulte os READMEs específicos em `1_maior_valor_pld/` e `5_inventorio/` para mais detalhes sobre estes módulos.

---

Caso tenha qualquer dúvida sobre a execução ou estrutura, fico à disposição!
