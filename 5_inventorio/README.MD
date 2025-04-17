# Sistema de Gerenciamento de Inventário

Um sistema de linha de comando para gerenciar inventário de produtos, desenvolvido em Python usando arquitetura limpa e boas práticas de desenvolvimento.

## 🚀 Funcionalidades

- Adicionar produtos com nome, categoria, preço e quantidade
- Remover produtos do inventário
- Listar todos os produtos
- Buscar produtos por categoria
- Verificar produtos com baixo estoque
- Persistência de dados em arquivo JSON

## 📋 Pré-requisitos

- Python 3.10+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd inventorio
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
pip install -e .
```

## 💻 Uso

O sistema pode ser executado de duas formas:

1. Como módulo Python:
```bash
python -m inventorio.cli --help
```

2. Como comando do sistema:
```bash
inventorio --help
```

### Comandos disponíveis:

- Adicionar produto:
```bash
inventorio add
```

- Listar produtos:
```bash
inventorio list
```

- Remover produto:
```bash
inventorio remove
```

- Buscar por categoria:
```bash
inventorio search-category
```

- Ver produto mais caro:
```bash
inventorio most-expensive
```

- Ver produtos abaixo do estoque:
```bash
inventorio below-stock
```

Cada comando possui opções interativas e help:
```bash
# Ver ajuda específica do comando
inventorio <comando> --help
```

## 🏗️ Estrutura do Projeto

```
inventorio/
├── __init__.py      # Inicialização do pacote
├── models.py        # Definições de dados
├── repository.py    # Camada de persistência
├── service.py       # Lógica de negócio
├── cli.py          # Interface de linha de comando
└── tests/          # Testes automatizados
```

## 🧪 Testes

Execute os testes usando pytest:

```bash
python -m pytest
```

## 📦 Tecnologias Utilizadas

- [Typer](https://typer.tiangolo.com/) - CLI moderno
- [pytest](https://docs.pytest.org/) - Framework de testes
- [Python](https://www.python.org/) - Linguagem de programação

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 🔍 Exemplos de Uso

```bash
# Adicionar novo produto
inventorio add

# Listar todos os produtos
inventorio list

# Buscar produtos da categoria 'Eletrônicos'
inventorio search-category
> Digite a categoria a ser buscada: Eletrônicos

# Ver produto com maior preço
inventorio most-expensive

# Listar produtos com estoque baixo
inventorio below-stock
> Digite a quantidade mínima de estoque: 5
```

## 👥 Autor

- Bruno - *Desenvolvimento inicial* - [bruno](https://github.com/seu-usuario)