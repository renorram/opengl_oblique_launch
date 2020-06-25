from OpenGL.GL import *
from OpenGL.GLU import *


class Lighting:
    environment_light = (0.2, 0.2, 0.2, 1.0)
    diffuse_light = (0.7, 0.7, 0.7, 1.0)
    specular_light = (1.0, 1.0, 1.0, 1.0)  # cor da luz especular, 4 valor é transparencia
    light_position = (5, 5, 0, 1.)
    specularity = (1.0, 1.0, 1.0, 1.0)
    material_specularity = 1

    def set_lighting(self):
        # Habilita o modelo de colorização de Gouraud
        glShadeModel(GL_SMOOTH)

        # Define a refletância do material
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.specularity)
        # Define a concentração do brilho
        glMateriali(GL_FRONT_AND_BACK, GL_SHININESS, self.material_specularity)

        # Ativa o uso da luz ambiente
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.environment_light)

        # Define os parâmetros da luz de número 0
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.environment_light)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.diffuse_light)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.specular_light)

        glLightfv(GL_LIGHT0, GL_POSITION, self.light_position)

        # Habilita a definição da cor do material a partir da cor corrente
        glEnable(GL_COLOR_MATERIAL)
        # Habilita o uso de iluminação
        glEnable(GL_LIGHTING)
        # Habilita a luz de número 0
        glEnable(GL_LIGHT0)

    def set_lighting_position(self):
        """
        Should be called every after look at at the main loop
        to active light transformations

        :return:
        """
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_position)
        # draw a sphere right on where light is, helps debug :)
        # glPushMatrix()
        # glColor3f(1, 1, 1)
        # glTranslatef(self.light_position[0], self.light_position[1], self.light_position[2])
        # q = gluNewQuadric()
        # gluQuadricDrawStyle(q, GLU_FILL)
        # gluQuadricNormals(q, GLU_SMOOTH)
        # gluSphere(q, .7, 50, 50)
        # glPopMatrix()
