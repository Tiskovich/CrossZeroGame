from typing import List

from constants import GameSymbols


class GameBoard:

    def __init__(self, board_size: int):
        self.size = board_size
        self.board = self._create_board()

    def _create_board(self) -> List[List[GameSymbols]]:
        res = []
        for _ in range(self.size):
            res.append([GameSymbols.EMPTY for _ in range(self.size)])
        return res

    def print_board(self):
        print("Current board:")
        for row in self.board:
            print(" | ".join([symbol.value for symbol in row]))

    def set_symbol(self, symbol: GameSymbols, row: int, column: int):
        if self.board[row][column] != GameSymbols.EMPTY:
            raise ValueError(f"Cell already occupied. Please choose another one.")

        self.board[row][column] = symbol
