class FoneP2:
    def conectar_p2(self):
        return "Tocando música via cabo analógico (P2)."


class FoneUSBC:
    def conectar_usb_c(self):
        return "Tocando música via conexão digital (USB-C)."


class CelularAntigo:
    def plugar_fone(self, fone):
        if isinstance(fone, FoneP2):
            print(f"✅ [Celular Antigo] Sucesso: {fone.conectar_p2()}")
        else:
            print("❌ [Celular Antigo] Erro: Este fone não encaixa. O celular só tem entrada P2.")


class CelularModerno:
    def plugar_fone(self, fone):
        if isinstance(fone, FoneUSBC):
            print(f"✅ [Celular Moderno] Sucesso: {fone.conectar_usb_c()}")
        else:
            print("❌ [Celular Moderno] Erro: Este fone não encaixa. O celular só tem entrada USB-C.")


def iniciarSimulacao():
    escolha_celular = input("Escolha o seu celular: \n1 - Celular Antigo (Entrada P2) \n2 - Celular Moderno (Entrada USB-C): ")
    if escolha_celular == '1':
        celular = CelularAntigo()
    else:
        celular = CelularModerno()

    escolha_fone = input("\nEscolha o seu fone de ouvido: \n1 - Fone Tradicional (Ponta P2) \n2 - Fone Novo (Ponta USB-C): ")
    if escolha_fone == '1':
        fone = FoneP2()
    else:
        fone = FoneUSBC()

    print("\n--- Tentando conectar o fone no celular... ---")
    celular.plugar_fone(fone)


if __name__ == "__main__":
    iniciarSimulacao()