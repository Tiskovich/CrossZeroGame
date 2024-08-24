from unittest.mock import patch

import pytest

from game_app.constants import GameSymbols
from game_app.game import CrossZeroGame


@pytest.fixture
def game():
    return CrossZeroGame(game_size=3)

def test_initial_board(game):
    board = game.game_board.board
    assert all(cell == GameSymbols.EMPTY for row in board for cell in row)

def test_player_move_valid(game):
    with patch('builtins.input', return_value='1 1'):
        row, col = game.get_player_move()
        assert row == 0
        assert col == 0

def test_player_move_invalid(game):
    with patch('builtins.input', return_value='4 4'):
        with patch('builtins.print') as mocked_print:
            row, col = game.get_player_move()
            assert row == 0
            assert col == 0
            mocked_print.assert_called_with("Please enter a valid row and column (1-3).")

def test_check_winner_horizontal(game):
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 0)
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 1)
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 2)
    assert game.check_winner()

def test_check_winner_vertical(game):
    game.current_player_symbol = GameSymbols.CROSS
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 0)
    game.game_board.set_symbol(GameSymbols.CROSS, 1, 0)
    game.game_board.set_symbol(GameSymbols.CROSS, 2, 0)
    assert game.check_winner()

def test_check_winner_diagonal(game):
    game.current_player_symbol = GameSymbols.CROSS
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 0)
    game.game_board.set_symbol(GameSymbols.CROSS, 1, 1)
    game.game_board.set_symbol(GameSymbols.CROSS, 2, 2)
    assert game.check_winner()

def test_check_draw(game):
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 0)
    game.game_board.set_symbol(GameSymbols.ZERO, 0, 1)
    game.game_board.set_symbol(GameSymbols.CROSS, 0, 2)
    game.game_board.set_symbol(GameSymbols.ZERO, 1, 0)
    game.game_board.set_symbol(GameSymbols.CROSS, 1, 1)
    game.game_board.set_symbol(GameSymbols.ZERO, 1, 2)
    game.game_board.set_symbol(GameSymbols.CROSS, 2, 0)
    game.game_board.set_symbol(GameSymbols.ZERO, 2, 1)
    game.game_board.set_symbol(GameSymbols.CROSS, 2, 2)
    assert game.is_game_board_full()
    assert not game.check_winner()

def test_game_play_win_horizontal(monkeypatch):
    moves = ['1 1', '2 1', '1 2', '2 2', '1 3']
    with patch('builtins.input', side_effect=moves):
        with patch('builtins.print') as mocked_print:
            game = CrossZeroGame()
            game.play()
            calls = [pytest.call(f"Player {symbol.value} wins!") for symbol in [GameSymbols.CROSS]]
            mocked_print.assert_has_calls(calls)

def test_game_play_draw(monkeypatch):
    moves = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
    with patch('builtins.input', side_effect=moves):
        with patch('builtins.print') as mocked_print:
            game = CrossZeroGame()
            game.play()
            mocked_print.assert_any_call("It's a draw!")