def parse_rules_and_updates_from_file(filename):
    """
    Parses the rules and updates from an input file.

    Args:
        filename (str): The name of the input file.

    Returns:
        tuple: A tuple containing:
               - rules (set of tuples): Set of (X, Y) rules indicating X|Y.
               - updates (list of lists): List of updates, where each update is a list of page numbers.
    """
    with open(filename, 'r') as file:
        input_text = file.read()

    sections = input_text.strip().split("\n\n")
    rules = set()
    updates = []

    for rule in sections[0].strip().splitlines():
        x, y = map(int, rule.split('|'))
        rules.add((x, y))

    for update in sections[1].strip().splitlines():
        updates.append(list(map(int, update.split(','))))

    return rules, updates

def is_update_in_order(update, rules):
    """
    Checks if the given update is in the correct order based on the rules.

    Args:
        update (list): A list of page numbers in the update.
        rules (set): Set of rules as (X, Y) tuples indicating X|Y.

    Returns:
        bool: True if the update is in the correct order, False otherwise.
    """
    page_positions = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] > page_positions[y]:
                return False

    return True

def find_middle_page(update):
    """
    Finds the middle page number of the given update.

    Args:
        update (list): A list of page numbers in the update.

    Returns:
        int: The middle page number.
    """
    return update[len(update) // 2]

def calculate_middle_sum_from_file(filename):
    """
    Calculates the sum of middle page numbers for correctly-ordered updates from an input file.

    Args:
        filename (str): The name of the input file.

    Returns:
        int: The sum of middle page numbers for correctly-ordered updates.
    """
    rules, updates = parse_rules_and_updates_from_file(filename)
    middle_sum = 0

    for update in updates:
        if is_update_in_order(update, rules):
            middle_sum += find_middle_page(update)

    return middle_sum

# File name
input_filename = "input.txt"

# Calculate the result
result = calculate_middle_sum_from_file(input_filename)
print("Sum of middle page numbers for correctly-ordered updates:", result)
