from functools import lru_cache

def count_design_ways(patterns, design):
    @lru_cache(None)
    def helper(remaining_design):
        if remaining_design == "":
            return 1  # One way to create an empty design
        ways = 0
        for pattern in patterns:
            if remaining_design.startswith(pattern):
                ways += helper(remaining_design[len(pattern):])
        return ways

    return helper(design)

def total_design_ways(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_design_ways(tuple(patterns), design)
    return total_ways

def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")
    
    # Parse patterns and designs
    patterns = lines[0].split(", ")
    designs = lines[2:]  # Designs start after the blank line

    # Calculate the total number of ways to make all designs
    result = total_design_ways(patterns, designs)
    print(result)

if __name__ == "__main__":
    main()
