import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3

# ---
# Initialize your classes etc.here
# ---
class Field:
    
    def __init__(self, row, column):
        self.color = WHITE
        self.status = 'empty'
        self.row = row
        self.column = column
        self.neighbor=[]
        
    def set_color(self, color):
        self.color = color
        
    def set_status(self, status):
        self.status = status
        
class Grid:
   
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for row in range(height):
            self.grid.append([])
            for column in range(width):
                self.grid[row].append(Field(row, column))
                
    def get_field(self, row, column):
        return self.grid[row][column]
    
    def draw(self, screen):
        for row in range(self.height):
            for column in range(self.width):
                field = self.grid[row][column]
                color = field.color
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                                (MARGIN + HEIGHT) * row + MARGIN, 
                                                WIDTH, HEIGHT])



grid = Grid(20,20)

blocked_field = [[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[11,9],[12,9],[13,9],[14,9],[15,9],[16,9],[17,9]
                 ,[18,9],[19,9],[0,16],[1,16],[2,16],[3,16],[4,16],[5,16],[6,16],[7,16],[8,16],[9,16],[10,16]]
for field in blocked_field :
    b_field = grid.get_field(field[0],field[1])
    b_field.set_color(RED)
    b_field.set_status("blocked")







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

        # ---
        # The code here ist called once per clock tick
        #Let your algorithm loop here
        # ---

    screen.fill(BLACK)

    grid.draw(screen)
        
       


    pygame.display.flip()

    clock.tick(60)

pygame.quit()