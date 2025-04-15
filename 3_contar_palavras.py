def contar_palavras(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

def ler_arquivo(nome_arquivo):
    # Adiciona extensão .txt se não existir
    if not nome_arquivo.lower().endswith('.txt'):
        nome_arquivo += '.txt'
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            return texto.strip().split()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None

# Função interativa
def main():
    print("\nEscolha o modo de entrada:")
    print("1 - Digite as palavras manualmente")
    print("2 - Ler de um arquivo .txt")
    
    modo = input("Opção (1 ou 2): ")
    
    if modo == "1":
        entrada = input("Digite as palavras separadas por espaço: ")
        palavras = entrada.strip().split()
    elif modo == "2":
        nome_arquivo = input("Digite o caminho do arquivo .txt: ")
        palavras = ler_arquivo(nome_arquivo)
        if palavras is None:
            return
    else:
        print("Opção inválida.")
        return
    
    resultado = contar_palavras(palavras)
    print("\nContagem de palavras:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")

# Chama a função principal
if __name__ == "__main__":
    main()