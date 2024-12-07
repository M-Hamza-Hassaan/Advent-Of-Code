from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate the expression with the given numbers and operators."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result

def is_solvable(target, numbers):
    """Check if the target can be achieved by placing operators."""
    n = len(numbers)
    for ops in product(["+", "*"], repeat=n - 1):
        if evaluate_expression(numbers, ops) == target:
            return True
    return False

def main():
    total_calibration_result = 0

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            target, numbers = line.split(":")
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            
            if is_solvable(target, numbers):
                total_calibration_result += target

    print(f"Total Calibration Result: {total_calibration_result}")

if __name__ == "__main__":
    main()
