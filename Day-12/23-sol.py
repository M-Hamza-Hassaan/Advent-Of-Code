def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def calculate_area_and_perimeter(region, grid):
    area = len(region)
    perimeter = 0
    for (x, y) in region:
        if x == 0 or grid[x-1][y] != grid[x][y]: perimeter += 1  # Top
        if x == len(grid) - 1 or grid[x+1][y] != grid[x][y]: perimeter += 1  # Bottom
        if y == 0 or grid[x][y-1] != grid[x][y]: perimeter += 1  # Left
        if y == len(grid[0]) - 1 or grid[x][y+1] != grid[x][y]: perimeter += 1  # Right
    return area, perimeter

def find_regions(grid):
    visited = set()
    regions = {}
    
    def dfs(x, y, plant_type):
        stack = [(x, y)]
        region = []
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            region.append((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] == plant_type:
                    stack.append((nx, ny))
        return region

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                plant_type = grid[i][j]
                region = dfs(i, j, plant_type)
                if plant_type not in regions:
                    regions[plant_type] = []
                regions[plant_type].append(region)
    
    return regions

def calculate_total_price(regions, grid):
    total_price = 0
    for plant_type, region_list in regions.items():
        for region in region_list:
            area, perimeter = calculate_area_and_perimeter(region, grid)
            total_price += area * perimeter
    return total_price

def main():
    grid = read_input('input.txt')
    regions = find_regions(grid)
    total_price = calculate_total_price(regions, grid)
    print(total_price)

if __name__ == "__main__":
    main()
