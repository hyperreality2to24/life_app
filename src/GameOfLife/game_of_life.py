class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.create_grid()

    def create_grid(self):
        return [[False for _ in range(self.width)] for _ in range(self.height)]

    def toggle_cell(self, x, y):
        self.grid[x][y] = not self.grid[x][y]

    def get_neighbors(self, x, y):
        neighbors = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % self.width, (y + dy) % self.height
                neighbors += self.grid[nx][ny]
        return neighbors

    def update_grid(self):
        new_grid = self.create_grid()
        for y in range(self.height):
            for x in range(self.width):
                alive = self.grid[x][y]
                neighbors = self.get_neighbors(x, y)
                if alive:
                    new_grid[x][y] = neighbors == 2 or neighbors == 3
                else:
                    new_grid[x][y] = neighbors == 3
        self.grid = new_grid
