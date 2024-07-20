class Grid:
    """
    A class to represent the grid for Conway's Game of Life.

    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        rows (list of int): The state of the grid represented as a list of integers.
    """

    def __init__(self, width, height):
        """
        Initialize the Grid class.

        Parameters:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.rows = [0] * height

    def toggle_cell(self, row, col):
        """
        Toggle the state of a cell in the grid.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        self.rows[row] ^= (1 << col)

    def is_alive(self, row, col):
        """
        Check if a cell is alive.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            bool: True if the cell is alive, False otherwise.
        """
        return (self.rows[row] & (1 << col)) != 0

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
                if self.is_alive(neighbor_row, neighbor_col):
                    neighbors += 1
        return neighbors

    def create_empty_grid(self):
        """
        Create an empty grid.

        Returns:
            Grid: The newly created empty grid.
        """
        return Grid(self.width, self.height)
