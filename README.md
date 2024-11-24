

---

# 8 Puzzle Solver using Iterative Deepening Search (IDS)

This Python project solves the classic 8-puzzle problem using **Depth-First Search** (DFS) with **Iterative Deepening Search** (IDS). The goal of the 8-puzzle is to arrange the numbered tiles (1 to 8) in a 3x3 grid, with the empty tile represented as `0`. The puzzle can be solved by sliding the tiles around, and this implementation finds the shortest solution path.

## Problem Description:

In the 8-puzzle, you are given an initial state and a goal state of the puzzle. The objective is to move the tiles in such a way that the initial configuration transforms into the goal configuration in the fewest possible moves.

### Example:
- **Initial State:**
  ```
  1 5 3
  2 7 4
  6 0 8
  ```

- **Goal State:**
  ```
  1 2 3
  4 5 6
  7 8 0
  ```

## Features:
- **Depth-First Search (DFS) with Iterative Deepening (IDS)**: The search algorithm increases the depth limit progressively to explore all possible states.
- **Solvability Check**: The program will automatically check if the puzzle is solvable and attempt to find a solution path if possible.
- **User Input**: Users can enter their own initial puzzle state, and the program will solve it for them.

## Installation:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Bushra-Butt-17/8-Puzzle-Solver-using-Iterative-Deepening-Search-IDS-.git
   ```
2. Navigate into the project directory:
   ```bash
   cd 8-Puzzle-Solver-using-Iterative-Deepening-Search-IDS-
   ```

3. Install any necessary Python dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

   **Note:** This project doesn't have any external dependencies other than Python itself, so no further setup is required.

## Usage:
1. Run the script:
   ```bash
   python puzzle_solver.py
   ```

2. The program will prompt you to enter the initial state of the puzzle in the following format (3 rows with 3 numbers each):
   ```
   1 5 3
   2 7 4
   6 0 8
   ```

3. After entering the initial state, the program will attempt to solve the puzzle and display the solution path (if a solution is found).

## Example Input:
```
Enter the initial state of the puzzle (3x3 grid):
1 5 3
2 7 4
6 0 8
```

## Example Output:
```
Solution found within the depth limit.

Solution Path:
1 5 3
2 7 4
6 0 8

1 5 3
2 0 4
6 7 8

1 0 3
2 5 4
6 7 8

...

Total number of moves: 10
```

## Project Structure:
- `puzzle_solver.py`: The main Python file that implements the 8-puzzle solver using IDS.
- `README.md`: This README file with all the project details.
- `requirements.txt`: (Optional) A list of Python dependencies.

## License:
This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
