from collections import defaultdict

def find_triplets_with_t(input_file):
    # Read the input and parse connections
    with open(input_file, 'r') as file:
        connections = [line.strip().split('-') for line in file.readlines()]
    
    # Build the adjacency list for the network
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    
    triplets_with_t = set()
    
    # Find all triplets
    for node in graph:
        for neighbor1 in graph[node]:
            for neighbor2 in graph[node]:
                if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                    triplet = tuple(sorted([node, neighbor1, neighbor2]))
                    triplets_with_t.add(triplet)
    
    # Filter triplets with at least one 't' starting name
    count = sum(1 for triplet in triplets_with_t if any(comp.startswith('t') for comp in triplet))
    
    return count

# Usage
input_file = 'input.txt'  # Make sure the input file is in the same directory
result = find_triplets_with_t(input_file)
print(result)
