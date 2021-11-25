#
# the Grid is the world in which the blips live, move, and evolve in
#

from blip import Blip, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_STAY, create_offspring
from random import random

class Grid:

    def __init__(self, width, height, max_num_blips):

        self.width = width
        self.height = height

        self.max_num_blips = max_num_blips

        self.grid = make_2d_array(self.width, self.height)


    # creates n blips in random positions in the grid
    def generate_birth(self, n):
        for i in range(n):
            self.birth_random_blip()


    # all blips in the right side of the grid reproduce
    def reproduce_blips(self):

        # list of all blips in the right side
        parents = []

        # list of new blips produced by surviving parents
        children = []

        # add all blips who are on the right side to parents list
        for x in range(int(self.width / 2), self.width):
            for y in range(self.height):
                if self.grid[x][y] != None:
                    parents.append(self.grid[x][y])

        # reset grid
        self.grid = make_2d_array(self.width, self.height)

        for n in range(self.max_num_blips):
            children.append(self.birth_reproduced_blip(parents))

        for c in children:
            self.place_blip(c)


    # creates a new blip in a random unoccupied cell
    def birth_random_blip(self):

        x = int(random() * self.width)
        y = int(random() * self.height)

        while self.grid[x][y] != None:
            x = int(random() * self.width)
            y = int(random() * self.height)

        self.grid[x][y] = Blip()


    # takes a random pair of parents and returns an offspring of them
    def birth_reproduced_blip(self, parents):
        parent_one = parents[int(random() * len(parents))]
        parent_two = parents[int(random() * len(parents))]

        child = create_offspring(parent_one, parent_two)
        return child
    

    # places blip in random unoccupied cell
    def place_blip(self, blip):

        x = int(random() * self.width)
        y = int(random() * self.height)

        while self.grid[x][y] != None:
            x = int(random() * self.width)
            y = int(random() * self.height)

        self.grid[x][y] = blip


    # returns blip at (x, y)
    def get_blip(self, x, y):
        return self.grid[x][y]


    # steps the grid to next cycle
    def step(self):

        for x in range(self.width):
            for y in range(self.height):
                self.move_blip(x, y)


    # moves blip at (x, y) by the move it returns from its get_move() method
    def move_blip(self, x, y):
        
        blip = self.grid[x][y]
        if blip == None:
            return
        move = blip.get_move()

        new_x = x
        new_y = y

        if move == MOVE_UP:
            if y == 0:
                return
            new_y = y - 1
        elif move == MOVE_DOWN:
            if y == self.height - 1:
                return
            new_y = y + 1
        elif move == MOVE_LEFT:
            if x == 0:
                return
            new_x = x - 1
        elif move == MOVE_RIGHT:
            if x == self.width - 1:
                return
            new_x = x + 1

        if self.grid[new_x][new_y] != None:
            return

        self.grid[new_x][new_y] = blip

        if move != MOVE_STAY:
            self.grid[x][y] = None


# utility function which creates a 2D array with dimensions width, height
# intially all elements are filled with None
def make_2d_array(width, height):

    cols = []
    for x in range(width):
        row = []
        for y in range(height):
            row.append(None)
        cols.append(row)

    return cols