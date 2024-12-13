from collections import defaultdict, deque

def parse_input(filename):
    """
    Parses the input file to extract ordering rules and updates.

    Args:
        filename (str): The input file containing rules and updates.

    Returns:
        tuple: A tuple with the ordering rules (set of tuples) and updates (list of lists).
    """
    with open(filename, 'r') as file:
        data = file.read().strip()
    
    rules_section, updates_section = data.split("\n\n")
    
    # Parse rules
    rules = set()
    for rule in rules_section.strip().splitlines():
        x, y = map(int, rule.split('|'))
        rules.add((x, y))
    
    # Parse updates
    updates = []
    for update in updates_section.strip().splitlines():
        updates.append(list(map(int, update.split(','))))
    
    return rules, updates

def is_in_correct_order(update, rules):
    """
    Checks if an update is in correct order according to the rules.

    Args:
        update (list): List of page numbers in the update.
        rules (set): Set of (X, Y) tuples indicating ordering rules.

    Returns:
        bool: True if the update is in correct order, otherwise False.
    """
    page_positions = {page: idx for idx, page in enumerate(update)}
    
    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] > page_positions[y]:
                return False
    return True

def correct_order(update, rules):
    """
    Corrects the order of an update based on the rules.

    Args:
        update (list): List of page numbers in the update.
        rules (set): Set of (X, Y) tuples indicating ordering rules.

    Returns:
        list: Correctly ordered update.
    """
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build graph and calculate in-degrees
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Kahn's algorithm for topological sorting
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def calculate_middle_sum(filename):
    """
    Calculates the sum of middle page numbers for corrected updates.

    Args:
        filename (str): Input file name.

    Returns:
        int: Sum of middle page numbers for corrected updates.
    """
    rules, updates = parse_input(filename)
    middle_sum = 0

    for update in updates:
        if not is_in_correct_order(update, rules):
            corrected = correct_order(update, rules)
            middle_sum += corrected[len(corrected) // 2]

    return middle_sum

# File name
input_filename = "input.txt"

# Calculate the sum of middle page numbers for corrected updates
result = calculate_middle_sum(input_filename)
print("Sum of middle page numbers for corrected updates:", result)
