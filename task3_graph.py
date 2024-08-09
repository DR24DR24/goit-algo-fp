import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (станцій/зупинок)
stations = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J"
]
G.add_nodes_from(stations)

# Додавання рёбер (маршрутів) з атрибутами (відстань, час у дорозі)
routes = [
    ("A", "B", {"distance": 5, "time": 10}),
    ("A", "C", {"distance": 7, "time": 15}),
    ("B", "D", {"distance": 3, "time": 7}),
    ("B", "E", {"distance": 4, "time": 8}),
    ("C", "F", {"distance": 6, "time": 12}),
    ("D", "G", {"distance": 5, "time": 10}),
    ("E", "H", {"distance": 2, "time": 5}),
    ("F", "I", {"distance": 8, "time": 16}),
    ("G", "J", {"distance": 4, "time": 9}),
    ("H", "I", {"distance": 3, "time": 7}),
    ("I", "J", {"distance": 6, "time": 13}),
]

G.add_edges_from(routes)

if "__main__"==__name__:
    # Візуалізація графа
    pos = nx.spring_layout(G)  # Визначення позицій вершин
    #pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")

    # Додавання міток для атрибутів рёбер (відстань, час у дорозі)
    edge_labels = {(u, v): f"{d['distance']} km, {d['time']} min" for u, v, d in G.edges(data=True)}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Transport Network of a City")
    plt.show()

    num_of_nodes=G.number_of_nodes()
    num_of_edges=G.number_of_edges()
    is_connected=nx.is_connected(G)
    print(f"num_of_nodes: {num_of_nodes} num_of_edges: {num_of_edges} is_connected: {is_connected} ")
    degree_centrality=nx.degree_centrality(G)
    closeness_centrality=nx.closeness_centrality(G)
    betweenness_centrality=nx.betweenness_centrality(G)
    print(f"degree_centrality: {degree_centrality}")
    print(f"closeness_centrality: {closeness_centrality}")
    print(f"betweenness_centrality: {betweenness_centrality}")
    degree=dict(G.degree())
    print(f"degree : {degree}")