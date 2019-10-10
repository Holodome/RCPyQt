import math

import numpy as np
from pyrr import Matrix44, Vector3, matrix44

from utils import SmoothFloat

FOV = 60
NEAR_PLANE = 0.1
FAR_PLANE = 50


class Camera:
    def __init__(self, window):
        self.window = window

        self.viewMatrix: Matrix44 = Matrix44.identity(dtype=np.float32)
        self.projectionMatrix: Matrix44 = matrix44.create_perspective_projection(FOV,
                                                                                 window.ratio,
                                                                                 NEAR_PLANE,
                                                                                 FAR_PLANE,
                                                                                 dtype=np.float32)

        self.pitch: float = 0
        self.yaw: float = 0

        self.angleAroundPlayer = SmoothFloat(0, 10)
        self.distanceFromPlayer = SmoothFloat(20, 5)

    def move(self):
        self.calculate_pitch()
        self.calculate_angle_around_player()
        self.calculate_zoom()
        self.yaw = 360 - self.angleAroundPlayer.actual
        self.yaw %= 360
        self.update_view_matrix()

    def update_view_matrix(self):
        self.viewMatrix = matrix44.multiply(matrix44.create_from_x_rotation(
            math.radians(self.pitch)),
            matrix44.create_from_y_rotation(math.radians(self.yaw)))
        self.viewMatrix = matrix44.multiply(self.viewMatrix, matrix44.create_from_translation(
            Vector3([0, 0, -self.distanceFromPlayer.actual])))

    def calculate_pitch(self):
        if self.window.mouse.is_key_held(1):
            pitch_change = -self.window.mouse.dy * 45
            self.pitch -= pitch_change
            if self.pitch < -45:
                self.pitch = -45
            elif self.pitch > 45:
                self.pitch = 45

    def calculate_angle_around_player(self):
        if self.window.mouse.is_key_held(1):
            angle_change = self.window.mouse.dx * 70
            self.angleAroundPlayer.target -= angle_change
        self.angleAroundPlayer.update(1.0 / 60)

    def calculate_zoom(self):
        target_zoom = self.distanceFromPlayer.target
        zoom_level = self.window.mouse.scroll * 0.2 * target_zoom
        self.window.mouse.scroll = 0
        target_zoom -= zoom_level
        if target_zoom < 6:
            target_zoom = 6
        elif target_zoom > 40:
            target_zoom = 40

        self.distanceFromPlayer.target = target_zoom
        self.distanceFromPlayer.update(1.0 / 60)
