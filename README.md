Facebook Graph: Teoria, Infraestrutura e Implementação 🌐
Este repositório contém um estudo aprofundado sobre como a Teoria dos Grafos é a espinha dorsal do Facebook (Meta), cobrindo desde a modelação matemática até as tecnologias de backend como TAO e GraphQL.

📌 Visão Geral
O projeto analisa o "Grafo Social" — um termo popularizado por Mark Zuckerberg em 2007 — que representa a rede global de pessoas e as suas infinitas conexões e interações.

🏗️ Arquitetura e Tecnologias (Meta Stack)
Com base na análise técnica, destacam-se três pilares que sustentam o grafo do Facebook:TAO (The Associations and Objects):
* O serviço de cache distribuído que o Facebook utiliza para gerenciar o grafo social.
* Otimiza a leitura e escrita de biliões de objetos (nós) e associações (arestas) em tempo real.
GraphQL:
Linguagem de consulta de dados criada para lidar com a natureza hierárquica e interconectada dos grafos, permitindo que o cliente peça apenas os dados necessários de cada nó.
Graph API:
* A interface principal que permite que aplicações externas interajam com os dados da rede (utilizadores, fotos, posts) através de uma estrutura de grafos.

🎓 Modelação Teórica
Matematicamente, a rede é tratada como um grafo $G = (V, A):
* Vértices (V): Representam entidades (Utilizadores, Páginas, Grupos).
* Arestas (A): Representam relações (Amizade, Check-in, Curtida). No Facebook, a amizade é uma aresta não-direcionada (recíproca), enquanto um "Seguir" pode ser uma aresta direcionada (dígrafo).

Métricas Analisadas:
* Grau do Vértice: Popularidade/Conectividade de um utilizador.
* Componentes Conectados: Identificação de sub-redes e grupos de interesse.
* Caminhos Mínimos: A lógica por trás do "Sugestões de Amizade" e do conceito de "seis graus de separação".

🔍 Graph Search & Busca Semântica
O projeto detalha o funcionamento do motor de busca semântica, que percorre o grafo para entregar resultados contextuais.
* Exemplo: Ao pesquisar "Amigos que gostam de Sushi em NY", o algoritmo não busca apenas palavras-chave, ele faz um percurso de vértices (Amigo -> Gosto -> Sushi -> Localização) para encontrar a interseção exata dos dados.
