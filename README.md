

---

# 8-Puzzle Solver using Iterative Deepening Search (IDS)

## Overview
This Python implementation solves the classic 8-puzzle problem using the Iterative Deepening Search (IDS) algorithm. The 8-puzzle is a sliding puzzle where the player must move tiles to arrange them in a specific goal configuration. The algorithm combines the benefits of Depth-First Search (DFS) and Breadth-First Search (BFS), allowing for an optimal solution while avoiding the high memory costs of BFS.

## Problem Description
The 8-puzzle problem consists of a 3x3 grid with 8 numbered tiles (1-8) and one empty space (0). The goal is to arrange the tiles in the following order:

```
1 2 3
4 5 6
7 8 0
```

A tile can be moved into the empty space in four directions: up, down, left, or right. The goal is to reach the target configuration in the fewest moves.

### Example:
Start State:
```
1 5 3
2 7 4
6 0 8
```

Goal State:
```
1 2 3
4 5 6
7 8 0
```

## Iterative Deepening Search (IDS)
IDS is a hybrid of Depth-First Search (DFS) and Breadth-First Search (BFS). It performs multiple depth-limited searches with increasing depth limits until a solution is found.

### Algorithm Steps:
1. **Initialize the puzzle** with the start state and goal state.
2. **Iterative Deepening**:
   - Start from a depth limit of 0.
   - Perform Depth-Limited Search (DLS) at each depth level.
   - If the goal state is found within the current depth limit, return the solution.
   - If the goal state is not found, increase the depth limit and repeat.
3. **Terminate** if the maximum depth limit is exceeded or if the puzzle is unsolvable.

### Depth-Limited Search (DLS) Algorithm:
- Check if the current state matches the goal state.
- If the depth limit is reached, return failure.
- Generate all possible successor states by sliding tiles in the four possible directions.
- Perform recursive DLS on each unvisited successor state.

## Features:
- Solves the 8-puzzle problem using IDS.
- Handles both the start and goal state configurations.
- Ensures the puzzle is solvable before attempting the solution.
- Outputs the sequence of moves to reach the goal state.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```
   cd 8-puzzle-ids
   ```

## Usage

### Example:
```python
from puzzle_solver import solve_puzzle

# Define the start state and goal state
start_state = [
    [1, 5, 3],
    [2, 7, 4],
    [6, 0, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Solve the puzzle using IDS
solution = solve_puzzle(start_state, goal_state)

if solution:
    print("Solution found!")
    for step in solution:
        print(step)
else:
    print("No solution found. The puzzle may be unsolvable.")
```

### Parameters:
- `start_state`: The initial configuration of the puzzle (3x3 grid).
- `goal_state`: The target configuration of the puzzle (3x3 grid).

### Output:
- Prints the sequence of moves leading from the start state to the goal state.
- If the puzzle is unsolvable, the program will notify the user.

## Example Output:
```
Solution found!
Move 1: [1, 5, 3] [2, 7, 4] [6, 0, 8]
Move 2: [1, 5, 3] [2, 0, 4] [6, 7, 8]
Move 3: [1, 0, 3] [2, 5, 4] [6, 7, 8]
...
```

## Solvability Check
Before running the search, the program checks if the puzzle is solvable. An 8-puzzle is solvable if the number of inversions (pairs of tiles where a higher numbered tile precedes a lower numbered tile) is even.

## Limitations
- The algorithm may take a significant amount of time for more complex initial states with larger depth limits.
- The implementation assumes that the puzzle is solvable; unsolvable puzzles will return a failure message.

## License
This project is licensed under the MIT License.

---
