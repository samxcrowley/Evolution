import sys
import pygame
from grid import Grid
import drawing

APP_WIDTH = 1280
APP_HEIGHT = 900

GRID_SIZE = 128
max_num_blips = 1000
max_num_gens = 100
max_num_steps = 100

num_gens = 0
num_steps = 0

# read config variables
with open('config.txt') as f:
    lines = f.readlines()
    GRID_SIZE = int(lines[0])
    max_num_blips = int(lines[1])
    max_num_gens = int(lines[2])
    max_num_steps = int(lines[3])

CELL_SIZE = 6
MARGIN = int((APP_HEIGHT - (GRID_SIZE * CELL_SIZE)) / 2)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
clock = pygame.time.Clock()

grid = Grid(GRID_SIZE, GRID_SIZE)
grid.generate_birth(max_num_blips)

if __name__ == "__main__":

    while 1:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLACK)

        # draw box around grid
        start_x = int(MARGIN * 0.75)
        start_y = MARGIN
        buf = 6
        box_size = GRID_SIZE * CELL_SIZE + (buf * 2)

        pygame.draw.rect(screen, (200, 200, 200), (start_x - buf, start_y - buf, box_size, box_size), 3)

        # draw Blips in grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):

                blip = grid.get_blip(x, y)

                if blip == None:
                    continue

                r = int(CELL_SIZE / 2) - 1
                drawing.draw_circle(screen, start_x + (x * CELL_SIZE) + r, start_y + (y * CELL_SIZE) + r, r, WHITE)

        if num_steps < max_num_steps:
            grid.step()
            num_steps += 1
        else:
            if num_gens < max_num_gens:
                num_gens += 1
                num_steps = 0
                grid = Grid(GRID_SIZE, GRID_SIZE)
                grid.generate_birth(max_num_blips)

        pygame.display.flip()