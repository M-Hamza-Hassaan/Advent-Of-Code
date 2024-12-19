def is_design_possible(patterns, design):
    # Recursive function to check if a design can be created
    if design == "":
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if is_design_possible(patterns, design[len(pattern):]):
                return True
    return False

def count_possible_designs(patterns, designs):
    possible_count = 0
    for design in designs:
        if is_design_possible(patterns, design):
            possible_count += 1
    return possible_count

def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")
    
    # Parse patterns and designs
    patterns = lines[0].split(", ")
    designs = lines[2:]  # Designs start after the blank line

    # Count how many designs are possible
    result = count_possible_designs(patterns, designs)
    print(result)

if __name__ == "__main__":
    main()
