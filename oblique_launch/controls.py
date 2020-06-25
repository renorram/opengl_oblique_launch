from .camera import Camera
from .cube import draw_in_space
from .arrow import draw_arrow
from .target import draw_target
from pygame.constants import *


class Controls:
    key_map = {
        K_w: 'move_frontwards',
        K_s: 'move_backwards',
        K_d: 'move_right',
        K_a: 'move_left',

        K_UP: 'look_up',
        K_DOWN: 'look_down',
        K_RIGHT: 'look_right',
        K_LEFT: 'look_left',

        K_SPACE: 'shoot_ball',
        K_r: 'reset',

        K_PAGEUP: 'increase_strength',
        K_PAGEDOWN: 'decrease_strength',
        K_m: 'increase_angle',
        K_n: 'decrease_angle',

        K_i: 'move_target_up',
        K_k: 'move_target_down',
        K_j: 'move_target_left',
        K_l: 'move_target_right',
    }

    strength = 1
    angle = 0
    max_strength = 5

    target_position = [5, -1, 0]

    scene_items = []

    def __init__(self, camera: Camera, max_strength: int):
        self.camera = camera
        self.max_strength = max_strength

    def handle_key(self, key):
        if key not in self.key_map:
            return

        func = self.__getattribute__(self.key_map[key])

        func()

    def move_frontwards(self):
        self.camera.eye_move_frontwards()

    def move_backwards(self):
        self.camera.eye_move_backwards()

    def move_right(self):
        self.camera.eye_move_right()

    def move_left(self):
        self.camera.eye_move_left()

    def look_up(self):
        self.camera.eye_look_up()

    def look_down(self):
        self.camera.eye_look_down()

    def look_right(self):
        self.camera.eye_look_right()

    def look_left(self):
        self.camera.eye_look_left()

    def orbital_control(self, button):
        if button == 4:
            self.camera.orbital_rotation()
        elif button == 5:
            self.camera.orbital_rotation(left=True)

    def shoot_ball(self):
        for item in self.scene_items:
            if item.shoot:
                item.shoot(self.angle, self.strength)

    def reset(self):
        for item in self.scene_items:
            if item.reset_position:
                item.reset_position()

    def increase_strength(self):
        if self.strength < self.max_strength:
            self.strength += .5
        print("increased strenght to", self.strength)

    def decrease_strength(self):
        if self.strength > 1:
            self.strength -= .5
        print("dimished strenght to", self.strength)

    def increase_angle(self):
        if self.angle < 90:
            self.angle += 1
        print("increased angle to", self.angle)

    def decrease_angle(self):
        if self.angle > 0:
            self.angle -= 1
        print("dimished angle to", self.angle)

    def move_target_up(self):
        self.target_position[1] += 0.1

    def move_target_down(self):
        self.target_position[1] -= 0.1

    def move_target_right(self):
        self.target_position[0] += 0.1

    def move_target_left(self):
        self.target_position[0] -= 0.1

    def draw_crontrols(self):
        # angle
        draw_arrow(translate=(-6, -.7, 0), rotate=(self.angle - 90, 0, 0, 1))
        # strength
        draw_in_space(scale=(1, self.strength / 2, 1), translate_in_space=(-3, -1, 0), color=(.5, .5, 1))
        # target
        draw_target(translate=self.target_position)
