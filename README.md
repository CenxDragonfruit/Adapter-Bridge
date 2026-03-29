Padrões de Projeto Estruturais: Adapter e Bridge

Este repositório contém implementações práticas e documentação teórica sobre os Padrões de Projeto Adapter e Bridge. Este trabalho foi desenvolvido com fins acadêmicos para a disciplina de Padrões de Projeto.

Contexto Acadêmico

    Instituição: Instituto Federal de Rondônia (IFRO) - Campus Porto Velho Calama 

Disciplina: Padrões de Projeto 

Docente: Me. Leandro Ferrarezi Valiante 

Discentes: Bruno Henrique, Lucas Nogueira, Vytor Henrique 

1. Introdução aos Padrões de Projeto

O conceito de padrões de projeto nasceu com Christopher Alexander, que criou uma linguagem de padrões para resolver problemas repetitivos de planejamento urbano e construções físicas. A ideia foi trazida para a computação pela "Gang of Four" (Erich Gamma, John Vlissides, Ralph Johnson e Richard Helm), que catalogou 23 soluções para problemas comuns na programação orientada a objetos.

Os padrões de projeto são soluções típicas e reutilizáveis para problemas comuns no design de software. Eles se dividem em três categorias principais:

    Criacionais: Focados em mecanismos de criação de objetos.

Estruturais: Explicam como montar objetos e classes em estruturas maiores, mantendo-as flexíveis e eficientes (nesta categoria estão Adapter e Bridge).

Comportamentais: Voltados aos algoritmos e à atribuição de responsabilidades entre objetos.

2. O Padrão Bridge (Ponte)

O Bridge é um padrão estrutural que serve para dividir uma classe muito complexa em duas partes separadas: a abstração e a implementação.

O Problema

A principal motivação do Bridge é evitar a explosão combinatória de classes. Imagine classes de Formas (Círculo, Quadrado) e Cores (Vermelho, Azul). Usando herança simples, teríamos classes combinadas para cada variação. Adicionar uma nova forma ou cor faria o número de classes multiplicar absurdamente.

A Solução

O Bridge resolve isso extraindo uma das dimensões (como Cor) para uma hierarquia de classes separada e faz a Forma apontar para ela via composição.

Vantagens e Desvantagens

    Vantagens: Permite criar classes e aplicações independentes de plataforma. O código cliente trabalha com abstrações em alto nível, não ficando exposto a detalhes de plataforma.

Desvantagens: Pode tornar o código mais complicado ao aplicar o padrão em uma classe altamente coesa.

Quando não usar

    Projetos pequenos: A criação de toda a arquitetura de interfaces gera arquivos inúteis e complexidade desnecessária para projetos simples.

Requisitos incertos: O Bridge exige definir a separação correta das classes logo no início; se a arquitetura inicial estiver errada, a refatoração terá um alto custo.

3. O Padrão Adapter (Adaptador)

O Adapter é um padrão de projeto estrutural que permite que objetos com interfaces incompatíveis colaborem entre si, atuando como um "tradutor".

O Problema

A principal motivação é integrar classes existentes, sistemas legados ou bibliotecas de terceiros sem precisar alterar o código original delas. Imagine que o sistema baixa dados em formato XML, mas a equipe precisa usar uma biblioteca de análise de terceiros que só aceita dados em formato JSON.

A Solução

Cria-se um Adaptador que implementa a interface que o Cliente entende (XML). O Adaptador recebe a chamada, traduz os dados para a estrutura exigida (JSON) e repassa o pedido para acionar o Serviço (biblioteca de análises) corretamente.

Vantagens e Desvantagens

    Vantagens: Separa a conversão de interface ou de dados da lógica primária do negócio. Permite introduzir novos tipos de adaptadores sem quebrar o código cliente existente.

Desvantagens: A complexidade geral do código aumenta porque você precisa introduzir novas interfaces e classes.

Quando não usar

    Controle total do código: Não é recomendado quando a equipe tem acesso e controle total sobre o código de ambas as partes. Nesses casos, refatorar para padronizar as interfaces é a melhor solução.

4. Estrutura do Repositório e Execução

Os exemplos práticos foram desenvolvidos em Python.

A estrutura do projeto é a seguinte:

    Pasta Adapter: Implementação e exemplos do padrão Adapter.

    Pasta Bridge: Implementação e exemplos do padrão Bridge.

    Arquivo README.md: Documentação teórica e técnica.

Como testar localmente:

    Clone este repositório para o seu computador.

    Navegue pelo terminal até o diretório desejado (Adapter ou Bridge).

    Execute o arquivo principal utilizando o comando: python main.py.

5. Referências Bibliográficas

    GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. Padrões de projeto: soluções reutilizáveis de software orientado a objetos. Porto Alegre: Bookman, 2000.

SHVETS, Alexander. Padrões de projeto. Refactoring.Guru. Disponível em: https://refactoring.guru/pt-br/design-patterns.

COIMBRA, Gustavo. Design Patterns: o segredo para projetos de software duradouros e flexíveis. DIO, 2025.
