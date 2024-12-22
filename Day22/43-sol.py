def calculate_2000th_secret_sum(file_path):
    try:
        MODULO = 16777216

        # Function to calculate the next secret number
        def next_secret(secret):
            secret = (secret ^ (secret * 64)) % MODULO
            secret = (secret ^ (secret // 32)) % MODULO
            secret = (secret ^ (secret * 2048)) % MODULO
            return secret

        # Read input from the file
        with open(file_path, 'r') as file:
            initial_secrets = [int(line.strip()) for line in file if line.strip().isdigit()]

        total_sum = 0

        # Process each initial secret number
        for secret in initial_secrets:
            for _ in range(2000):  # Generate 2000th secret
                secret = next_secret(secret)
            total_sum += secret  # Add the 2000th secret to the sum

        return total_sum

    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except ValueError:
        print("Error: The file contains invalid data.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Input file path
file_path = "input.txt"

# Calculate and print the result
result = calculate_2000th_secret_sum(file_path)
if result is not None:
    print(f"The sum of the 2000th secret numbers is: {result}")