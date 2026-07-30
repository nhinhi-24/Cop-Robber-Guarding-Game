import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation


def animate_guarding_strategy(G, R, C, guard_configuration):

    node_position = {}

    robber_graph = nx.cycle_graph(len(R))
    robber_position = nx.circular_layout(robber_graph)

    for i in range(len(R)):
        x, y = robber_position[i]
        node_position[R[i]] = (4 * x, 4 * y + 4)

    protected_graph = G.subgraph(C)

    protected_position = nx.spring_layout(
        protected_graph,
        seed=42
    )

    for vertex in C:
        x, y = protected_position[vertex]
        node_position[vertex] = (4 * x, 4 * y - 4)

    fig, ax = plt.subplots(figsize=(8, 8))

    def update(frame):

        ax.clear()

        robber_vertex = R[frame]
        
        threatened = []
        
        for neighbor in G.neighbors(robber_vertex):
            if neighbor in C:
                threatened.append(neighbor)

        guards = guard_configuration.get(frame + 1, [])

        node_colors = []

        for node in G.nodes():

            if node == robber_vertex:
                node_colors.append("red")

            elif node in guards and node in threatened:
                node_colors.append("gold")

            elif node in guards:
                node_colors.append("limegreen")
                
            elif node in threatened:
                node_colors.append("orange")
                
            elif node in R:
                node_colors.append("skyblue")

            else:
                node_colors.append("white")

        edge_colors = []
        for edge in G.edges():
            if robber_vertex in edge:
                edge_colors.append("red")
            else:
                edge_colors.append("gray")

        nx.draw_networkx(
            G,
            pos=node_position,
            node_color=node_colors,
            edgecolors="black",
            node_size=700,
            with_labels=True,
            ax=ax
        )

        ax.set_title(
            f"Time step = {frame+1}\n"
            f"Robber = {robber_vertex},"
            f"Threatened: {', '.join(threatened)}"
        )

    ani = FuncAnimation(
        fig,
        update,
        frames=len(R),
        interval=1000,
        repeat=True,
        cache_frame_data=False
    )

    plt.tight_layout()

    plt.show(block=True)

    return ani
