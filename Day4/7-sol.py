def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-right diagonal
        (-1, -1),# Up-left diagonal
        (1, -1), # Down-left diagonal
        (-1, 1)  # Up-right diagonal
    ]
    
    def is_word_at(row, col, dr, dc):
        for i in range(word_len):
            r, c = row + i * dr, col + i * dc
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
                return False
        return True

    count = 0
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if is_word_at(row, col, dr, dc):
                    count += 1
    return count

# Read the input grid from the file
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Word to search
word = "XMAS"

# Count occurrences
total_occurrences = count_word_occurrences(grid, word)
print("Total occurrences of 'XMAS':", total_occurrences)
