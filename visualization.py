import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, R, C):

    node_position = {}
    robber_graph = nx.cycle_graph(len(R))
    robber_position = nx.circular_layout(robber_graph)
    for i in range(len(R)):
        x, y = robber_position[i]
        node_position[R[i]] = (x * 4, y * 4 + 4)
        
    protected_graph = G.subgraph(C)
    protected_position = nx.spring_layout(protected_graph, seed=42)
    
    for vertex in C:
        x, y = protected_position[vertex]
        node_position[vertex] = (x * 4, y * 4 - 4)

    robber_edges = []

    protected_edges = []

    connection_edges = []

    for u, v in G.edges():

        if u in R and v in R:

            robber_edges.append((u, v))

        elif u in C and v in C:

            protected_edges.append((u, v))

        else:

            connection_edges.append((u, v))

    plt.figure(figsize=(10, 8))

    nx.draw_networkx_nodes(
        G,
        node_position,
        nodelist=R,
        node_color="skyblue",
        edgecolors="black",
        node_size=700
    )

    nx.draw_networkx_nodes(
        G,
        node_position,
        nodelist=C,
        node_color="lightgreen",
        edgecolors="black",
        node_size=700
    )

    nx.draw_networkx_labels(G, node_position)

    nx.draw_networkx_edges(
        G,
        node_position,
        edgelist=robber_edges,
        edge_color="blue",
        width=2
    )

    nx.draw_networkx_edges(
        G,
        node_position,
        edgelist=protected_edges,
        edge_color="green",
        width=2
    )

    nx.draw_networkx_edges(
        G,
        node_position,
        edgelist=connection_edges,
        edge_color="gray",
        style="dashed",
        width=1.5
    )

    plt.title("Cop-Robber Guarding Game")

    plt.axis("off")

    plt.show()