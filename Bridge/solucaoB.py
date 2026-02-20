# PAGAMENTOS

class Pix:
    def processar(self):
        return "PIX"


class Cartao:
    def processar(self):
        return "Cartão"


# ENTREGAS

class PedidoDelivery:
    def __init__(self, forma_pagamento):
        self.pagamento = forma_pagamento

    def finalizar(self, lanche):
        status = self.pagamento.processar()
        print(f"🏍️ [DELIVERY] Levando seu {lanche}. \nMétodo de Pagamento: {status}.")


class PedidoRetirada:
    def __init__(self, forma_pagamento):
        self.pagamento = forma_pagamento

    def finalizar(self, lanche):
        status = self.pagamento.processar()
        print(f"🛍️ [RETIRADA] Seu {lanche} está no balcão. \nMétodo de Pagamento: {status}.")


class ComerNoLocal:
    def __init__(self, forma_pagamento):
        self.pagamento = forma_pagamento

    def finalizar(self, lanche):
        status = self.pagamento.processar()
        print(f"🍽️ [COMER NO LOCAL] Servindo {lanche} na mesa 10. \nMétodo de Pagamento: {status}.")


# USUÁRIO

def main():
    print("🍔 --- APP DE DELIVERY --- 🍔")

    opcao_pag = input("Como deseja pagar? (1 - Pix, 2 - Cartão): ")
    if opcao_pag == '1':
        meu_pagamento = Pix()
    else:
        meu_pagamento = Cartao()

    opcao_entrega = input("Como quer receber? (1 - Delivery, 2 - Comer no Local, 3 - Retirada): ")
    if opcao_entrega == '1':
        meu_pedido = PedidoDelivery(meu_pagamento)
    elif opcao_entrega == '2':
        meu_pedido = ComerNoLocal(meu_pagamento)
    else:
        meu_pedido = PedidoRetirada(meu_pagamento)

    lanche = input("Qual o seu lanche? (ex: X-Bacon): ")

    print("\nProcessando pedido...")
    meu_pedido.finalizar(lanche)


if __name__ == "__main__":
    main()