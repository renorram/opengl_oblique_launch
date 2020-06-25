import pygame
import os
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from oblique_launch import Camera, Controls, Lighting, Ball, TextureLoader, draw_ground

base_resources_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
texture_loader = TextureLoader(base_resources_path)

# see controls
MAX_STRENGTH = 10


def event_capture_loop(controls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            controls.handle_key(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            controls.orbital_control(event.button)


def main():
    eye = (0, 0, 10)
    target = (0, 0, 0)
    up = (0, 1, 0)

    pygame.init()
    display = (1600, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # base settings
    glClearColor(0.761, 0.773, 0.824, 1.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_AUTO_NORMAL)

    # set perspective
    gluPerspective(45, (display[0] / display[1]), .1, 50.0)
    camera = Camera(eye, target, up)
    controls = Controls(camera, MAX_STRENGTH)

    lighting = Lighting()
    lighting.set_lighting()

    ball = Ball()
    controls.scene_items.append(ball)
    # ground texture
    ground_texture = texture_loader.load_texture('ground_texture.png')

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)

        glPushMatrix()
        glTranslate(0, -1, 0)
        camera.set_look_at()
        lighting.set_lighting_position()

        event_capture_loop(controls)
        controls.draw_crontrols()

        draw_ground(ground_texture)
        glTranslatef(0, -.5, 0)
        ball.draw()

        glPopMatrix()

        pygame.display.flip()
        # pygame.time.wait(1)


if __name__ == '__main__':
    main()
