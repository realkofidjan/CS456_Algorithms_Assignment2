def find_words_in_puzzle(grid, word_list):
    found_words = []

    def horizontal_search(word):
        for i in range(num_rows):
            for j in range(num_cols):
                match = True

                for k in range(len(word)):
                    if grid[i][(j + k) % num_cols] != word[k]:
                        match = False
                        break

                if match:
                    found_words.append(word)
                    return

    def vertical_search(word):
        for j in range(num_cols):
            for i in range(num_rows):
                match = True

                for k in range(len(word)):
                    if grid[(i + k) % num_rows][j] != word[k]:
                        match = False
                        break

                if match:
                    found_words.append(word)
                    return

    def diagonal_search_upward(word):
        for i in range(num_rows):
            for j in range(num_cols):
                match = True

                for k in range(len(word)):
                    if grid[(i - k) % num_rows][(j + k) % num_cols] != word[k]:
                        match = False
                        break

                if match:
                    found_words.append(word)
                    return

    def diagonal_search_downward(word):
        for i in range(num_rows):
            for j in range(num_cols):
                match = True

                for k in range(len(word)):
                    if grid[(i + k) % num_rows][(j + k) % num_cols] != word[k]:
                        match = False
                        break

                if match:
                    found_words.append(word)
                    return

    num_rows = len(grid)
    num_cols = len(grid[0])

    for word in word_list:
        vertical_search(word)
        horizontal_search(word)
        diagonal_search_upward(word)
        diagonal_search_downward(word)

    return found_words


def print_grid(grid):
    for row in grid:
        print(' '.join(row))


word_grid = [['T', 'S', 'I', 'S'], ['I', 'H', 'A', 'W'], ['O', 'R', 'I', 'F'], ['I', 'N', 'D', 'S']]
to_find = ['THIS', 'IS', 'WORD', 'FIND']

print("Word Grid:")
print_grid(word_grid)

user_input = input("Enter the word you want to find: ").upper()
found_words = find_words_in_puzzle(word_grid, [user_input])

if found_words:
    print(f"The word '{found_words[0]}' was found in the puzzle.")
else:
    print(f"The word '{user_input}' was not found in the puzzle.")
