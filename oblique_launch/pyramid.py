from OpenGL.GL import *

default_color = (0.318, 0.271, 0.224)

vertices = (
    (0, 0, 0),  # 0
    (1, 0, 0),  # 1
    (0, 0, -1),  # 2
    (1, 0, -1),  # 3
    (.5, 1, -.5),  # 4
)

edges = (
    # down face
    (0, 1, 2),
    (1, 3, 2),
    # front face
    (0, 1, 4),
    # right face
    (1, 3, 4),
    # back face
    (3, 2, 4),
    # left face
    (2, 0, 4),
)

normals = [
    (0, -1, 0),  # down face
    (0, -1, 0),  # down face
    (0, 0, 1),  # front face
    (1, 0, 0),  # right face
    (0, 0, -1),  # back face
    (-1, 0, 0),  # left face
]


def draw_pyramid(translate=None, scale=None, color=None, rotate=None):
    if color is None:
        color = default_color

    glPushMatrix()

    if translate:
        glTranslatef(*translate)

    if scale:
        glScalef(*scale)

    if rotate:
        glRotatef(*rotate)

    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    for (edge, normal) in zip(edges, normals):
        glNormal3d(*normal)
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

    glPopMatrix()
