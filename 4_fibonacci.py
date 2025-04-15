def fibonacci(n):
    if n <= 0:
        return "O valor de n deve ser um número positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    
    return b

# Função interativa
def main():
    while True:
        try:
            n = int(input("Digite o valor de n para calcular o n-ésimo número da sequência de Fibonacci (ou '0' para sair): "))
            if n == 0:
                print("Saindo...")
                break
            elif n < 0:
                print("Por favor, insira um número positivo.")
            else:
                print(f"O {n}º número da sequência de Fibonacci é: {fibonacci(n)}")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Chama a função principal
if __name__ == "__main__":
    main()
