def fibonacci_iterativo(n):
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

def fibonacci_recursivo(n):
    if n <= 0:
        return "O valor de n deve ser um número positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def main():
    while True:
        try:
            print("\n1 - Modo Iterativo")
            print("2 - Modo Recursivo (não recomendada para números grandes)")
            print("0 - Sair")
            modo = input("Escolha o modo de cálculo: ")
            
            if modo == "0":
                print("Saindo...")
                break
                
            if modo not in ["1", "2"]:
                print("Opção inválida.")
                continue
                
            n = int(input("Digite o valor de n para calcular o n-ésimo número da sequência de Fibonacci: "))
            
            if n == 0:
                print("Saindo...")
                break
            elif n < 0:
                print("Por favor, insira um número positivo.")
            else:
                if modo == "1":
                    resultado = fibonacci_iterativo(n)
                else:
                    resultado = fibonacci_recursivo(n)
                print(f"O {n}º número da sequência de Fibonacci é: {resultado}")
                
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Chama a função principal
if __name__ == "__main__":
    main()
