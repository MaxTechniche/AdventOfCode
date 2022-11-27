from time import time

t1 = time()


def format_board(board):
    board = board.split('\n')
    board = [list(map(int, row.split())) for row in board]
    return board

def get_number_count(board, numbers):
    numbers = set(numbers)
    max_number_count = 0
    
    for row in range(len(board)):
        current_count = 0
        for col in range(len(board[row])):
            if board[row][col] in numbers:
                current_count += 1
        max_number_count = max(current_count, max_number_count)

    for col in range(len(board)):
        current_count = 0
        for row in range(len(board[col])):
            if board[row][col] in numbers:
                current_count += 1
        max_number_count = max(current_count, max_number_count)
    
    return max_number_count

def board_score(board, numbers):
    last_num = numbers[-1]
    numbers = set(numbers)
    score = 0
    for row in board:
        for num in row:
            if num not in numbers:
                score += num
    return score * last_num

with open("2021/Day_04/input") as f:
    lines = f.read().split('\n\n')
    picked_numbers = list(map(int, lines[0].split(',')))
    boards = lines[1:]
    
max_board_score = 0
max_numbers_used = 100
last_board_numbers_used = 0
last_board_score = float('inf')

# Go through each board
for board in boards:
    # Format board
    board = format_board(board)
    numbers = picked_numbers[:5]
    scored = False

    while not scored:
    
        # Get max row/col picked number count
        number_count = get_number_count(board, numbers)
        
        if number_count == 5:
            if len(numbers) < max_numbers_used:
                max_board_score = board_score(board, numbers)
                max_numbers_used = len(numbers)
            elif len(numbers) == max_numbers_used:
                max_board_score = max(max_board_score, board_score(board, numbers))
            scored = True
            # Part 2
            if len(numbers) > last_board_numbers_used:
                last_board_score = board_score(board, numbers)
                last_board_numbers_used = len(numbers)
            elif len(numbers) == last_board_numbers_used:
                last_board_score = min(last_board_score, board_score(board, numbers))
        else:
            # Add next group of numbers
            numbers = picked_numbers[:len(numbers) + 5 - number_count]

    
print(max_board_score)
print(last_board_score)
print("Time:", time() - t1)
