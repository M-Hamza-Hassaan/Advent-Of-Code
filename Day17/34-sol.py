import re

def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
    regs, program = data.split('\n\n')
    A, B, C = map(int, re.findall('-?\d+', regs))
    program = list(map(int, program.split(':')[1].strip().split(',')))
    return A, B, C, program

def get_combo_value(x, A, B, C):
    if 0 <= x <= 3:
        return x
    elif x == 4:
        return A
    elif x == 5:
        return B
    elif x == 6:
        return C
    raise ValueError("Invalid combo operand value.")

def simulate_program(A, B, C, program, find_match=False):
    ip = 0
    outputs = []
    while ip < len(program):
        if ip + 1 >= len(program):
            break
        cmd = program[ip]
        op = program[ip + 1]
        combo = get_combo_value(op, A, B, C)

        if cmd == 0:
            A = A // (2 ** combo)
        elif cmd == 1:
            B ^= op
        elif cmd == 2:
            B = combo % 8
        elif cmd == 3:
            if A != 0:
                ip = op - 2  # adjust for the automatic increment
        elif cmd == 4:
            B ^= C
        elif cmd == 5:
            out = combo % 8
            outputs.append(out)
            if find_match and len(outputs) <= len(program) and out != program[len(outputs)-1]:
                return None
        elif cmd == 6:
            B = A // (2 ** combo)
        elif cmd == 7:
            C = A // (2 ** combo)
        ip += 2
    
    return outputs if not find_match else None if outputs != program else True

def find_min_A_for_match(B, C, program):
    Ast = 1
    while True:
        result = simulate_program(Ast, B, C, program, find_match=True)
        if result is True:
            return Ast
        Ast += 1

# Read input data
A, B, C, program = parse_input("input.txt")



# Part Two
min_A = find_min_A_for_match(B, C, program)
print("Minimum A for Part Two:", min_A)