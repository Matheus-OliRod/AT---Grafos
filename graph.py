### Arquivo exlcuisvo para a criação e manipulação de grafos ###

import networkx as nx
import matplotlib.pyplot as plt

# Criando as arestas

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
arestas = [
    ('A', 'B', 2.0),
    ('A', 'C', 12.0),
    ('A', 'F', 4.0),
    ('A', 'G', 3.5),
    ('A', 'H', 2.0),
    ('B', 'C', 1.0),
    ('B', 'D', 2.5),
    ('C', 'E', 1.0),
    ('D', 'E', 1.0),
    ('D', 'I', 4.0),
    ('E', 'F', 1.0),
    ('F', 'G', 1.0),
    ('G', 'H', 1.0),
    ('I', 'E', 3.0),
    ('I', 'F', 5.0),
    ('I', 'G', 6.0),
    ('I', 'H', 7.5)
]

G = nx.Graph()
# Adicionando vertices e arestas

G.add_weighted_edges_from(arestas)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True, node_color = 'lightblue', edge_color = 'black', node_size = 300, font_size = 16)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Simple graph visualization")
plt.show()