import re
def mainFunction(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
            pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
            matches = re.findall(pattern, content)
            total_sum = sum(int(x) * int(y) for x, y in matches)
            return total_sum
    except FileNotFoundError:
        print(f"File not found: {file}")
        return 0
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return 0
file = 'input.txt'
result = mainFunction(file)
print(f"Total sum: {result}")
