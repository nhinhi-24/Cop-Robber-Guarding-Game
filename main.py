from graph_generator import generate_graph
from visualization import draw_graph
from time_expanded import build_time_expanded_graph
from ilp_solver import solve_guarding_problem
from animation import animate_guarding_strategy
from time_expanded_illustration import draw_time_expanded_graph
from validator import validate_solution

def main():
    R = ["r0", "r1", "r2"]

    C = ["c0","c1","c2","c3","c4", "c5", "c6", "c7", "c8"]

    protected_edges = [("c0","c1"),("c0","c3"),
                       ("c1","c2"),("c2","c3"),
                       ("c3","c4"),("c4","c5"),
                       ("c5","c6"),("c6","c7"),
                       ("c6","c8"),("c7","c8")
    ]

    connection_edges = [("r0","c2"),("r0","c5"),
                        ("r1","c2"),("r1","c3"),
                        ("r1","c6"),("r2","c0"),
                        ("r2","c8")
    ]

    G = generate_graph(
        R,
        C,
        protected_edges,
        connection_edges
    )

    H = build_time_expanded_graph(G, R, C)

    result = solve_guarding_problem(G, R, C)

    validate_solution(G, R, C, result["guard_configuration"])

    print("Solver Status:")
    print(result["status"])

    print()

    print("Minimum Number of Guards:")
    print(result["minimum_guards"])


    draw_graph(G, R, C)
    draw_time_expanded_graph(G, C)
    animate_guarding_strategy(
        G,
        R,
        C,
        result["guard_configuration"]
    )



if __name__ == "__main__":
    main()