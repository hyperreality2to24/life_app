class GameOfLife:
    """
    A class to represent Conway's Game of Life.

    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        grid (list of list of bool): The current state of the grid.
    """

    def __init__(self, width, height):
        """
        Initialize the GameOfLife class.

        Parameters:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.grid = self.create_grid()

    def create_grid(self):
        """
        Create an empty grid.

        Returns:
            list of list of bool: The newly created grid.
        """
        return [[False for _ in range(self.width)] for _ in range(self.height)]

    def toggle_cell(self, row, col):
        """
        Toggle the state of a cell in the grid.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        self.grid[row][col] = not self.grid[row][col]

    def get_neighbors(self, row, col):
        """
        Get the number of live neighbors for a cell.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of live neighbors.
        """
        neighbors = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                neighbor_row, neighbor_col = (row + dy) % self.height, (col + dx) % self.width
                neighbors += self.grid[neighbor_row][neighbor_col]
        return neighbors

    def update_grid(self):
        """
        Update the grid to the next state according to the rules of Conway's Game of Life.
        """
        new_grid = self.create_grid()
        for row in range(self.height):
            for col in range(self.width):
                alive = self.grid[row][col]
                neighbors = self.get_neighbors(row, col)
                if alive:
                    new_grid[row][col] = neighbors == 2 or neighbors == 3
                else:
                    new_grid[row][col] = neighbors == 3
        self.grid = new_grid
