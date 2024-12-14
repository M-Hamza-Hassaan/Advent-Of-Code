# Constants
WIDTH = 101
HEIGHT = 103
TIME = 100

# Load input
with open("input.txt") as f:
    lines = f.readlines()

# Parse positions and velocities
robots = []
for line in lines:
    parts = line.split()
    px, py = map(int, parts[0][2:].split(','))
    vx, vy = map(int, parts[1][2:].split(','))
    robots.append((px, py, vx, vy))

# Update positions after 100 seconds
final_positions = []
for px, py, vx, vy in robots:
    x_new = (px + vx * TIME) % WIDTH
    y_new = (py + vy * TIME) % HEIGHT
    final_positions.append((x_new, y_new))

# Count robots in each quadrant
q1 = q2 = q3 = q4 = 0
mid_x = WIDTH // 2
mid_y = HEIGHT // 2

for x, y in final_positions:
    if x == mid_x or y == mid_y:
        continue  # Skip robots on the middle lines
    if x < mid_x and y < mid_y:
        q1 += 1
    elif x >= mid_x and y < mid_y:
        q2 += 1
    elif x < mid_x and y >= mid_y:
        q3 += 1
    elif x >= mid_x and y >= mid_y:
        q4 += 1

# Calculate the safety factor
safety_factor = q1 * q2 * q3 * q4

print("Safety Factor:", safety_factor)





