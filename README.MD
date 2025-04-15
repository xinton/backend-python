# ========================
# README.md

# Prova Admissional - Backend - Ludfor

Este repositório contém a solução para os 5 exercícios propostos na prova para a vaga de desenvolvedor backend.

## Como executar os exercícios

1. Tenha o Python 3 instalado. Você pode verificar com:
   ```bash
   python --version
   ```

2. Execute qualquer um dos scripts com:
   ```bash
   python nome_do_arquivo.py
   ```

Exemplo:
```bash
python 3_contar_palavras.py
```

## Descrição dos arquivos

- `1_maior_valor_pld.py`: Lê a planilha PLD.xlsx no formato fornecido e imprime o maior valor de cada submercado por ano. Requer a instalação das bibliotecas `pandas` e `openpyxl`:
  ```bash
  pip install pandas openpyxl
  ```
- `2_pilha.py`: Implementa uma pilha com operações básicas usando lista nativa. Inclui testes automatizados com `assert` e um modo interativo opcional para executar operações via terminal.
- `3_contar_palavras.py`: Lê palavras do terminal e conta quantas vezes cada uma aparece.
- `4_fibonacci.py`: Calcula o n-ésimo número da sequência de Fibonacci com dois modos de execução:
  - Modo Iterativo: Implementação eficiente com complexidade O(n) e memória constante O(1)
  - Modo Recursivo: Implementação didática com complexidade O(2^n), não recomendada para números grandes devido à recursão múltipla
  ```bash
  python 4_fibonacci.py
  ```
- `5_inventario.py`: Sistema de gerenciamento de inventário com menu interativo.

---

Cada script é autocontido e pode ser executado individualmente.

Comentários, validações de entrada e estruturação foram feitos com foco em clareza, boas práticas e legibilidade. Testes e tipagem foram adicionados pontualmente para evidenciar familiaridade com boas práticas de código Python moderno.

---

Caso tenha qualquer dúvida sobre a execução ou estrutura, fico à disposição!
