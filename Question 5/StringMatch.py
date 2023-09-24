# Function to perform brute force string matching
def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1


# Function to read input from file and write output to file
def file_input():
    with open("input.txt", "r") as file:
        num_cases = int(file.readline().strip())
        cases = [file.readline().strip() for _ in range(num_cases * 2)]
        results = []
        for i in range(0, len(cases), 2):
            text = cases[i]
            pattern = cases[i + 1]
            result = brute_force_string_match(text, pattern)
            results.append(result)

    with open("output.txt", "w") as file:
        for result in results:
            file.write(str(result) + "\n")


# Function to take input interactively
def interactive_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")
    result = brute_force_string_match(text, pattern)
    print(f"The index of the first occurrence of the pattern is: {result}")


# Main function to handle command-line arguments
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 StringMatch.py [interactive/file]")
        sys.exit(1)

    if sys.argv[1] == "interactive":
        interactive_input()
        answer = input("Do you want to match another string? ")
    elif sys.argv[1] == "file":
        file_input()
    else:
        print("Invalid argument. Use 'interactive' or 'file'.")
