# Directions: Up, Right, Down, Left
DIRECTIONS = ['^', '>', 'v', '<']
# Helper to turn right
def turn_right(current_direction):
    index = DIRECTIONS.index(current_direction)
    return DIRECTIONS[(index + 1) % 4]
# Helper to move forward
def move_forward(position, direction):
    r, c = position
    if direction == '^':
        return r - 1, c
    elif direction == '>':
        return r, c + 1
    elif direction == 'v':
        return r + 1, c
    elif direction == '<':
        return r, c - 1
# Simulate guard movement with an obstruction
def simulate_with_obstruction(grid, start_state, obstruction, max_steps=10000):
    rows, cols = len(grid), len(grid[0])
    r, c, direction = start_state
    visited = set()
    # Place the obstruction
    grid[obstruction[0]][obstruction[1]] = '#'
    for step in range(max_steps):
        # Detect loop
        if (r, c, direction) in visited:
            # Remove the obstruction before returning
            grid[obstruction[0]][obstruction[1]] = '.'
            return True  # A loop is detected
        visited.add((r, c, direction))
        # Check next position
        next_r, next_c = move_forward((r, c), direction)
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '#':
            direction = turn_right(direction)  # Turn right if obstacle ahead
        else:
            r, c = next_r, next_c  # Move forward
        # Exit if out of bounds
        if not (0 <= r < rows and 0 <= c < cols):
            grid[obstruction[0]][obstruction[1]] = '.'
            return False  # No loop detected
    # Fallback for too many steps
    grid[obstruction[0]][obstruction[1]] = '.'
    return False
# Main function to solve the puzzle
def find_possible_obstruction_positions(grid, start_state):
    rows, cols = len(grid), len(grid[0])
    possible_positions = []
    # Check all positions for potential obstructions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != (start_state[0], start_state[1]):
                if simulate_with_obstruction(grid, start_state, (r, c)):
                    possible_positions.append((r, c))
    return possible_positions
# Function to read the input file
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    grid = []
    start_state = None
    for r, line in enumerate(lines):
        row = list(line.strip())
        for c, char in enumerate(row):
            if char in DIRECTIONS:  # Detect guard's starting position and direction
                start_state = (r, c, char)
        grid.append(row)
    if not start_state:
        raise ValueError("Guard's starting position and direction not found in the input.")
    return grid, start_state
# Main execution
if __name__ == "__main__":
    # Change this to the path of your input file
    input_file = "input.txt"
    grid, start_state = read_input(input_file)
    # Solve the puzzle
    possible_positions = find_possible_obstruction_positions(grid, start_state)
    print(f"Possible positions to add an obstruction: {possible_positions}")
    print(f"Number of possible positions: {len(possible_positions)}")