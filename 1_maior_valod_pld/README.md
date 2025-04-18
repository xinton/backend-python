# Análise de Preços PLD por Submercado

Script Python para análise de preços PLD (Preço de Liquidação das Diferenças) por submercado, extraindo os valores máximos anuais de uma planilha Excel.

## Funcionalidades

- Leitura de arquivo Excel com dados PLD
- Processamento de dados por submercado
- Cálculo do maior valor anual por submercado
- Tratamento de dados ausentes ou inválidos
- Exibição formatada dos resultados

## Pré-requisitos

- Python 3.8+
- pandas
- openpyxl

## Instalação

1. Instale as dependências:
```bash
pip install pandas openpyxl
```

2. Coloque seu arquivo `PLD.xlsx` no mesmo diretório do script.

## Estrutura de Arquivos

Coloque o arquivo `PLD.xlsx` na pasta raiz do projeto:

```
1_maior_valor_pld/
├── PLD.xlsx           <- Arquivo de dados aqui
├── setup.py
└── pld_analyzer/
    ├── __init__.py
    ├── maior_valor_pld.py
    └── tests/
```

## Uso

Execute o script diretamente:
```bash
python maior_valor_pld.py
```

## Executando

1. Certifique-se de que o arquivo `PLD.xlsx` está na pasta correta
2. Execute o script:
```bash
cd 1_maior_valor_pld
python pld_analyzer/maior_valor_pld.py
```

### Formato do Excel Esperado

O arquivo Excel deve seguir a estrutura:
- Primeira linha: datas
- Primeira coluna: identificadores
- Segunda coluna: nomes dos submercados
- Demais células: valores PLD

Exemplo:
```
     A      B         C        D        E
1    -      -     01/2023  02/2023  03/2023
2    -   SUDESTE   100.50   150.20   200.30
3    -   SUL       98.40    145.30   198.20
4    -   NORDESTE  102.30   155.40   205.10
5    -   NORTE     99.20    148.90   199.40
```

## 🧪 Testes

Execute os testes com pytest:
```bash
python -m pytest test_maior_valor_pld.py -v
```

## Tratamento de Dados

- Valores ausentes (NaN) são ignorados
- Anos incompletos são processados normalmente
- Erros de conversão são tratados silenciosamente

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.