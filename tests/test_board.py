import pytest

from game_app.board import GameBoard
from game_app.constants import GameSymbols

@pytest.mark.parametrize('board_size', [
    pytest.param(3),
    pytest.param(4),
    pytest.param(5),
])
def test_create_board(board_size):
    game_board = GameBoard(board_size)
    assert len(game_board.board) == board_size
    assert all(len(row) == board_size for row in game_board.board)
    assert all(cell == GameSymbols.EMPTY for row in game_board.board for cell in row)

@pytest.mark.parametrize('symbol', [
    pytest.param(GameSymbols.ZERO, id='zero'),
    pytest.param(GameSymbols.CROSS, id='cross'),
])
def test_set_symbol(symbol):
    game_board = GameBoard(3)
    game_board.set_symbol(symbol, 1, 1)
    assert game_board.board[1][1] == symbol


def test_set_symbol_already_occupied():
    game_board = GameBoard(3)
    game_board.set_symbol(GameSymbols.CROSS, 1, 1)
    with pytest.raises(ValueError):
        game_board.set_symbol(GameSymbols.ZERO, 1, 1)


def test_print_board(capsys):
    game_board = GameBoard(3)
    game_board.set_symbol(GameSymbols.X, 1, 1)
    game_board.print_board()
    captured = capsys.readouterr()
    expected_output = "\n".join([
        "  |   |  ",
        "  | X |  ",
        "  |   |  ",
        ""
    ])
    assert captured.out == expected_output
