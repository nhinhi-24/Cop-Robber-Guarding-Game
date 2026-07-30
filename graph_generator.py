import networkx as nx

def generate_graph(R, C, protected_edges, connection_edges):

    if len(R) < 3:
        raise ValueError("The robber region must contain at least three vertices.")
   
    G = nx.Graph()

    G.add_nodes_from(R)
    G.add_nodes_from(C)

    number_of_robber_vertices = len(R)

    for i in range(number_of_robber_vertices):
        G.add_edge(R[i], R[(i + 1) % number_of_robber_vertices])

    G.add_edges_from(protected_edges)

    G.add_edges_from(connection_edges)

    return G
