class AnalisadorXML:
    """O sistema original espera trabalhar com dados em XML."""

    def analisar(self, dados_xml: str) -> str:
        return f"Analisando dados nativos: {dados_xml}"


class BibliotecaDeAnalisesJSON:
    """A nova biblioteca (Adaptee) só aceita JSON."""

    def specific_request(self, dados_json: str) -> str:
        # Simula o erro caso receba um formato XML em vez de JSON
        if "<" in dados_json or ">" in dados_json:
            raise ValueError("Erro de Integração: Formato incompatível. Esperado JSON, mas recebeu XML.")
        return f"Gráficos avançados gerados a partir de: {dados_json}"


def cliente_tentando_direto() -> None:
    dados_da_bolsa_xml = "<acoes><acao>AAPL</acao><valor>150</valor></acoes>"

    nova_biblioteca = BibliotecaDeAnalisesJSON()

    print("Cliente: Tentando enviar XML direto para a nova biblioteca...")
    # Esta linha vai gerar o erro (Crash):
    nova_biblioteca.specific_request(dados_da_bolsa_xml)


if __name__ == "__main__":
    cliente_tentando_direto()

# SAÍDA ESPERADA:
# Cliente: Tentando enviar XML direto para a nova biblioteca...
# ValueError: Erro de Integração: Formato incompatível. Esperado JSON, mas recebeu XML.