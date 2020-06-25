from .cube import draw_cube

from .pyramid import draw_pyramid
from OpenGL.GL import *


def draw_arrow(translate=None, rotate=None):
    glPushMatrix()
    if translate:
        glTranslatef(*translate)

    if rotate:
        glRotatef(*rotate)

    draw_cube(scale=(.2, 1.5, .2))
    draw_pyramid(scale=(.4, .4, .2), translate=(-.11, 1.5, 0))
    glPopMatrix()
