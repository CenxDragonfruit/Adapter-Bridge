from abc import ABC, abstractmethod


# ==========================================
# A HIERARQUIA RÍGIDA (Sem Bridge)
# ==========================================

# 1. A CLASSE PAI (A Abstração base)
class Forma(ABC):
    @abstractmethod
    def desenhar(self) -> None:
        pass


# 2. AS 9 CLASSES FILHAS (O Problema do Produto Cartesiano)
# Note que a Cor e a Forma estão rigidamente unidas na mesma classe.

class CirculoVermelho(Forma):
    def desenhar(self) -> None: print("Desenhando um Círculo Vermelho")


class CirculoAzul(Forma):
    def desenhar(self) -> None: print("Desenhando um Círculo Azul")


class CirculoVerde(Forma):
    def desenhar(self) -> None: print("Desenhando um Círculo Verde")


class QuadradoVermelho(Forma):
    def desenhar(self) -> None: print("Desenhando um Quadrado Vermelho")


class QuadradoAzul(Forma):
    def desenhar(self) -> None: print("Desenhando um Quadrado Azul")


class QuadradoVerde(Forma):
    def desenhar(self) -> None: print("Desenhando um Quadrado Verde")


class TrianguloVermelho(Forma):
    def desenhar(self) -> None: print("Desenhando um Triângulo Vermelho")


class TrianguloAzul(Forma):
    def desenhar(self) -> None: print("Desenhando um Triângulo Azul")


class TrianguloVerde(Forma):
    def desenhar(self) -> None: print("Desenhando um Triângulo Verde")


# ==========================================
# 3. O MENU INTERATIVO (Código Cliente)
# ==========================================
if __name__ == "__main__":
    print("\n--- SISTEMA DE DESENHO (SEM BRIDGE) ---")
    print("Passo 1: Escolha a Forma")
    print("1. Círculo  |  2. Quadrado  |  3. Triângulo")
    op_forma = input("Digite o número da Forma: ")

    print("\nPasso 2: Escolha a Cor")
    print("1. Vermelho |  2. Azul      |  3. Verde")
    op_cor = input("Digite o número da Cor: ")

    print("\nResultado:")

    # Instancia a classe filha engessada com base em uma cadeia gigantesca de IFs
    forma_obj: Forma

    if op_forma == '1' and op_cor == '1':
        forma_obj = CirculoVermelho()
    elif op_forma == '1' and op_cor == '2':
        forma_obj = CirculoAzul()
    elif op_forma == '1' and op_cor == '3':
        forma_obj = CirculoVerde()

    elif op_forma == '2' and op_cor == '1':
        forma_obj = QuadradoVermelho()
    elif op_forma == '2' and op_cor == '2':
        forma_obj = QuadradoAzul()
    elif op_forma == '2' and op_cor == '3':
        forma_obj = QuadradoVerde()

    elif op_forma == '3' and op_cor == '1':
        forma_obj = TrianguloVermelho()
    elif op_forma == '3' and op_cor == '2':
        forma_obj = TrianguloAzul()
    elif op_forma == '3' and op_cor == '3':
        forma_obj = TrianguloVerde()

    else:
        print("Opção inválida.")
        exit()

    # Executa a operação garantida pelo contrato da Classe Pai
    forma_obj.desenhar()