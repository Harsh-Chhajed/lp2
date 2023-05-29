def is_safe(board, row, col, N):
    # Check if the current position is safe for the queen

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # If no conflicts found, return True
    return True


def solve_n_queens_util(board, col, N):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Recursive case: Try placing the queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place the remaining queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing the queen doesn't lead to a solution, backtrack and remove it
            board[i][col] = 0

    # If no valid placement found, return False
    return False


def solve_n_queens(N):
    # Create an empty N x N chessboard
    board = [[0] * N for _ in range(N)]

    # Call the utility function to solve the problem
    if not solve_n_queens_util(board, 0, N):
        print("No solution exists for N = ", N)
        return

    # Print the solution
    for row in board:
        print(row)


# Example usage: Solve N-Queens for N = 4
solve_n_queens(4)
