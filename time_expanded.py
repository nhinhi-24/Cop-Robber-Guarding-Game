import networkx as nx


def build_time_expanded_graph(G, R, C):

    T = len(R)

    H = nx.DiGraph()

    for t in range(1, T + 1):

        for u in C:

            H.add_node((u, t))

    for t in range(1, T + 1):

        if t == T:
            next_time = 1
        else:
            next_time = t + 1

        for u in C:

            H.add_edge((u, t), (u, next_time))

            for neighbor in G.neighbors(u):

                if neighbor in C:

                    H.add_edge((u, t), (neighbor, next_time))

    return H