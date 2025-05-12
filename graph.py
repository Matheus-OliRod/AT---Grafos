
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque  # Usado no BFS
from itertools import permutations

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

# Criando o grafo original
G = nx.Graph()
G.add_weighted_edges_from(arestas)

# Desenhando e salvando o grafo original
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=300, font_size=16)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Simple graph visualization")
plt.savefig("grafo.png")
plt.clf()
# -------------------------------
# TSP: menor caminho passando por todos, partindo de 'I'
# -------------------------------

def tsp_brute_force(G, start):
    nodes = list(G.nodes())
    nodes.remove(start)
    min_cost = float('inf')
    best_path = None

    for perm in permutations(nodes):
        path = [start] + list(perm)
        cost = 0
        valid = True
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            if G.has_edge(u, v):
                cost += G[u][v]['weight']
            else:
                valid = False
                break
        if valid and cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Executa a busca TSP
tsp_path, tsp_cost = tsp_brute_force(G, 'I')

if tsp_path:
    print("TSP encontrado (menor caminho):")
    print(" -> ".join(tsp_path))
    print(f"Custo total: {tsp_cost:.2f}")

    # Criando grafo do TSP
    tsp_graph = nx.Graph()
    for i in range(len(tsp_path) - 1):
        u, v = tsp_path[i], tsp_path[i + 1]
        tsp_graph.add_edge(u, v, weight=G[u][v]['weight'])

    # Visualização
    pos = nx.spring_layout(tsp_graph, seed=42)
    nx.draw(tsp_graph, pos, with_labels=True, node_color='lightgreen', edge_color='blue', node_size=300, font_size=16)
    edge_labels = nx.get_edge_attributes(tsp_graph, 'weight')
    nx.draw_networkx_edge_labels(tsp_graph, pos, edge_labels=edge_labels)
    plt.title(f"TSP Caminho Mínimo (de 'I') - Custo: {tsp_cost:.2f}")
    plt.savefig("tsp_path.png")
    plt.clf()

else:
    print("Não foi possível encontrar um caminho TSP.")
