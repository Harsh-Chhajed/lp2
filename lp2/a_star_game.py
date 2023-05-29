import heapq


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def get_empty_cells(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    cells.append((i, j))
        return cells

    def make_move(self, move, player):
        self.board[move[0]][move[1]] = player

    def is_winner(self, player):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == player:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def evaluate_state(self):
        if self.is_winner('X'):
            return 1  # AI player wins
        elif self.is_winner('O'):
            return -1  # Human player wins
        else:
            return 0  # Draw or game not over

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def a_star_search(self, depth, move, maximizing_player):
        if depth == 0 or self.evaluate_state() != 0:
            return self.evaluate_state()

        if maximizing_player:
            max_eval = float('-inf')
            empty_cells = self.get_empty_cells()
            for cell in empty_cells:
                self.make_move(cell, 'X')
                eval = self.a_star_search(depth - 1, cell, False)
                self.make_move(cell, ' ')
                max_eval = max(max_eval, eval)
            return max_eval

        else:
            min_eval = float('inf')
            empty_cells = self.get_empty_cells()
            for cell in empty_cells:
                self.make_move(cell, 'O')
                eval = self.a_star_search(depth - 1, cell, True)
                self.make_move(cell, ' ')
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        max_eval = float('-inf')
        best_move = None
        empty_cells = self.get_empty_cells()

        for cell in empty_cells:
            self.make_move(cell, 'X')
            eval = self.a_star_search(len(empty_cells) - 1, cell, False)
            self.make_move(cell, ' ')

            if eval > max_eval:
                max_eval = eval
                best_move = cell

        return best_move


def play_game():
    game = TicTacToe()
    game.print_board()

    while True:
        human_move = input("Enter your move (row,column): ")
        row, col = map(int, human_move.split(','))
        game.make_move((row, col), 'O')

        if game.is_winner('O'):
            print("You win!")
            break

        empty_cells = game.get_empty_cells()

        if not empty_cells:
            print("It's a draw!")
            break

        best_move = game.get_best_move()
        game.make_move(best_move, 'X')
        print(f"AI's move: {best_move}")

        if game.is_winner('X'):
            print("AI wins!")
            break

        game.print_board()


play_game()
