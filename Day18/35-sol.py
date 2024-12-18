from collections import deque

def read_input(file_path):
    """Reads the corrupted cell coordinates from the input file."""
    with open(file_path, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_memory_space(corrupted_cells, grid_size):
    """Creates the grid and marks corrupted cells."""
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in corrupted_cells[:1024]:  # Simulate the first 1024 bytes
        grid[y][x] = 1  # Mark the cell as corrupted
    return grid

def find_shortest_path(grid, start, end):
    """Finds the shortest path using BFS."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == 0:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return -1  # Return -1 if no path exists

def main():
    input_file = 'input.txt'
    corrupted_cells = read_input(input_file)
    grid_size = 71  # Grid size for the actual input

    # Simulate the memory space
    grid = simulate_memory_space(corrupted_cells, grid_size)

    # Find the shortest path
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    shortest_path_steps = find_shortest_path(grid, start, end)

    print("Minimum number of steps to reach the exit:", shortest_path_steps)

if __name__ == "__main__":
    main()
