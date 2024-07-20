from .grid import Grid

class GameOfLife:
    """
    A class to represent Conway's Game of Life.

    Attributes:
        grid (Grid): The grid representing the state of the game.
    """

    def __init__(self, width, height):
        """
        Initialize the GameOfLife class.

        Parameters:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.grid = Grid(width, height)

    def toggle_cell(self, row, col):
        """
        Toggle the state of a cell in the grid.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        self.grid.toggle_cell(row, col)

    def update_grid(self):
        """
        Update the grid to the next state according to the rules of Conway's Game of Life.
        """
        new_grid = self.grid.create_empty_grid()
        for row in range(self.grid.height):
            for col in range(self.grid.width):
                alive = self.grid.is_alive(row, col)
                neighbors = self.grid.get_neighbors(row, col)
                if alive:
                    if neighbors == 2 or neighbors == 3:
                        new_grid.toggle_cell(row, col)  # Keep the cell alive
                else:
                    if neighbors == 3:
                        new_grid.toggle_cell(row, col)  # Make the cell alive
        self.grid = new_grid
