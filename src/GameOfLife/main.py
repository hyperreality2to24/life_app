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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_grid(surface, grid):
    """
    Draw the grid on the given surface.

    Parameters:
        surface (pygame.Surface): The surface to draw on.
        grid (list of list of bool): The current state of the grid.
    """
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = GREEN if grid[row][col] else WHITE
            pygame.draw.rect(surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, GRAY, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

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
        screen.fill(BLACK)
        draw_grid(screen, game.grid)

        # Draw start/stop button
        button_text = "Stop" if is_running else "Start"
        button_color = RED if is_running else GREEN
        button_surface = button_font.render(button_text, True, WHITE, button_color)
        button_rect = button_surface.get_rect(center=(WINDOW_WIDTH - 50, 30))
        screen.blit(button_surface, button_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  # Start/stop button clicked
                    is_running = not is_running          # Toggle the running state
                elif not is_running:
                    col, row = event.pos
                    game.toggle_cell(row // CELL_SIZE, col // CELL_SIZE)

        if is_running:
            game.update_grid()

        pygame.display.flip()
        clock.tick(FPS)  # Limit the frame rate to FPS by sleeping the correct amount of time

if __name__ == '__main__':
    main()
