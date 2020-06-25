from .cube import draw_cube
from OpenGL.GL import *


def draw_target(translate=None):
    glPushMatrix()

    if translate:
        glTranslatef(*translate)

    draw_cube(color=(0.553, 0.957, 0.682))

    glPopMatrix()
