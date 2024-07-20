import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from .game_of_life import GameOfLife

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GRID_WIDTH, GRID_HEIGHT = 80, 60
CELL_SIZE = 10
FPS = 10

# Colors
CLR_TEXT = (255, 255, 255) # White
CLR_BACKGROUND = (0, 0, 0) # Black
CLR_GRID = (200, 200, 200) # Gray 
CLR_LIFE = (0, 255, 0)     # Green
CLR_DEAD = (255, 255, 255) # White
CLR_START = (0, 0, 255)    # Blue
CLR_STOP = (255, 0, 0)     # Red

def draw_grid(surface, grid):
    """
    Draw the grid on the given surface.

    Parameters:
        surface (pygame.Surface): The surface to draw on.
        grid (Grid): The grid object representing the state of the grid.
    """
    for row in range(grid.height):
        for col in range(grid.width):
            color = CLR_LIFE if grid.is_alive(row, col) else CLR_DEAD
            pygame.draw.rect(surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, CLR_GRID, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    """
    Main function to run the Conway's Game of Life simulation.
    """
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    game = GameOfLife(GRID_WIDTH, GRID_HEIGHT)
    is_running = False
    button_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(CLR_BACKGROUND)
        draw_grid(screen, game.grid)

        # Draw start/stop button
        button_text = "Stop" if is_running else "Start"
        button_color = CLR_STOP if is_running else CLR_START
        button_surface = button_font.render(button_text, True, CLR_TEXT, button_color)
        button_rect = button_surface.get_rect(center=(WINDOW_WIDTH - 50, 30))
        screen.blit(button_surface, button_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    is_running = not is_running
                elif not is_running:
                    col, row = event.pos
                    game.toggle_cell(row // CELL_SIZE, col // CELL_SIZE)

        if is_running:
            game.update_grid()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
