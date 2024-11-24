# This code doesnot involve classes of State and Puzzlegame, logic is same.
visited_states = set()


def get_user_input():
    print("Enter the initial state of the puzzle (3x3 grid):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError(
                "Invalid input. Please enter 3 integers separated by spaces for each row."
            )
        initial_state.append(row)
    return initial_state


def generate_successor_states(state):
    # Generate all possible successor states by moving one tile in each of the four directions
    # (up, down, left, right).
    successor_states = []
    empty_row, empty_col = find_empty_tile(state)

    # Moving tile up
    if empty_row > 0:
        new_state = [list(row) for row in state]
        new_state[empty_row][empty_col] = new_state[empty_row - 1][empty_col]
        new_state[empty_row - 1][empty_col] = 0
        successor_states.append(new_state)
    # Moving tile down
    if empty_row < 2:
        new_state = [list(row) for row in state]
        new_state[empty_row][empty_col] = new_state[empty_row + 1][empty_col]
        new_state[empty_row + 1][empty_col] = 0
        successor_states.append(new_state)
    # Moving tile left
    if empty_col > 0:
        new_state = [list(row) for row in state]
        new_state[empty_row][empty_col] = new_state[empty_row][empty_col - 1]
        new_state[empty_row][empty_col - 1] = 0
        successor_states.append(new_state)
    # Moving tile right
    if empty_col < 2:
        new_state = [list(row) for row in state]
        new_state[empty_row][empty_col] = new_state[empty_row][empty_col + 1]
        new_state[empty_row][empty_col + 1] = 0
        successor_states.append(new_state)
    return successor_states


def find_empty_tile(state):
    for row in range(len(state)):
        for col in range(len(state[0])):
            if state[row][col] == 0:
                return row, col


def print_puzzle(state):
    for row in state:
        for tile in row:
            print(tile, end=" ")
        print()


def depth_limited_search(state, depth_limit, max_depth, moves, visited_states):
    # 3. Perform a depth-limited search (DLS) with the current depth limit, starting from the
    # initial state of the puzzle.
    if tuple(map(tuple, state)) == goal_state:
        # 1. Check if the current state is the goal state.
        return True
    if depth_limit == 0:
        # Depth limit reached, return failure
        return False
    if depth_limit > max_depth:
        # Depth limit exceeds maximum depth, terminate search and return failure
        return False
    # Generate successor states by moving one tile in each direction
    successor_states = generate_successor_states(state)
    # For each successor state, check if it has already been visited. If yes, skip to the next
    # successor state. If not, mark the state as visited.
    for successor_state in successor_states:
        if tuple(map(tuple, successor_state)) not in visited_states:
            visited_states.add(
                tuple(map(tuple, successor_state))
            )  # Mark the state as visited

            moves.append(successor_state)  # Add the current move to the list of moves

            if depth_limited_search(
                successor_state, depth_limit - 1, max_depth, moves, visited_states
            ):
                return True
            moves.pop()  # Remove the current move if it doesn't lead to the goal
            visited_states.remove(
                tuple(map(tuple, successor_state))
            )  # Remove the state from visited states
    return False


def main():
    # 1. Define the initial state of the puzzle and the goal state.
    # initial_state = [[1, 2, 3], [7, 8, 0], [4, 5, 6]]
    initial_state = get_user_input()
    global goal_state
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    print("Initial State:")
    print_puzzle(initial_state)
    print()
    print("Goal State:")
    print_puzzle(goal_state)
    print("____________________________________________________")
    # 2. Set the initial depth limit to 0.
    depth_limit = 0
    max_depth = 50  # Set the maximum depth of the search space

    visited_states.clear()  # Clear visited states

    print("\nSolving with Depth-Limited Search...")

    moves = [initial_state]  # List to store the sequence of moves

    while True:
        if depth_limited_search(
            initial_state, depth_limit, max_depth, moves, visited_states
        ):
            print("Solution found within the depth limit.")
            print("\nSolution Path:")
            for move in moves:
                print_puzzle(move)
                print()
            print("Total number of moves:", len(moves) - 1)
            break
        else:
            visited_states.clear()  # Clear visited states for the next iteration
            depth_limit += 1
        if depth_limit > max_depth:
            print("Search terminated. Depth limit exceeds maximum depth.")
            break


if __name__ == "__main__":
    main()
