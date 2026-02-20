# Padrões de Projeto GoF: Adapter e Bridge em Python

## 📚 Visão Geral do Projeto

Este repositório é dedicado ao estudo e demonstração de dois padrões de projeto fundamentais da **Gang of Four (GoF)**: **Adapter** e **Bridge**. O objetivo principal é ilustrar, através de exemplos práticos em Python, como esses padrões são aplicados para resolver desafios comuns no design de software, promovendo a flexibilidade, a manutenibilidade e a extensibilidade de sistemas orientados a objetos. O projeto serve como um recurso educacional para aprofundar a compreensão sobre a importância e a aplicação estratégica de padrões de projeto em contextos acadêmicos e profissionais.

## 💡 O que são Padrões de Projeto GoF?

Os **Padrões de Projeto GoF** (Gang of Four) são soluções reutilizáveis para problemas comuns que surgem no design de software orientado a objetos. Publicados no livro "Design Patterns: Elements of Reusable Object-Oriented Software" por Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides (a "Gang of Four"), esses padrões oferecem um vocabulário comum e uma abordagem estruturada para projetar sistemas robustos e flexíveis. Eles são categorizados em três tipos:

*   **Criacionais**: Lidam com a criação de objetos de forma flexível e controlada.
*   **Estruturais**: Preocupam-se com a composição de classes e objetos para formar estruturas maiores.
*   **Comportamentais**: Focam na comunicação e atribuição de responsabilidades entre objetos.

Este repositório explora dois padrões estruturais: Adapter e Bridge.

## 📁 Estrutura do Repositório

O projeto está organizado para facilitar a compreensão e a execução dos exemplos:

```
Adapter-Bridge/
├── .venv/
├── Adapter/
│   ├── fone.py         # Exemplo sem o padrão Adapter
│   └── solucaoA.py     # Exemplo com o padrão Adapter
├── Bridge/
│   ├── delivery.py     # Exemplo sem o padrão Bridge
│   └── solucaoB.py     # Exemplo com o padrão Bridge
└── README.md
```

## 📐 Padrão de Projeto: Adapter (Adaptador)

### 💡 Propósito

O padrão **Adapter** (também conhecido como Wrapper) é um padrão de projeto estrutural que permite que objetos com interfaces incompatíveis colaborem. Ele atua como um intermediário, convertendo a interface de uma classe existente (o `Adaptee`) para uma interface que o cliente espera (o `Target`). Isso é particularmente útil para integrar sistemas legados ou bibliotecas de terceiros sem modificar seu código-fonte original, promovendo a reutilização de código e a flexibilidade.

### 🎯 Objetivo do Código (`Adapter/fone.py` e `Adapter/solucaoA.py`)

Os arquivos `fone.py` e `solucaoA.py` demonstram o padrão Adapter no contexto de conexão de fones de ouvido a celulares. O `fone.py` ilustra um cenário onde celulares (antigos com entrada P2 e modernos com USB-C) e fones de ouvido (P2 e USB-C) são diretamente incompatíveis, exigindo uma classe específica para cada combinação. Isso resulta em um sistema rígido e difícil de estender. Já o `solucaoA.py` apresenta a implementação do padrão Adapter, introduzindo um `AdaptadorUniversal` que permite a conexão de qualquer tipo de fone a qualquer tipo de celular, independentemente de suas interfaces originais. O objetivo é mostrar como o Adapter resolve a incompatibilidade de interfaces, permitindo que componentes distintos trabalhem juntos harmoniosamente.

### 🏗️ Estrutura Conceitual do Adapter

O Padrão Adapter é composto por:

*   **Target (Alvo)**: Define a interface que o cliente espera.
*   **Adaptee (Adaptado)**: A classe existente com a funcionalidade desejada, mas com uma interface incompatível.
*   **Adapter (Adaptador)**: A classe que implementa a interface `Target` e encapsula um objeto `Adaptee`, traduzindo as chamadas de uma interface para outra.
*   **Client (Cliente)**: A classe que interage com o `Target`.

### 👍 Vantagens do Adapter

*   **Reutilização de Código**: Permite o uso de classes existentes com interfaces diferentes.
*   **Flexibilidade**: Facilita a integração de componentes incompatíveis.
*   **Separação de Preocupações**: Isola a lógica de adaptação em uma classe dedicada.
*   **Manutenibilidade**: Reduz a necessidade de refatorar classes existentes.

