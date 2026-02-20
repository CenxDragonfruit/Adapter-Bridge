class FoneP2:
    def conectar_p2(self):
        return "Tocando música via cabo analógico (P2)."


class CelularAntigo:
    def plugar_fone(self, fone):
        if isinstance(fone, FoneP2):
            print(f"✅ [Celular Antigo] Sucesso: {fone.conectar_p2()}")
        else:
            print("❌ [Celular Antigo] Erro: Fone incompatível. Entrada exclusiva para P2.")

class FoneP2Decorator(FoneP2):
    def __init__(self, fone_embrulhado):
        self.fone = fone_embrulhado

    def conectar_p2(self):
        return self.fone.conectar_p2()


class IsolamentoAcustico(FoneP2Decorator):
    def conectar_p2(self):
        som_original = self.fone.conectar_p2()
        return f"{som_original} 🔇 [Filtro de Ruído Ativado]"


class AmplificadorDeGrave(FoneP2Decorator):
    def conectar_p2(self):
        som_original = self.fone.conectar_p2()
        return f"{som_original} 🔊 [Graves no Talo!]"


def iniciarSimulacaoDecorator():
    meu_celular = CelularAntigo()

    print("--- 1. FONE PADRÃO ---")
    fone_simples = FoneP2()
    meu_celular.plugar_fone(fone_simples)

    print("\n--- 2. FONE COM ISOLAMENTO ---")
    # Embrulhamos o fone simples no isolamento
    fone_isolado = IsolamentoAcustico(fone_simples)
    meu_celular.plugar_fone(fone_isolado)

    print("\n--- 3. FONE MONSTRO (ISOLAMENTO + GRAVES) ---")
    # Embrulhamos o fone que JÁ TEM isolamento dentro do amplificador
    fone_monstro = AmplificadorDeGrave(fone_isolado)
    meu_celular.plugar_fone(fone_monstro)


if __name__ == "__main__":
    iniciarSimulacaoDecorator()