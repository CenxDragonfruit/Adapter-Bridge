class DeliveryComPix:
    def finalizar(self, lanche: str):
        print(f"🏍️ Entregando {lanche} em casa. Pagamento via PIX confirmado.")


class DeliveryComCartao:
    def finalizar(self, lanche: str):
        print(f"🏍️ Entregando {lanche} em casa. Levando a maquininha de Cartão.")


class RetiradaComPix:
    def finalizar(self, lanche: str):
        print(f"🛍️ {lanche} pronto para retirada balcão. Pagamento via PIX.")


class RetiradaComCartao:
    def finalizar(self, lanche: str):
        print(f"🛍️ {lanche} pronto para retirada balcão. Pagamento no Cartão.")


class ComerNoLocalComPix:
    def finalizar(self, lanche: str):
        print(f"🍽️ Servindo {lanche} na mesa 10. Pagamento via PIX.")


class ComerNoLocalComCartao:
    def finalizar(self, lanche: str):
        print(f"🍽️ Servindo {lanche} na mesa 10. Pagamento no Cartão.")


def main():
    print("🍔 --- APP DE DELIVERY --- 🍔")

    print("1 - Delivery | 2 - Retirada | 3 - Comer no Local")
    tipo = input("Escolha como quer receber: ")

    print("1 - Pix | 2 - Cartão")
    pag = input("Escolha como quer pagar: ")

    lanche = input("Qual o seu lanche? (ex: X-Bacon): ")
    print("\nProcessando...\n")

    if tipo == '1' and pag == '1':
        pedido = DeliveryComPix()
    elif tipo == '1' and pag == '2':
        pedido = DeliveryComCartao()
    elif tipo == '2' and pag == '1':
        pedido = RetiradaComPix()
    elif tipo == '2' and pag == '2':
        pedido = RetiradaComCartao()
    elif tipo == '3' and pag == '1':
        pedido = ComerNoLocalComPix()
    elif tipo == '3' and pag == '2':
        pedido = ComerNoLocalComCartao()
    else:
        return print("Opção inválida! Combinação não existe.")

    pedido.finalizar(lanche)

if __name__ == "__main__":
    main()