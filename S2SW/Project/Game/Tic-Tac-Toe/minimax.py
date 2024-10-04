class Minimax:
    def __init__(self, max_depth=float('inf')):
        self.max_depth = max_depth

    def get_best_move(self, board, player):
        best_val = float('-inf') if player == 'O' else float('inf')
        best_move = -1

        for i in range(9):
            if board[i] == " ":
                board[i] = player
                if player == 'O':  # Maximizing player
                    move_val = self._minimax(board, 0, False, float('-inf'), float('inf'))
                    if move_val > best_val:
                        best_move = i
                        best_val = move_val
                else:  # Minimizing player
                    move_val = self._minimax(board, 0, True, float('-inf'), float('inf'))
                    if move_val < best_val:
                        best_move = i
                        best_val = move_val
                board[i] = " "  # Undo the move

        return best_move

    def _minimax(self, board, depth, is_maximizing, alpha, beta):
        if depth >= self.max_depth or self._game_over(board):
            return self._evaluate(board)

        if is_maximizing:
            best_val = float('-inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = 'O'
                    eval = self._minimax(board, depth + 1, False, alpha, beta)
                    board[i] = " "
                    best_val = max(best_val, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return best_val
        else:
            best_val = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = 'X'
                    eval = self._minimax(board, depth + 1, True, alpha, beta)
                    board[i] = " "
                    best_val = min(best_val, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return best_val

    def _game_over(self, board):
        # Check for a win
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                return True

        # Check for a draw
        if " " not in board:
            return True

        return False

    def _evaluate(self, board):
        # Simple evaluation: +10 for O win, -10 for X win, 0 for draw
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]]:
                if board[combo[0]] == 'O':
                    return 10
                elif board[combo[0]] == 'X':
                    return -10
        return 0