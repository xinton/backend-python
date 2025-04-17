import typer
from decimal import Decimal
from typing import Optional
from .repository import InventoryRepository
from .service import InventoryService

app = typer.Typer(help="Sistema de Gerenciamento de Inventário")
repo = InventoryRepository()
service = InventoryService(repo)

@app.callback()
def callback():
    """
    Sistema de Gerenciamento de Inventário - CLI
    """
    pass

@app.command()
def add(
    name: str = typer.Option(..., prompt=True, help="Nome do produto"),
    category: str = typer.Option(..., prompt=True, help="Categoria do produto"),
    price: float = typer.Option(..., prompt=True, help="Preço do produto"),
    quantity: int = typer.Option(..., prompt=True, help="Quantidade em estoque")
):
    """Adiciona um novo produto ao inventário"""
    try:
        service.add_product(name, category, Decimal(str(price)), quantity)
        typer.echo(f"Produto '{name}' adicionado com sucesso!")
    except ValueError as e:
        typer.echo(f"Erro: {e}", err=True)

@app.command()
def list():
    """Lista todos os produtos no inventário"""
    products = service.repository.get_all()
    if not products:
        typer.echo("Inventário vazio!")
        return
    
    for name, product in products.items():
        typer.echo(f"\nProduto: {name}")
        typer.echo(f"  Categoria: {product.category}")
        typer.echo(f"  Preço: R$ {product.price:.2f}")
        typer.echo(f"  Quantidade: {product.quantity}")

@app.command()
def remove(name: str = typer.Option(..., prompt=True, help="Nome do produto")):
    """Remove um produto do inventário"""
    if service.remove_product(name):
        typer.echo(f"Produto '{name}' removido com sucesso!")
    else:
        typer.echo(f"Produto '{name}' não encontrado.")

@app.command()
def search_category(
    category: str = typer.Option(..., prompt=True, help="Categoria a ser buscada")
):
    """Busca produtos por categoria"""
    products = service.get_by_category(category)
    if not products:
        typer.echo(f"Nenhum produto encontrado na categoria '{category}'.")
        return
    
    typer.echo(f"\nProdutos na categoria '{category}':")
    for product in products:
        typer.echo(f"- {product.name}: R$ {product.price:.2f}, Quantidade: {product.quantity}")

@app.command()
def most_expensive():
    """Exibe o produto mais caro do inventário"""
    product = service.get_most_expensive()
    if not product:
        typer.echo("O inventário está vazio!")
        return
    
    typer.echo(f"Produto mais caro: {product.name}, Preço: R$ {product.price:.2f}")

@app.command()
def below_stock(
    minimum: int = typer.Option(..., prompt=True, help="Quantidade mínima de estoque")
):
    """Lista produtos abaixo do estoque mínimo"""
    if minimum < 0:
        typer.echo("O estoque mínimo não pode ser negativo!")
        return
    
    products = service.get_below_stock(minimum)
    if not products:
        typer.echo(f"Nenhum produto abaixo do estoque mínimo de {minimum}.")
        return
    
    typer.echo(f"\nProdutos com estoque abaixo de {minimum}:")
    for product in products:
        typer.echo(f"- {product.name}: Quantidade: {product.quantity}")

def main():
    app()

if __name__ == "__main__":
    main()