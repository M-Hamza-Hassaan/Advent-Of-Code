def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(file_name):
    safe_count = 0

    try:
        with open(file_name, 'r') as file:
            for line in file:
                report = list(map(int, line.strip().split()))
                if is_safe(report):
                    safe_count += 1
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return safe_count
file_name = "input.txt"
safe_reports = count_safe_reports(file_name)
print(f"Number of safe reports: {safe_reports}")