def contar_palavras(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

# Função interativa
def main():
    entrada = input("Digite as palavras separadas por espaço: ")
    palavras = entrada.strip().split()
    resultado = contar_palavras(palavras)
    print("\nContagem de palavras:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")

# Chama a função principal
if __name__ == "__main__":
    main()