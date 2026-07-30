import pulp

def create_variables(C, T):
    x = {}
    for u in C:
        for t in range(1, T + 1):
            x[(u, t)] = pulp.LpVariable(f"x_{u}_{t}", cat="Binary")
            
    s = pulp.LpVariable("s", lowBound=0, cat="Integer")
    return x, s


def add_guarding_constraints(model, G, R, C, T, x):

    for t in range(1, T + 1):

        robber_vertex = R[t - 1]

        endangered_vertices = []

        for neighbor in G.neighbors(robber_vertex):

            if neighbor in C:

                endangered_vertices.append(neighbor)

        for u in endangered_vertices:

            model += x[(u, t)] == 1

def add_movement_constraints(model, G, C, T, x):
    for t in range(1, T + 1):
        next_time = 1 if t == T else t + 1 
        
        for u in C:

            reachable_vertices = [u]

            for neighbor in G.neighbors(u):

                if neighbor in C:

                    reachable_vertices.append(neighbor)

            model += x[(u, t)] <= pulp.lpSum(x[(v, next_time)] for v in reachable_vertices)


def add_capacity_constraints(model, C, T, x, s):
    for t in range(1, T + 1):
        model += pulp.lpSum(x[(u, t)] for u in C) == s


def extract_solution(model, C, T, x, s):
    if pulp.LpStatus[model.status] != 'Optimal':
        print(f"Warning: Solver did not find an optimal solution. Status: {pulp.LpStatus[model.status]}")
        return None, None

    guard_configuration = {}
    for t in range(1, T + 1):
        occupied_vertices = []
        for u in C:
            value = pulp.value(x[(u, t)])
            if value is not None and value > 0.5:
                occupied_vertices.append(u)

        guard_configuration[t] = occupied_vertices

    minimum_guards = int(round(pulp.value(s)))
    return minimum_guards, guard_configuration


def solve_guarding_problem(G, R, C):
    T = len(R)
    
    model = pulp.LpProblem("Cop_Robber_Guarding_Game", pulp.LpMinimize)
    x, s = create_variables(C, T)
    
    model += s
    
    add_guarding_constraints(model, G, R, C, T, x)
    add_movement_constraints(model, G, C, T, x)
    add_capacity_constraints(model, C, T, x, s)
    
    solver = pulp.PULP_CBC_CMD(msg=False) 
    model.solve(solver)
    
    minimum_guards, guard_configuration = extract_solution(model, C, T, x, s)
    return { "minimum_guards": minimum_guards, "guard_configuration": guard_configuration, "status": pulp.LpStatus[model.status]}