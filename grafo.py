import networkx as nx
import matplotlib.pyplot as plt

# 1. Crie um grafo simples
grafo = nx.Graph()
grafo.add_edge("São Paulo", "Rio de Janeiro", distance=430)
grafo.add_edge("São Paulo", "Belo Horizonte", distance=586)
grafo.add_edge("Rio de Janeiro", "Belo Horizonte", distance=335)

# Posicione os nós para uma visualização clara
pos = nx.spring_layout(grafo)

# Extraia as distâncias como labels
labels = nx.get_edge_attributes(grafo, 'distance')

# Desenhe o grafo
plt.figure(figsize=(8, 6))
nx.draw(grafo, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels, font_color='red', font_size=10)

# Exiba o gráfico
plt.title("Grafo de Distâncias entre Cidades")
plt.show()
