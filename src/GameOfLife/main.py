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
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = GREEN if grid[y][x] else WHITE
            pygame.draw.rect(surface, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Conway\'s Game of Life')
    clock = pygame.time.Clock()
    game = GameOfLife(GRID_WIDTH, GRID_HEIGHT)
    running = False
    button_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(BLACK)
        draw_grid(screen, game.grid)

        # Draw start/stop button
        button_text = "Stop" if running else "Start"
        button_color = RED if running else GREEN
        button_surface = button_font.render(button_text, True, WHITE, button_color)
        button_rect = button_surface.get_rect(center=(WINDOW_WIDTH - 50, 30))
        screen.blit(button_surface, button_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = not running
                elif not running:
                    x, y = event.pos
                    game.toggle_cell(y // CELL_SIZE, x // CELL_SIZE)

        if running:
            game.update_grid()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
