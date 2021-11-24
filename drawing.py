#
# contains utility functions to make drawing easier
#

from pygame import gfxdraw

# draws a circle with anti-aliasing
def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)