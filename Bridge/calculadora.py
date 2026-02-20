import time


def calcular_complexidade():
    print("=" * 55)
    print("🍔  BEM-VINDO À CALCULADORA DO PADRÃO BRIDGE!  🍔")
    print("=" * 55)
    print("Vamos descobrir como o Bridge salva o seu projeto de ")
    print("virar uma bagunça de classes infinitas.\n")
    time.sleep(1)

    dimensoes = {}
    contador = 1

    while True:
        print(f"\n--- 📦 Característica {contador} ---")
        nome = input(
            "Qual o NOME dessa característica? (Ex: 'Entrega', 'Pagamento' ou digite 'fim' para encerrar): ").strip()

        # Condição de parada mais intuitiva
        if nome.lower() in ['fim', 'sair', '0', '']:
            if len(dimensoes) < 2:
                print("⚠️ Poxa, precisamos de pelo menos 2 características para a mágica acontecer! Tente novamente.")
                continue
            break

        # Loop para garantir que o usuário digite um número válido
        while True:
            try:
                qtd = int(input(f"Quantas opções existem para '{nome}'? (Ex: 3): "))
                if qtd <= 0:
                    print("⚠️ Digite um número maior que zero.")
                    continue
                break  # Sai do loop se o número for válido
            except ValueError:
                print("⚠️ Ops! Digite apenas números inteiros (ex: 2, 3, 4).")

        # Salva o nome e a quantidade no nosso dicionário
        dimensoes[nome] = qtd
        contador += 1
        print(f"✅ Legal! A característica '{nome}' com {qtd} opções foi adicionada.")
        time.sleep(0.5)

    print("\n⏳ Calculando o impacto no seu código...\n")
    time.sleep(1.5)

    # Sem Bridge: Multiplicação
    sem_bridge = 1
    for qtd in dimensoes.values():
        sem_bridge *= qtd

    # Com Bridge: Adição
    com_bridge = sum(dimensoes.values())

    # Prepara os textos para a exibição final
    nomes_dimensoes = list(dimensoes.keys())
    valores = list(dimensoes.values())

    print("=" * 55)
    print("📊 RESULTADO DA COMPLEXIDADE")
    print("=" * 55)

    print("\n❌ SEM o Padrão Bridge (Criando classes para cada combinação):")
    print(f"   Fórmula: {' * '.join(map(str, valores))} ({' x '.join(nomes_dimensoes)})")
    print(f"   Total  : 🤯 {sem_bridge} classes concretas")

    print(f"\n✅ COM o Padrão Bridge (Separando as responsabilidades):")
    print(f"   Fórmula: {' + '.join(map(str, valores))} ({' + '.join(nomes_dimensoes)})")
    print(f"   Total  : 😌 {com_bridge} classes concretas")
    print("=" * 55)

    economia = sem_bridge - com_bridge
    print(f"\n💡 CONCLUSÃO:")
    print(f"Usando o Bridge, você deixaria de escrever e manter {economia} classes desnecessárias!")
    print("Isso significa menos bugs, código mais limpo e paz de espírito. 🚀\n")


if __name__ == "__main__":
    calcular_complexidade()