from collections import deque

def read_map(filename):
    """Read the topographic map from a file."""
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def is_valid_move(map_data, x, y, current_height):
    """Check if the move is valid: within bounds, passable, and increasing by exactly 1."""
    return (
        0 <= x < len(map_data) and
        0 <= y < len(map_data[0]) and
        map_data[x][y] == current_height + 1
    )

def bfs_score(map_data, start_x, start_y):
    """Perform BFS to calculate the score of a trailhead."""
    queue = deque([(start_x, start_y, 0)])  # (x, y, current_height)
    visited = set()
    visited.add((start_x, start_y))
    score = 0

    while queue:
        x, y, height = queue.popleft()

        if height == 9:
            score += 1
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid_move(map_data, nx, ny, height):
                visited.add((nx, ny))
                queue.append((nx, ny, height + 1))

    return score

def calculate_total_score(map_data):
    """Calculate the total score for all trailheads in the map."""
    total_score = 0

    for x in range(len(map_data)):
        for y in range(len(map_data[0])):
            if map_data[x][y] == 0:  # Found a trailhead
                total_score += bfs_score(map_data, x, y)

    return total_score

def main():
    map_data = read_map('input.txt')
    total_score = calculate_total_score(map_data)
    print(f"Total score of all trailheads: {total_score}")

if __name__ == "__main__":
    main()