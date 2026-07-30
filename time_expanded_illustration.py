import matplotlib.pyplot as plt
import networkx as nx


def draw_time_expanded_graph(G, C):

    H = nx.DiGraph()

    position = {}

    horizontal_gap = 5
    vertical_gap = 2


    for i, u in enumerate(C):

        y = -i * vertical_gap

        H.add_node((u, 1))
        H.add_node((u, 2))

        position[(u, 1)] = (0, y)
        position[(u, 2)] = (horizontal_gap, y)

    stay_edges = []

    for u in C:

        H.add_edge((u, 1), (u, 2))
        stay_edges.append(((u, 1), (u, 2)))

    move_edges = []

    for u in C:

        for v in G.neighbors(u):

            if v in C:

                H.add_edge((u, 1), (v, 2))
                move_edges.append(((u, 1), (v, 2)))


    plt.figure(figsize=(10, 9))

    nx.draw_networkx_nodes(
        H,
        position,
        node_color="lightblue",
        edgecolors="black",
        node_size=900
    )

    nx.draw_networkx_labels(
        H,
        position,
        labels={(u, t): u for (u, t) in H.nodes()},
        font_weight="bold"
    )

    nx.draw_networkx_edges(
        H,
        position,
        edgelist=stay_edges,
        width=2.5,
        arrows=True,
        arrowsize=18
    )

    nx.draw_networkx_edges(
        H,
        position,
        edgelist=move_edges,
        width=1.2,
        style="dashed",
        alpha=0.5,
        edge_color="black",
        arrows=True,
        arrowsize=15
    )

    plt.text(
        0,
        2,
        "Time t",
        fontsize=14,
        fontweight="bold",
        ha="center"
    )

    plt.text(
        horizontal_gap,
        2,
        "Time t+1",
        fontsize=14,
        fontweight="bold",
        ha="center"
    )

    plt.title(
        "Illustration of the Time-Expanded Graph Construction",
        fontsize=16,
        fontweight="bold"
    )

    plt.axis("off")

    plt.tight_layout()
