import re

def extract_and_sum_mul_instructions_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the contents of the file
            corrupted_memory = file.read()

            # Initialize the flag to indicate mul instructions are enabled
            mul_enabled = True
            total_sum = 0

            # Loop through the corrupted memory, scanning for instructions
            i = 0
            while i < len(corrupted_memory):
                # Check for mul(X, Y) pattern
                mul_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', corrupted_memory[i:])
                if mul_match:
                    x, y = mul_match.groups()
                    if mul_enabled:
                        # Only execute mul if enabled
                        total_sum += int(x) * int(y)
                    # Skip over the matched mul instruction
                    i += len(mul_match.group(0))
                    continue

                # Check for do() and don't() instructions
                do_match = re.match(r'do\(\)', corrupted_memory[i:])
                dont_match = re.match(r"don't\(\)", corrupted_memory[i:])
                
                if do_match:
                    mul_enabled = True  # Enable future mul instructions
                    i += len(do_match.group(0))
                    continue
                elif dont_match:
                    mul_enabled = False  # Disable future mul instructions
                    i += len(dont_match.group(0))
                    continue

                # Move to the next character if no match is found
                i += 1

            return total_sum

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return 0
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return 0


# Specify the input file name
file_name = "input.txt"

# Call the function and print the result
result = extract_and_sum_mul_instructions_from_file(file_name)
print(f"Total sum: {result}")
