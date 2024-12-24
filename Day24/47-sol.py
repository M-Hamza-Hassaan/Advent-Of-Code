def parse_input(input_text):
    lines = input_text.strip().split('\n')
    initial_values = {}
    gates = []
    parsing_gates = False
    
    for line in lines:
        line = line.strip()
        if not line:
            parsing_gates = True
            continue
            
        if not parsing_gates:
            if ':' in line:
                wire, value = line.split(':')
                initial_values[wire.strip()] = int(value.strip())
        else:
            if '->' in line:
                inputs, output = line.split('->')
                inputs = inputs.strip()
                output = output.strip()
                
                parts = inputs.split()
                if len(parts) == 3:  # Normal gate with two inputs
                    input1, op, input2 = parts
                    gates.append({
                        'type': op,
                        'inputs': [input1, input2],
                        'output': output
                    })
                else:
                    raise ValueError(f"Invalid gate format: {line}")
    
    return initial_values, gates

def evaluate_gate(gate_type, inputs):
    if gate_type == 'AND':
        return 1 if inputs[0] == 1 and inputs[1] == 1 else 0
    elif gate_type == 'OR':
        return 1 if inputs[0] == 1 or inputs[1] == 1 else 0
    elif gate_type == 'XOR':
        return 1 if inputs[0] != inputs[1] else 0
    else:
        raise ValueError(f"Unknown gate type: {gate_type}")

def simulate_circuit(initial_values, gates):
    wires = initial_values.copy()
    evaluated = set()
    
    while True:
        progress = False
        for i, gate in enumerate(gates):
            if i in evaluated:
                continue
                
            input_values = []
            can_evaluate = True
            
            # Check if we have all input values
            for input_wire in gate['inputs']:
                if input_wire not in wires:
                    can_evaluate = False
                    break
                input_values.append(wires[input_wire])
            
            if can_evaluate:
                result = evaluate_gate(gate['type'], input_values)
                wires[gate['output']] = result
                evaluated.add(i)
                progress = True
        
        if not progress:
            if len(evaluated) < len(gates):
                unevaluated = [gates[i] for i in range(len(gates)) if i not in evaluated]
                missing_wires = set()
                for gate in unevaluated:
                    for input_wire in gate['inputs']:
                        if input_wire not in wires:
                            missing_wires.add(input_wire)
                print(f"Missing wire values for: {missing_wires}")
            break
    
    return wires

def extract_z_value(wires):
    # Get all z-wires
    z_wires = [(int(wire[1:]), value) for wire, value in wires.items() 
               if wire.startswith('z') and wire[1:].isdigit()]
    
    # Sort by wire number
    z_wires.sort()
    
    # Construct binary string
    binary = ''
    for _, value in z_wires:
        binary = str(value) + binary  # Add at start for correct bit order
    
    # Convert to decimal
    if binary:
        return int(binary, 2)
    else:
        return 0

def main():
    try:
        with open('input.txt', 'r') as f:
            input_text = f.read()
        
        # Parse and simulate
        initial_values, gates = parse_input(input_text)
        final_wires = simulate_circuit(initial_values, gates)
        
        # Debug output
        print("\nWire values:")
        for wire in sorted(final_wires.keys()):
            print(f"{wire}: {final_wires[wire]}")
        
        # Calculate result
        result = extract_z_value(final_wires)
        print(f"\nFinal decimal value: {result}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
