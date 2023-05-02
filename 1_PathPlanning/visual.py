import math
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3

class Grid:
    def __init__(self, rows, cols):
        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[row].append(0)

    def draw(self, screen):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                color = WHITE
                if self.grid[row][col] == 1:
                    color = GREEN
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN,
                                                 (MARGIN + HEIGHT) * row + MARGIN,
                                                  WIDTH,
                                                  HEIGHT])

# Define the Field class
class Field:
    def __init__(self, grid, rows, cols):
        self.grid = grid
        self.rows = rows
        self.cols = cols

    def click(self, x, y):
        row = y // (HEIGHT + MARGIN)
        col = x // (WIDTH + MARGIN)
        self.grid.grid[row][col] = 1

    def draw(self, screen):
        self.grid.draw(screen)

# Initialize the classes
rows = 20
cols = 20
grid = Grid(rows, cols)
field = Field(grid, rows, cols)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            field.click(pos[0], pos[1])

# The code here is called once per clock tick
# Let your algorithm loop here

    screen.fill(BLACK)

    field.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
