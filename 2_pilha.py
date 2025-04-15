from typing import Any

class Pilha:
    def __init__(self):
        self._dados = []

    def append(self, item: Any) -> None:
        self._dados.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop de pilha vazia")
        return self._dados.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek de pilha vazia")
        return self._dados[-1]

    def is_empty(self) -> bool:
        return len(self._dados) == 0

    def size(self) -> int:
        return len(self._dados)

def rodar_testes():
    pilha = Pilha()
    pilha.append(10)
    pilha.append(20)
    assert pilha.is_empty() is False
    assert pilha.peek() == 20
    assert pilha.size() == 2
    assert pilha.pop() == 20
    assert pilha.pop() == 10
    assert pilha.is_empty() is True
    print("✅ Todos os testes da pilha passaram.")

def menu_interativo():
    pilha = Pilha()
    print("\nModo interativo - Pilha em Python")
    while True:
        print("\n1 - Adicionar item")
        print("2 - Remover item (pop)")
        print("3 - Ver topo (peek)")
        print("4 - Verificar se está vazia")
        print("5 - Tamanho da pilha")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                item = input("Digite o valor a adicionar: ")
                pilha.append(item)
            elif opcao == "2":
                print("Item removido:", pilha.pop())
            elif opcao == "3":
                print("Topo da pilha:", pilha.peek())
            elif opcao == "4":
                print("Está vazia?", pilha.is_empty())
            elif opcao == "5":
                print("Tamanho da pilha:", pilha.size())
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    rodar_testes()
    usar_interativo = input("\nDeseja entrar no modo interativo? (s/n): ").lower()
    if usar_interativo == "s":
        menu_interativo()