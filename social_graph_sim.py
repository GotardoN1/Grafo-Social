import networkx as nx
import matplotlib.pyplot as plt

# 1. Criar o Grafo (G = V, A)
G = nx.Graph()

# 2. Adicionar Vértices (Utilizadores)
utilizadores = ["João", "Paulo", "Maria", "Ana", "Carlos", "Desconhecido"]
G.add_nodes_from(utilizadores)

# 3. Adicionar Arestas (Amizades/Interações Recíprocas)
amizades = [("João", "Paulo"), ("João", "Maria"), ("Maria", "Ana"), ("Ana", "Paulo")]
G.add_edges_from(amizades)

# 4. Cálculo de Métricas (Grau do Vértice)
print(f"O grau do vértice (número de amigos) do João é: {G.degree('João')}")

# 5. Visualização do Grafo
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G) # Layout para posicionar os vértices

# Desenhar vértices e arestas
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_weight='bold', edge_color='gray')

plt.title("Simulação de Grafo Social (Modelo Facebook)")
plt.show()

# Verificar se existe "Passeio/Caminho" entre João e Ana
tem_caminho = nx.has_path(G, "João", "Ana")
print(f"Existe caminho entre João e Ana? {'Sim' if tem_caminho else 'Não'}")

# Verificar componente desconectado
tem_caminho_vulp = nx.has_path(G, "João", "Desconhecido")
print(f"Existe caminho entre João e o utilizador Desconhecido? {'Sim' if tem_caminho_vulp else 'Não'}")
