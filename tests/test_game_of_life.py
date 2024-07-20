import pytest
from GameOfLife.game_of_life import GameOfLife

@pytest.fixture
def game():
    return GameOfLife(80, 60)

def test_initial_grid(game):
    assert game.grid == [[False for _ in range(80)] for _ in range(60)]

def test_toggle_cell(game):
    game.toggle_cell(10, 10)
    assert game.grid[10][10] == True
    game.toggle_cell(10, 10)
    assert game.grid[10][10] == False

def test_get_neighbors(game):
    game.toggle_cell(10, 10)
    game.toggle_cell(11, 10)
    game.toggle_cell(12, 10)
    assert game.get_neighbors(11, 10) == 2
    assert game.get_neighbors(10, 10) == 1
    assert game.get_neighbors(13, 10) == 1

def test_update_grid(game):
    game.toggle_cell(10, 10)
    game.toggle_cell(11, 10)
    game.toggle_cell(12, 10)
    game.update_grid()
    assert game.grid[11][10] == True
    assert game.grid[11][9] == True
    assert game.grid[11][11] == True
    assert game.grid[10][10] == False
    assert game.grid[12][10] == False
