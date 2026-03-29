# Padrões de Projeto Estruturais: Adapter e Bridge

Este repositório contém implementações práticas e documentação teórica sobre os Padrões de Projeto **Adapter** e **Bridge**. Este trabalho foi desenvolvido com fins acadêmicos.

## 🎓 Contexto Acadêmico

| Informação | Detalhe |
| :--- | :--- |
| **Instituição** | Instituto Federal de Rondônia (IFRO) - Campus Porto Velho Calama |
| **Disciplina** | Padrões de Projeto |
| **Docente** | Me. Leandro Ferrarezi Valiante |
| **Discentes** | Bruno Henrique, Lucas Nogueira, Vytor Henrique |

---

## 📖 1. Introdução aos Padrões de Projeto

O conceito de padrões de projeto nasceu com Christopher Alexander, que criou uma "linguagem de padrões" para resolver problemas repetitivos de planejamento urbano e construções físicas. A ideia foi trazida para a computação por quatro autores (Erich Gamma, John Vlissides, Ralph Johnson e Richard Helm). Em 1994, eles lançaram o livro *"Padrões de Projeto - Soluções Reutilizáveis de Software Orientado a Objetos"*, apresentando 23 soluções padronizadas para resolver problemas comuns na programação orientada a objetos.

Os padrões de projeto dividem-se em três categorias principais:

*   **Criacionais:** Fornecem vários mecanismos de criação de objetos, que aumentam a flexibilidade.
*   **Estruturais:** Explicam como montar objetos e classes em estruturas maiores, mantendo essas estruturas flexíveis e eficientes. (Nesta categoria estão *Adapter* e *Bridge*).
*   **Comportamentais:** Voltados aos algoritmos e à atribuição de responsabilidades entre objetos.

---

## 🌉 2. O Padrão Bridge (Ponte)

O **Bridge** é um padrão estrutural que serve para dividir uma classe muito complexa em duas partes separadas: a abstração e a implementação.

### O Problema
A principal motivação do Bridge é evitar a explosão combinatória de classes. Imagine classes de Formas (Círculo, Quadrado) e Cores (Vermelho, Azul). Usando herança, teríamos classes específicas para cada combinação (como Círculo Vermelho ou Quadrado Azul), e adicionar uma nova forma ou cor faria o número de classes multiplicar absurdamente.

### A Solução
O Bridge extrai uma das dimensões (como Cor) para uma hierarquia de classes separada e faz a Forma apontar para ela.

### Vantagens e Desvantagens

| Vantagens | Desvantagens |
| :--- | :--- |
| O código cliente trabalha com abstrações em alto nível, não ficando exposto a detalhes de plataforma. | Pode tornar o código mais complicado ao aplicar o padrão em uma classe que já é altamente coesa. |
| Permite criar aplicações independentes de plataforma. | |

### Quando NÃO usar
*   **Projetos pequenos:** Não é recomendado para sistemas simples e estáticos. A criação de toda a arquitetura de interfaces e pontes gera arquivos inúteis e complexidade desnecessária para o projeto.
*   **Foco em leitura rápida:** Deve ser evitado quando a equipe precisa entender o código de imediato. O padrão fragmenta a lógica, obrigando os desenvolvedores a buscarem o código real em vários arquivos diferentes.
*   **Requisitos incertos:** Não é indicado para projetos que mudam constantemente. O Bridge exige definir a separação correta das classes logo no início; se as regras mudarem e a arquitetura inicial estiver errada, a refatoração terá um alto custo.

---

## 🔌 3. O Padrão Adapter (Adaptador)

O **Adapter** é um padrão estrutural que permite objetos com interfaces incompatíveis colaborarem entre si, atuando como um "tradutor".

### O Problema
A principal motivação é integrar classes existentes, sistemas legados ou bibliotecas de terceiros sem precisar alterar o código original delas. Imagine que a sua aplicação baixa dados no formato XML, mas a equipe precisa integrar uma biblioteca de análise de terceiros que só aceita dados no formato JSON.

### A Solução
Cria-se um Adaptador que implementa a interface que a Aplicação entende (XML). Esse Adaptador recebe a chamada contendo o XML, traduz os dados para uma estrutura JSON e repassa o pedido para acionar a biblioteca de análises corretamente.

### Vantagens e Desvantagens

| Vantagens | Desvantagens |
| :--- | :--- |
| Você pode separar a conversão de interface da lógica primária do negócio. | A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes. |
| É possível introduzir novos adaptadores sem quebrar o código cliente existente. | |

### Problemas Comuns
*   **Uso Excessivo:** Ocorre quando o desenvolvedor cria adaptadores para conectar sistemas internos que ele mesmo controla, em vez de simplesmente refatorar o código para que tenham a mesma interface.
*   **Adaptadores de Duas Vias:** Quando dois sistemas precisam falar um com o outro usando interfaces diferentes, criar um adaptador que funcione em ambas as direções pode gerar um código extremamente complexo e difícil de manter.

### Quando NÃO usar
*   **Controle total do código:** Não é recomendado quando a equipe tem acesso e controle total sobre o código de ambas as partes; nesses casos, a refatoração das classes para padronizar as interfaces é a melhor solução.

---

## 🚀 4. Executando o Projeto

Os exemplos práticos deste repositório foram desenvolvidos em **Python**.

*   📁 **Pasta Adapter:** Contém a implementação e exemplos do padrão Adapter.
*   📁 **Pasta Bridge:** Contém a implementação e exemplos do padrão Bridge.

### Para rodar localmente:

1.  Clone o repositório em sua máquina.
2.  Navegue até o diretório desejado (`Adapter` ou `Bridge`).
3.  Execute o arquivo de inicialização via terminal ou IDE.

---

## 📚 5. Referências Bibliográficas

1.  GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Padrões de projeto: soluções reutilizáveis de software orientado a objetos**. Porto Alegre: Bookman, 2000.
2.  SHVETS, Alexander. **Padrões de projeto**. Refactoring. Guru, [s.d.]. Disponível em: [https://refactoring.guru/pt-br/design-patterns](https://refactoring.guru/pt-br/design-patterns).
3.  COIMBRA, Gustavo. **Design Patterns: o segredo para projetos de software duradouros e flexíveis**. DIO, 17 mar. 2025.