### 👎 Desvantagens do Adapter

*   **Complexidade Adicional**: Pode introduzir uma camada extra de complexidade.
*   **Overhead de Desempenho**: Pequeno impacto no desempenho devido às chamadas adicionais.
*   **Acoplamento**: O Adapter se acopla ao Adaptee.

## 🌉 Padrão de Projeto: Bridge (Ponte)

### 💡 Propósito

O padrão **Bridge** é um padrão de projeto estrutural que visa desacoplar uma abstração de sua implementação, permitindo que ambas variem independentemente. Ele é ideal para cenários onde um sistema possui múltiplas dimensões de variação, e a combinação direta dessas variações levaria a uma "explosão de classes". O Bridge promove um design mais flexível e extensível, onde as mudanças em uma dimensão não afetam a outra.

### 🎯 Objetivo do Código (`Bridge/delivery.py` e `Bridge/solucaoB.py`)

Os arquivos `delivery.py` e `solucaoB.py` demonstram o padrão Bridge no contexto de um sistema de pedidos de comida. O `delivery.py` ilustra o problema da "explosão de classes", onde cada combinação de tipo de entrega (Delivery, Retirada, Comer no Local) e forma de pagamento (PIX, Cartão) exige uma classe separada (ex: `DeliveryComPix`, `RetiradaComCartao`). Isso torna o sistema rígido e difícil de escalar. Em contraste, o `solucaoB.py` aplica o padrão Bridge, separando a hierarquia de abstração (tipos de pedido) da hierarquia de implementação (formas de pagamento). Isso permite que novas formas de pagamento ou novos tipos de entrega sejam adicionados de forma independente, sem a necessidade de modificar as classes existentes na outra hierarquia. O objetivo é evidenciar como o Bridge evita a proliferação de classes e promove um design mais modular e adaptável.

### 🏗️ Estrutura Conceitual do Bridge

O Padrão Bridge é composto por:

*   **Abstraction (Abstração)**: Define a interface de alto nível e mantém uma referência a um objeto `Implementor`.
*   **Refined Abstraction (Abstração Refinada)**: Extensões da Abstração que fornecem variações da lógica de controle.
*   **Implementor (Implementador)**: Define a interface para as classes de implementação.
*   **Concrete Implementor (Implementador Concreto)**: Implementa a interface `Implementor`.

### 👍 Vantagens do Bridge

*   **Desacoplamento**: Separação clara entre abstração e implementação.
*   **Extensibilidade**: Permite a adição independente de novas abstrações ou implementações.
*   **Flexibilidade**: Possibilita a configuração dinâmica da implementação em tempo de execução.
*   **Reutilização de Código**: Implementações podem ser reutilizadas por diferentes abstrações.

### 👎 Desvantagens do Bridge

*   **Complexidade Inicial**: Pode aumentar a complexidade inicial do design.
*   **Aumento do Número de Classes**: Embora evite a explosão combinatória, ainda resulta em mais classes no total.

## 🚀 Como Explorar os Exemplos

Para interagir com os exemplos, navegue até as respectivas pastas (`Adapter` e `Bridge`) e execute os arquivos Python. Cada arquivo é projetado para ser autoexplicativo e interativo, permitindo que você observe o comportamento dos sistemas com e sem a aplicação dos padrões de projeto.

## 📝 Conclusão

Os padrões de projeto Adapter e Bridge são ferramentas indispensáveis para o desenvolvimento de software robusto e flexível. O Adapter facilita a interoperabilidade entre componentes com interfaces distintas, enquanto o Bridge oferece uma solução elegante para gerenciar a complexidade de sistemas com múltiplas dimensões de variação. A aplicação desses padrões é um pilar fundamental para a construção de arquiteturas de software que aderem aos princípios de design orientado a objetos, como o Open/Closed Principle e o Single Responsibility Principle, resultando em sistemas mais manuteníveis, escaláveis e adaptáveis a futuras mudanças.

## 🧑‍💻 Autor

**Bruno Henrique, Vytor Henrique, Lucas Nogueira**
**ADS 3º Período 2026**
**IFRO Campus Porto Velho Calama**
