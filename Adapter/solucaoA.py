class FoneP2:
    def conectar_p2(self):
        return "Tocando música via cabo analógico (P2)."


class FoneUSBC:
    def conectar_usb_c(self):
        return "Tocando música via conexão digital (USB-C)."


class AdaptadorUniversal(FoneP2, FoneUSBC):
    def __init__(self, fone):
        self.fone = fone

    def conectar_p2(self):
        if isinstance(self.fone, FoneP2):
            return self.fone.conectar_p2()
        else:
            print("🎧 [Adaptador] Convertendo Fone USB-C para entrada P2...")
            return self.fone.conectar_usb_c()

    def conectar_usb_c(self):
        if isinstance(self.fone, FoneUSBC):
            return self.fone.conectar_usb_c()
        else:
            print("🎧 [Adaptador] Convertendo Fone P2 para entrada USB-C...")
            return self.fone.conectar_p2()


class CelularAntigo:
    def plugar_fone(self, fone):
        if isinstance(fone, FoneP2):
            print(f"✅ [Celular Antigo] Sucesso: {fone.conectar_p2()}")
        else:
            print("❌ [Celular Antigo] Erro: Fone incompatível. Entrada exclusiva para P2.")


class CelularModerno:
    def plugar_fone(self, fone):
        if isinstance(fone, FoneUSBC):
            print(f"✅ [Celular Moderno] Sucesso: {fone.conectar_usb_c()}")
        else:
            print("❌ [Celular Moderno] Erro: Fone incompatível. Entrada exclusiva para USB-C.")


def iniciarSimulacao():

    escolha_celular = input("Escolha o seu celular:\n1 - Celular Antigo (Entrada P2)\n2 - Celular Moderno (Entrada USB-C)\nSua escolha: ")

    if escolha_celular == '1':
        celular = CelularAntigo()
    else:
        celular = CelularModerno()


    escolha_fone = input("\nEscolha o seu fone de ouvido:\n1 - Fone Tradicional (Ponta P2)\n2 - Fone Novo (Ponta USB-C)\nSua escolha: ")

    if escolha_fone == '1':
        fone_escolhido = FoneP2()
    else:
        fone_escolhido = FoneUSBC()

    usar_adaptador = input("\nVocê quer conectar o fone no ADAPTADOR UNIVERSAL antes de plugar no celular? (s/n): ")

    if usar_adaptador.lower() == 's':
        fone_final = AdaptadorUniversal(fone_escolhido)
        print("\n[Aviso] Fone conectado ao adaptador!")
    else:
        fone_final = fone_escolhido
        print("\n[Aviso] Fone indo direto para o celular sem adaptador!")

    print("\n--- Tentando conectar no celular... ---")
    celular.plugar_fone(fone_final)


if __name__ == "__main__":
    iniciarSimulacao()