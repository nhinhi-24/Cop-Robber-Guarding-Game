# Optimizing the Number of Guards in a Cop-Robber Guarding Game with a Cycle Robber Region

## Introduction

This repository contains the Python implementation accompanying the research project **"Optimizing the Number of Guards in a Cop-Robber Guarding Game with a Cycle Robber Region."**

The project formulates the guarding problem as a **Time-Extended Integer Linear Programming (ILP)** model to determine the minimum number of guards required to continuously protect a graph while an omniscient robber moves on a cycle robber region.

The implementation includes graph construction, time-expanded graph generation, ILP optimization using the CBC solver, and visualization of the optimal guarding strategy.

---

## Repository Structure

```

├── animation.py                 # Guard movement animation
├── graph_generator.py           # Graph construction
├── ilp_solver.py                # Time-Extended ILP model and optimization
├── main.py                      # Main program
├── time_expanded_illustration.py# Time-expanded graph illustration
├── time_expanded.py             # Time-expanded graph generation
├── validator.py                 # Solution validation
└── visualization.py             # Static graph visualization
```

---

## Requirements

- Python 3.x
- NetworkX
- Matplotlib
- PuLP

Install the required packages:

```bash
pip install networkx matplotlib pulp
```

---

## Running the Project

Run the main program:

```bash
python main.py
```

The program will:

1. Construct the graph instance.
2. Generate the time-expanded graph.
3. Formulate the Time-Extended ILP model.
4. Solve the optimization problem using the CBC solver.
5. Output the optimal guard configuration.
6. Visualize the guarding strategy.

---

## Author

**Nguyen Duong Quynh Nhi**

University of Science and Technology of Hanoi (USTH)

2026
