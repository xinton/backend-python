def adicionar_produto(inventario):
    """Adiciona um novo produto ao inventário ou atualiza a quantidade se já existir."""
    try:
        nome = input("Digite o nome do produto: ").strip()
        if not nome:
            print("Nome do produto não pode ser vazio!")
            return
        
        # Verifica se o produto já existe
        if nome in inventario:
            quantidade_atual = inventario[nome]["quantidade"]
            
            try:
                quantidade_adicional = int(input(f"Produto já existe. Quantidade atual: {quantidade_atual}. "
                                           f"Digite a quantidade adicional: "))
                if quantidade_adicional < 0:
                    print("Quantidade não pode ser negativa!")
                    return
                
                inventario[nome]["quantidade"] += quantidade_adicional
                print(f"Quantidade de {nome} atualizada para {inventario[nome]['quantidade']}.")
            except ValueError:
                print("Quantidade inválida! Por favor, digite um número inteiro.")
        else:
            # Novo produto
            categoria = input("Digite a categoria do produto: ").strip()
            if not categoria:
                print("Categoria não pode ser vazia!")
                return
            
            try:
                preco = float(input("Digite o preço do produto: "))
                if preco <= 0:
                    print("Preço deve ser maior que zero!")
                    return
                
                quantidade = int(input("Digite a quantidade em estoque: "))
                if quantidade < 0:
                    print("Quantidade não pode ser negativa!")
                    return
                
                # Adiciona o produto ao inventário
                inventario[nome] = {
                    "categoria": categoria,
                    "preco": preco,
                    "quantidade": quantidade
                }
                
                print(f"Produto '{nome}' adicionado com sucesso!")
            except ValueError:
                print("Entrada inválida! Preço deve ser um número e quantidade um inteiro.")
    except Exception as e:
        print(f"Erro ao adicionar produto: {e}")

def remover_produto(inventario):
    """Remove um produto do inventário com base no nome."""
    try:
        nome = input("Digite o nome do produto a ser removido: ").strip()
        
        if nome in inventario:
            del inventario[nome]
            print(f"Produto '{nome}' removido com sucesso!")
        else:
            print(f"Produto '{nome}' não encontrado no inventário.")
    except Exception as e:
        print(f"Erro ao remover produto: {e}")

def exibir_inventario(inventario):
    """Exibe todos os produtos no inventário."""
    try:
        if not inventario:
            print("O inventário está vazio!")
            return
        
        print("\n===== INVENTÁRIO ATUAL =====")
        for nome, info in inventario.items():
            print(f"Produto: {nome}")
            print(f"  Categoria: {info['categoria']}")
            print(f"  Preço: R$ {info['preco']:.2f}")
            print(f"  Quantidade: {info['quantidade']}")
            print("-" * 30)
    except Exception as e:
        print(f"Erro ao exibir inventário: {e}")

def menu_principal():
    """Exibe o menu principal e gerencia o fluxo do programa."""
    inventario = {}
    
    while True:
        print("\n===== SISTEMA DE GERENCIAMENTO DE INVENTÁRIO =====")
        print("1. Adicionar um produto")
        print("2. Remover um produto")
        print("3. Buscar produtos por categoria")
        print("4. Exibir o produto mais caro")
        print("5. Exibir produtos abaixo de um estoque mínimo")
        print("6. Exibir todo o inventário")
        print("0. Sair")
        
        try:
            opcao = input("\nEscolha uma opção: ")
            
            match opcao:
                case "1":
                    adicionar_produto(inventario)
                case "2":
                    remover_produto(inventario)                  
                case "3":
                    print("buscar_por_categoria(inventario)")                    
                case "4":
                    print("produto_mais_caro(inventario)")                    
                case "5":
                    print("produtos_abaixo_estoque(inventario)")
                case "6":
                    exibir_inventario(inventario)
                case "0":
                    print("Saindo do sistema. Até logo!")
                    break
                case _:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Gerenciamento de Inventário!")
    menu_principal()