import math

import numpy as np
from pyrr import Matrix44, Vector3, matrix44

from rendering.utils import SmoothFloat

FOV = 60
NEAR_PLANE = 0.1
FAR_PLANE = 50


class Camera:
    def __init__(self):
        self.viewMatrix: Matrix44 = Matrix44.identity(dtype=np.float32)
        self.projectionMatrix: Matrix44 = matrix44.create_perspective_projection(FOV,
                                                                                 1,
                                                                                 NEAR_PLANE,
                                                                                 FAR_PLANE,
                                                                                 dtype=np.float32)

        self.pitch: float = 0
        self.yaw: float = 0

        self.angleAroundPlayer = SmoothFloat(0, 10)
        self.distanceFromPlayer = SmoothFloat(20, 5)

    def move(self):
        self.distanceFromPlayer.update(1.0 / 60)
        self.angleAroundPlayer.update(1.0 / 60)
        self.yaw = self.angleAroundPlayer.actual
        self.yaw %= 360
        self.update_view_matrix()

    def update_view_matrix(self):
        self.viewMatrix = matrix44.multiply(
            matrix44.create_from_x_rotation(math.radians(self.pitch)),
            matrix44.create_from_y_rotation(math.radians(self.yaw)))
        self.viewMatrix = matrix44.multiply(
            self.viewMatrix,
            matrix44.create_from_translation(Vector3([0, 0, -self.distanceFromPlayer.actual])))

    def calculate_pitch(self, dy):
        pitch_change = -dy / 2
        self.pitch = np.clip(self.pitch - pitch_change, -45, 45)

    def calculate_angle_around_player(self, dx):
        angle_change = dx
        self.angleAroundPlayer.target += angle_change

    def calculate_zoom(self, scroll):
        target_zoom = self.distanceFromPlayer.target
        zoom_level = scroll * target_zoom / 200
        target_zoom = np.clip(target_zoom - zoom_level, 6, 40)

        self.distanceFromPlayer.target = target_zoom
        self.distanceFromPlayer.update(1.0 / 60)
