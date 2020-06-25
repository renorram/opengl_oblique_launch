from OpenGL.GL import *
from OpenGL.GLU import *
import math

GRAVITY = 10


class Ball:
    color = (0, 1, 1)
    scale = [1, 1, 1]
    translate_vector = [0.0, 0.0, 0.0]
    base_speed = 10
    is_fired = False
    angle = 0
    strength = 1

    current_time = 0
    current_acceleration = [0.0, GRAVITY]
    current_velocity = [0.0, 0.0]
    time_inc = 0.01

    def draw(self):
        self.process_shoot_distance()

        glPushMatrix()

        glColor3f(*self.color)
        glScale(*self.scale)
        glTranslatef(*self.translate_vector)

        ball = gluNewQuadric()
        gluQuadricDrawStyle(ball, GLU_FILL)
        gluQuadricNormals(ball, GLU_SMOOTH)
        gluSphere(ball, .5, 50, 50)

        glPopMatrix()

    def process_shoot_distance(self):
        if not self.is_fired:
            return

        if self.current_time == 0 or self.translate_vector[1] >= 0:
            self.current_time += self.time_inc
            self.current_acceleration = [
                -self.current_velocity[0],
                self.current_acceleration[1] - self.current_velocity[1]
            ]

            self.current_velocity = [
                self.current_velocity[0] + self.current_acceleration[0] * self.time_inc,
                self.current_velocity[1] + self.current_acceleration[1] * self.time_inc,
            ]

            self.translate_vector[0] = self.translate_vector[0] + self.current_velocity[0] * self.time_inc
            self.translate_vector[1] = self.translate_vector[1] + self.current_velocity[1] * self.time_inc

    def shoot(self, angle, strength):
        if not self.is_fired:
            self.is_fired = True
            self.angle = angle
            self.strength = strength

            self.current_velocity = [
                self.get_speed() * math.cos(math.radians(self.angle)),
                self.get_speed() * math.sin(math.radians(self.angle))
            ]

            self.current_acceleration = [0, GRAVITY]
            self.current_time = 0

    def reset_position(self):
        print("Last position", self.translate_vector)
        self.is_fired = False
        self.translate_vector[0] = 0
        self.translate_vector[1] = 0
        self.current_time = 0
        self.current_acceleration = [0.0, 0.0]
        self.current_velocity = [0.0, 0.0]

    def get_speed(self):
        return self.strength * self.base_speed
