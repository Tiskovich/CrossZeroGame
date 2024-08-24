from game_app.board import GameBoard
from game_app.constants import GameSymbols


class CrossZeroGame:
    def __init__(self, game_size: int = 3):
        self.game_board = GameBoard(game_size)
        self.current_player_symbol = GameSymbols.CROSS

    def get_player_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player_symbol.value}, enter your move in next format 'row column',"
                             f" where row and column must be from 1 to {self.game_board.size}: ")
                row, col = map(int, move.split())
                if row in range(1, self.game_board.size + 1) and col in range(1, self.game_board.size + 1):
                    return row - 1, col - 1
                else:
                    print(f"Please enter a valid row and column (1-{self.game_board.size}).")
            except ValueError:
                print(
                    "Invalid input. Please enter row and column as two numbers separated by space, like 'row column'.")

    def check_winner(self):
        for row in self.game_board.board:
            if all([cell == self.current_player_symbol for cell in row]):
                return True

        for col in range(self.game_board.size):
            if all([row[col] == self.current_player_symbol for row in self.game_board.board]):
                return True

        if all([row[index] == self.current_player_symbol for index, row in enumerate(self.game_board.board)]):
            return True

        if all([row[-(1 + index)] == self.current_player_symbol for index, row in enumerate(self.game_board.board)]):
            return True

        return False

    def is_game_board_full(self):
        return all([cell in [GameSymbols.CROSS, GameSymbols.ZERO] for row in self.game_board.board for cell in row])

    def play(self):
        while True:
            self.game_board.print_board()
            row, col = self.get_player_move()

            try:
                self.game_board.set_symbol(self.current_player_symbol, row, col)
            except ValueError as e:
                print(e)
                continue

            if self.check_winner():
                self.game_board.print_board()
                print(f"Player {self.current_player_symbol.value} wins!")
                break

            if self.is_game_board_full():
                self.game_board.print_board()
                print("It's a draw!")
                break

            self.current_player_symbol = GameSymbols.ZERO if self.current_player_symbol == GameSymbols.CROSS else GameSymbols.CROSS


if __name__ == "__main__":
    game = CrossZeroGame()
    game.play()
