#
# 'blips' are the organisms
#

from random import random

MOVE_UP = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_RIGHT = 3
MOVE_STAY = 4

class Blip:

    def __init__(self):

        # weightings for this blip's tendencies to move in each direction
        self.move_up = random()
        self.move_down = random()
        self.move_left = random()
        self.move_right = random()
        self.move_stay = random()


    # gets this blip's next move based off of its tendencies
    def get_move(self):

        sum = self.sum_weightings()
        ran = random() * sum

        up_min    = 0
        down_min  = self.move_up
        left_min  = self.move_up + self.move_down
        right_min = self.move_up + self.move_down + self.move_left
        stay_min  = self.move_up + self.move_down + self.move_left + self.move_right

        if ran >= up_min and ran < down_min:
            return MOVE_UP
        elif ran >= down_min and ran < left_min:
            return MOVE_DOWN
        elif ran >= left_min and ran < right_min:
            return MOVE_LEFT
        elif ran >= right_min and ran < stay_min:
            return MOVE_RIGHT
        else:
            return MOVE_STAY


    def sum_weightings(self):
        return self.move_up + self.move_down + self.move_left + self.move_right + self.move_stay

    
# creates a new blip with the averages of two blips' tendencies
def create_offspring(blip_one, blip_two):

    offspring = Blip()

    offspring.move_up = mean(blip_one.move_up, blip_two.move_up)
    offspring.move_down = mean(blip_one.move_down, blip_two.move_down)
    offspring.move_left = mean(blip_one.move_left, blip_two.move_left)
    offspring.move_right = mean(blip_one.move_right, blip_two.move_right)
    offspring.move_stay = mean(blip_one.move_stay, blip_two.move_stay)

    return offspring


# returns the mean of two numbers
def mean(num_one, num_two):
    return (num_one + num_two) / 2;