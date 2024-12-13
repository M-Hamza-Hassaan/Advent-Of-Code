def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n\n')

def parse_machines(data):
    machines = []
    for machine in data:
        lines = machine.split('\n')
        button_a = tuple(map(int, lines[0].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')))
        button_b = tuple(map(int, lines[1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')))
        prize = tuple(map(int, lines[2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', ')))
        machines.append((button_a, button_b, prize))
    return machines

def min_tokens_to_win(button_a, button_b, prize):
    x_a, y_a = button_a
    x_b, y_b = button_b
    x_p, y_p = prize

    for a in range(101):
        for b in range(101):
            if a * x_a + b * x_b == x_p and a * y_a + b * y_b == y_p:
                return a * 3 + b * 1
    return float('inf')

def total_min_tokens(machines):
    total_tokens = 0
    for button_a, button_b, prize in machines:
        tokens = min_tokens_to_win(button_a, button_b, prize)
        if tokens != float('inf'):
            total_tokens += tokens
    return total_tokens

def main():
    data = read_input('input.txt')
    machines = parse_machines(data)
    result = total_min_tokens(machines)
    print(result)

if __name__ == "__main__":
    main()
