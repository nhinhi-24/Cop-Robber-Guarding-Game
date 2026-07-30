def validate_solution(G, R, C, guard_configuration):

    T = len(R)

    for t in range(1, T + 1):

        robber = R[t - 1]

        endangered = [
            u for u in G.neighbors(robber)
            if u in C
        ]

        guards = guard_configuration[t]

        print(f"\nTime {t}")
        print(f"Robber: {robber}")
        print(f"Endangered: {endangered}")
        print(f"Guards: {guards}")

        if all(u in guards for u in endangered):
            print("✓ Guarding constraint satisfied")
        else:
            print("✗ Guarding constraint violated")