from collections import deque

def read_input(file_path):
    """Reads the corrupted cell coordinates from the input file."""
    with open(file_path, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_memory_space(grid, x, y):
    """Marks a single cell as corrupted."""
    grid[y][x] = 1

def is_path_available(grid, start, end):
    """Checks if a path exists using BFS."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == 0:
                queue.append((nx, ny))
                visited.add((nx, ny))

    return False

def find_blocking_byte(corrupted_cells, grid_size):
    """Finds the first byte that blocks the path."""
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    for x, y in corrupted_cells:
        simulate_memory_space(grid, x, y)
        if not is_path_available(grid, start, end):
            return x, y

    return None

def main():
    input_file = 'input.txt'
    corrupted_cells = read_input(input_file)
    grid_size = 71  # Grid size for the actual input

    # Find the blocking byte
    blocking_byte = find_blocking_byte(corrupted_cells, grid_size)

    if blocking_byte:
        print(f"{blocking_byte[0]},{blocking_byte[1]}")
    else:
        print("No blocking byte found.")

if __name__ == "__main__":
    main()
