import numpy as np
from typing import List, Tuple

def parse_input(filename: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Parse input file to extract robot positions and velocities.

    Args:
        filename (str): Path to input file

    Returns:
        List of tuples, each containing (position, velocity)
    """
    robots = []
    with open(filename, 'r') as f:
        for line in f:
            pos_str, vel_str = line.strip().split(' ')
            px, py = map(int, pos_str[2:].split(','))
            vx, vy = map(int, vel_str[2:].split(','))
            robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robots(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]],
                    time: int,
                    width: int,
                    height: int) -> np.ndarray:
    """
    Simulate robot movements and count robot positions after given time.

    Args:
        robots (List): List of robot (position, velocity) tuples
        time (int): Seconds to simulate
        width (int): Space width
        height (int): Space height

    Returns:
        numpy array of robot count per tile
    """
    # Initialize grid to track robot positions
    grid = np.zeros((height, width), dtype=int)

    for (px, py), (vx, vy) in robots:
        # Calculate final position after time, with wraparound
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        grid[final_y, final_x] += 1

    return grid

def is_christmas_tree(grid: np.ndarray) -> bool:
    """
    Check if the robot positions form a Christmas tree pattern.

    Args:
        grid (numpy array): Robot position grid

    Returns:
        Boolean indicating if a Christmas tree pattern is found
    """
    # Define a potential Christmas tree pattern
    # This is a simplistic representation and might need adjustment
    # based on the actual expected pattern
    tree_pattern = [
        [0, 0, 1, 0, 0],   # top of tree
        [0, 1, 1, 1, 0],   # middle of tree
        [1, 1, 1, 1, 1],   # base of tree
    ]

    height, width = grid.shape

    # Search for the pattern in the grid
    for y in range(height - len(tree_pattern)):
        for x in range(width - len(tree_pattern[0])):
            # Check if this section matches the tree pattern
            match = True
            for dy, row in enumerate(tree_pattern):
                for dx, val in enumerate(row):
                    if val == 1 and grid[y+dy, x+dx] == 0:
                        match = False
                        break
                if not match:
                    break

            if match:
                return True

    return False

def find_christmas_tree_time(filename: str, max_time: int = 10000, width: int = 101, height: int = 103) -> int:
    """
    Find the earliest time when robots form a Christmas tree pattern.

    Args:
        filename (str): Input file path
        max_time (int): Maximum time to search
        width (int): Space width
        height (int): Space height

    Returns:
        Time when Christmas tree pattern is found, or -1 if not found
    """
    # Parse input
    robots = parse_input(filename)

    # Search for Christmas tree pattern
    for time in range(max_time):
        # Simulate robot positions
        grid = simulate_robots(robots, time, width, height)

        # Check for Christmas tree pattern
        if is_christmas_tree(grid):
            return time

    return -1  # No pattern found within max_time

# Solve problem
result = find_christmas_tree_time('input.txt')
print(f"Seconds until Christmas Tree Pattern: {result}")