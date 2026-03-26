# 🌉 Padrão de Projeto: Bridge (Ponte)

Este repositório demonstra, de forma interativa e com rigor acadêmico, o padrão de projeto estrutural **Bridge**. 

O objetivo principal deste padrão é separar a **Abstração** (o que o objeto é) da sua **Implementação** (do que ele é feito ou como se comporta), permitindo que ambas as hierarquias evoluam de forma independente. Isso evita o temido problema da "explosão de classes" (crescimento exponencial de arquivos no sistema).

---

## 🚨 O Problema

Quando utilizamos apenas herança simples para modelar características múltiplas (como *Formas* e *Cores*), criamos um acoplamento rígido. Para cada nova combinação, somos obrigados a criar uma nova classe filha. 

Isso gera um crescimento de complexidade $O(N^2)$ (Produto Cartesiano). No exemplo abaixo, temos 3 formas e 3 cores, resultando em **9 classes filhas** diretas da classe pai `Forma`.

<details>
<summary><b>Clique para ver o código SEM Bridge (A Abordagem Rígida)</b></summary>

```python
from abc import ABC, abstractmethod

# 1. A CLASSE PAI (A Abstração base)
class Forma(ABC):
    @abstractmethod
    def desenhar(self) -> None:
        pass

# 2. AS 9 CLASSES FILHAS (O Problema do Produto Cartesiano)
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

if __name__ == "__main__":
    print("\n--- SISTEMA DE DESENHO (SEM BRIDGE) ---")
    op_forma = input("Escolha a Forma (1. Círculo | 2. Quadrado | 3. Triângulo): ")
    op_cor = input("Escolha a Cor (1. Vermelho | 2. Azul | 3. Verde): ")

    forma_obj: Forma
    
    # Avaliação rígida cruzando as opções
    if op_forma == '1' and op_cor == '1': forma_obj = CirculoVermelho()
    elif op_forma == '1' and op_cor == '2': forma_obj = CirculoAzul()
    elif op_forma == '1' and op_cor == '3': forma_obj = CirculoVerde()
    elif op_forma == '2' and op_cor == '1': forma_obj = QuadradoVermelho()
    elif op_forma == '2' and op_cor == '2': forma_obj = QuadradoAzul()
    elif op_forma == '2' and op_cor == '3': forma_obj = QuadradoVerde()
    elif op_forma == '3' and op_cor == '1': forma_obj = TrianguloVermelho()
    elif op_forma == '3' and op_cor == '2': forma_obj = TrianguloAzul()
    elif op_forma == '3' and op_cor == '3': forma_obj = TrianguloVerde()
    else: exit(print("Opção inválida."))

    forma_obj.desenhar()
````
-----

## ✅ A Solução

O padrão Bridge resolve isso favorecendo a **Composição** em vez da Herança. Nós separamos a lógica em duas hierarquias de classes independentes e criamos uma "Ponte" (uma variável de referência) entre elas. O crescimento da complexidade cai para $O(N)$ (Crescimento Linear).

### 🧩 Arquitetura do Código

1.  **A Implementação (`Cor`):** Criamos uma interface base (`ABC`) com o método abstrato `get_nome()`. As classes filhas (`CorVermelha`, `CorAzul`, `CorVerde`) implementam esse contrato. Elas não sabem nada sobre formas geométricas.
2.  **A Abstração (`Forma`):** Criamos outra interface base. O grande diferencial está no construtor `__init__`, que recebe um objeto do tipo `Cor`. **Esta é a Ponte\!** A Forma não herda a cor, ela *contém* a cor.
3.  **O Código Cliente:** O menu interativo recolhe as escolhas, instancia a peça de cor escolhida e "pluga" essa peça dentro da forma selecionada na hora da execução.

### 💻 Código Principal

```python
from abc import ABC, abstractmethod

# ==========================================
# 1. A IMPLEMENTAÇÃO (Classes Pai e Filhas das Cores)
# ==========================================
class Cor(ABC):
    @abstractmethod
    def get_nome(self) -> str:
        pass

class CorVermelha(Cor):
    def get_nome(self) -> str: return "Vermelho"

class CorAzul(Cor):
    def get_nome(self) -> str: return "Azul"

class CorVerde(Cor):
    def get_nome(self) -> str: return "Verde"

# ==========================================
# 2. A ABSTRAÇÃO (Classes Pai e Filhas das Formas)
# ==========================================
class Forma(ABC):
    def __init__(self, cor: Cor) -> None:
        self.cor = cor  # <--- A Ponte (Bridge) oficial!

    @abstractmethod
    def desenhar(self) -> None:
        pass

class Circulo(Forma):
    def desenhar(self) -> None:
        print(f"Desenhando um Círculo {self.cor.get_nome()}")

class Quadrado(Forma):
    def desenhar(self) -> None:
        print(f"Desenhando um Quadrado {self.cor.get_nome()}")

class Triangulo(Forma):
    def desenhar(self) -> None:
        print(f"Desenhando um Triângulo {self.cor.get_nome()}")

# ==========================================
# 3. O MENU INTERATIVO (Código Cliente)
# ==========================================
if __name__ == "__main__":
    print("\n--- SISTEMA DE DESENHO (COM BRIDGE) ---")
    op_forma = input("Escolha a Forma (1. Círculo | 2. Quadrado | 3. Triângulo): ")
    op_cor = input("Escolha a Cor (1. Vermelho | 2. Azul | 3. Verde): ")

    # 1. Instancia a classe filha da Implementação
    cor_obj: Cor
    if op_cor == '1': cor_obj = CorVermelha()
    elif op_cor == '2': cor_obj = CorAzul()
    elif op_cor == '3': cor_obj = CorVerde()
    else: exit(print("Cor inválida."))

    # 2. Instancia a classe filha da Abstração, passando a ponte
    forma_obj: Forma
    if op_forma == '1': forma_obj = Circulo(cor_obj)
    elif op_forma == '2': forma_obj = Quadrado(cor_obj)
    elif op_forma == '3': forma_obj = Triangulo(cor_obj)
    else: exit(print("Forma inválida."))

    # 3. Executa a operação delegando o trabalho dinamicamente
    forma_obj.desenhar()
```

-----

## ⚙️ Como Executar

1.  Tenha o [Python](https://www.python.org/downloads/) instalado.
2.  Salve os exemplos acima em arquivos `.py` (ex: `bridge.py` e `sem_bridge.py`).
3.  Execute no terminal:
    ```bash
    python bridge.py
    ```
4.  Observe que a experiência de uso no terminal é idêntica para ambos, provando que o padrão de projeto altera a **arquitetura interna** e a manutenibilidade, mas mantém o contrato com o usuário intacto.
