class Target:
    """A interface (Target) que o sistema cliente já usa e entende."""

    def request(self, dados: str) -> str:
        return f"Target: Comportamento padrão processando {dados}"


class Adaptee:
    """O serviço (Adaptee) incompatível que precisa de adaptação."""

    def specific_request(self, dados_json: str) -> str:
        if "<" in dados_json:
            raise ValueError("Erro: Formato XML não suportado.")
        return f"Adaptee: Gráficos gerados com os dados: {dados_json}"


class Adapter(Target, Adaptee):
    """O Adaptador herda as características e faz a ponte (tradução)."""

    def request(self, dados_xml: str) -> str:
        print("Adapter: (TRADUZINDO) Convertendo XML para JSON nos bastidores...")
        # Simula a lógica de conversão de dados
        dados_convertidos_json = '{"acao": "AAPL", "valor": 150}'

        # Chama o método do Adaptee com o formato correto
        return self.specific_request(dados_convertidos_json)


def client_code(target: "Target", dados: str) -> None:
    """O código cliente trabalha com qualquer classe que siga a interface Target."""
    print(target.request(dados), end="\n\n")


if __name__ == "__main__":
    dados_da_bolsa_xml = "<acoes><acao>AAPL</acao><valor>150</valor></acoes>"

    print("Cliente: Trabalhando perfeitamente com o Adapter:")
    # O cliente instância o Adaptador achando que é um Target comum
    adaptador = Adapter()

    # O cliente envia o XML, o adaptador traduz e aciona a biblioteca
    client_code(adaptador, dados_da_bolsa_xml)

# SAÍDA ESPERADA:
# Cliente: Trabalhando perfeitamente com o Adapter:
# Adapter: (TRADUZINDO) Convertendo XML para JSON nos bastidores...
# Adaptee: Gráficos gerados com os dados: {"acao": "AAPL", "valor": 150}