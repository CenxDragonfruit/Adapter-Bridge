from abc import ABC, abstractmethod

# ==========================================
# 1. A IMPLEMENTAÇÃO (Classes Pai e Filhas das Cores)
# ==========================================

# Classe Pai (Interface de Implementação)
class Cor(ABC):
    @abstractmethod
    def get_nome(self) -> str:
        pass

# Classes Filhas (Implementações Concretas)
class CorVermelha(Cor):
    def get_nome(self) -> str: return "Vermelho"

class CorAzul(Cor):
    def get_nome(self) -> str: return "Azul"

class CorVerde(Cor):
    def get_nome(self) -> str: return "Verde"


# ==========================================
# 2. A ABSTRAÇÃO (Classes Pai e Filhas das Formas)
# ==========================================

# Classe Pai (A Abstração que contém a "Ponte")
class Forma(ABC):
    def __init__(self, cor: Cor) -> None:
        self.cor = cor

    @abstractmethod
    def desenhar(self) -> None:
        pass

# Classes Filhas (Abstrações Refinadas)
class Circulo(Forma):
    def desenhar(self) -> None:
        # Delega o trabalho da cor para o objeto implementado
        print(f"Desenhando um Círculo {self.cor.get_nome()}")

class Quadrado(Forma):
    def desenhar(self) -> None:
        print(f"Desenhando um Quadrado {self.cor.get_nome()}")

class Triangulo(Forma):
    def desenhar(self) -> None:
        print(f"Desenhando um Triângulo {self.cor.get_nome()}")


# ==========================================
# 3. O MENU INTERATIVO
# ==========================================
if __name__ == "__main__":
    print("\n--- SISTEMA DE DESENHO ---")
    print("Passo 1: Escolha a Forma")
    print("1. Círculo  |  2. Quadrado  |  3. Triângulo")
    op_forma = input("Digite o número da Forma: ")

    print("\nPasso 2: Escolha a Cor")
    print("1. Vermelho |  2. Azul      |  3. Verde")
    op_cor = input("Digite o número da Cor: ")

    print("\nResultado:")

    # 1. Instancia a classe filha da Implementação
    cor_obj: Cor
    if op_cor == '1': cor_obj = CorVermelha()
    elif op_cor == '2': cor_obj = CorAzul()
    elif op_cor == '3': cor_obj = CorVerde()
    else:
        print("Cor inválida.")
        exit()

    # 2. Instancia a classe filha da Abstração, passando a ponte
    forma_obj: Forma
    if op_forma == '1': forma_obj = Circulo(cor_obj)
    elif op_forma == '2': forma_obj = Quadrado(cor_obj)
    elif op_forma == '3': forma_obj = Triangulo(cor_obj)
    else:
        print("Forma inválida.")
        exit()

    # 3. Executa a operação
    forma_obj.desenhar()