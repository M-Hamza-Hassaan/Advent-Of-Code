def simulate_guard_path(map_lines):
    # Parse the map and locate the guard's starting position and direction
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}

    grid = [list(line.strip()) for line in map_lines]
    rows, cols = len(grid), len(grid[0])

    # Find the guard's starting position and direction
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = "."  # Replace the guard's marker with empty space
                break
        if guard_pos:
            break

    visited = set()
    visited.add(guard_pos)

    # Simulate the guard's movement
    while True:
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_pos = (r + dr, c + dc)

        # Check if the guard is leaving the map bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check if the next position is blocked
        if grid[next_pos[0]][next_pos[1]] == "#":
            guard_dir = turn_right[guard_dir]  # Turn right
        else:
            guard_pos = next_pos  # Move forward
            visited.add(guard_pos)

    return len(visited)

# Read the map from an input file
input_file = "input.txt"

with open(input_file, "r") as file:
    map_lines = file.readlines()

# Calculate the number of distinct positions visited
distinct_positions = simulate_guard_path(map_lines)
print("Distinct positions visited:", distinct_positions)
