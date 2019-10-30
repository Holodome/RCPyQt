import numpy as np
import pyrr as pr
from OpenGL.GL import *
from PyQt5 import QtCore, QtGui, QtOpenGL, QtWidgets, uic

from camera import Camera
from rubiks_cube.cube_renderer import CubeRenderer
from rubiks_cube.rubiks_cube import RubiksCube
from utils import Light


class CubeViewWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        fmt = QtOpenGL.QGLFormat()
        fmt.setVersion(3, 3)
        fmt.setSampleBuffers(True)

        super().__init__(fmt, parent)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.camera = Camera()
        self.light = Light(pr.Vector3([0.0, 0.0, -10.0]), pr.Vector3([1.0, 1.0, 1.0]))
        self.reflectivity: float = 0.5

        self.cube = RubiksCube(3)

        self.previousMousePos = [0, 0]
        self.mouseButtons = {}

        self.camera_callback = lambda x, y: None

    def initializeGL(self) -> None:
        # Контекст инициализируется здесь
        self.renderer = CubeRenderer()

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)

    def paintGL(self) -> None:
        # Обновление логики
        mouse_pos = self.mapFromGlobal(QtGui.QCursor.pos())
        mx = np.clip(mouse_pos.x(), 0, self.width())
        my = np.clip(mouse_pos.y(), 0, self.height())

        dx = self.previousMousePos[0] - mx
        dy = self.previousMousePos[1] - my

        self.previousMousePos = [mx, my]

        if self.mouseButtons.get(1):
            self.camera.calculate_angle_around_player(dx)
            self.camera.calculate_pitch(dy)
        self.camera.move()
        self.camera_callback(self.camera.pitch, self.camera.yaw)
        # Отрисовка здесь
        self.clear()
        self.renderer.render(self.cube, self.camera, self.light, self.reflectivity)
        self.update()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_G:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_G:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.mouseButtons[event.button()] = True

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.mouseButtons[event.button()] = False

    def resizeGL(self, w: int, h: int) -> None:
        glViewport(0, 0, w, h)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        self.camera.calculate_zoom(event.angleDelta().y())

    @staticmethod
    def _opengl_info() -> str:
        return f"""### OpenGL info ###        
 Vendor: {glGetString(GL_VENDOR).decode("utf-8")}
 Renderer: {glGetString(GL_RENDERER).decode("utf-8")}
 OpenGL Version: {glGetString(GL_VERSION).decode("utf-8")}
 GLSL Version: {glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8")}
"""

    def clear(self):
        # glClearColor(0.94117647058, 0.94117647058, 0.94117647058, 1.0)
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        uic.loadUi("ui.ui", self)

        self.view = CubeViewWidget(self)
        self.view.setGeometry(0, 0, 800, 800)
        # Цвет света
        self.s_LCr.valueChanged.connect(lambda: self.change_color(0))
        self.s_LCg.valueChanged.connect(lambda: self.change_color(1))
        self.s_LCb.valueChanged.connect(lambda: self.change_color(2))
        # Позиция света
        self.s_LPx.valueChanged.connect(lambda: self.change_light_position(0))
        self.s_LPy.valueChanged.connect(lambda: self.change_light_position(1))
        self.s_LPz.valueChanged.connect(lambda: self.change_light_position(2))
        # Отражаемость
        self.s_R.valueChanged.connect(self.change_reflectivity)
        # Камера
        self.s_Cx.valueChanged.connect(lambda: self.change_camera_rotation(0))
        self.s_Cy.valueChanged.connect(lambda: self.change_camera_rotation(1))
        self.view.camera_callback = self.manual_camera_rotation_change_callback

        self.ignore_rotation_change: bool = False

    def change_color(self, color_ind):
        value = self.sender().value() / 255
        self.view.light.color[color_ind] = value

    def change_light_position(self, pos_ind):
        value = self.sender().value() / 10
        self.view.light.position[pos_ind] = value

    def change_reflectivity(self):
        value = self.sender().value() / 100
        self.view.reflectivity = value

    def change_camera_rotation(self, rot_ind):
        if self.ignore_rotation_change:
            return

        value = self.sender().value()
        if rot_ind == 0:
            self.view.camera.pitch = value
        elif rot_ind == 1:
            self.view.camera.angleAroundPlayer.target = value

    def manual_camera_rotation_change_callback(self, x_rot, y_rot):
        self.ignore_rotation_change = True
        self.s_Cx.setValue(x_rot)
        self.s_Cy.setValue(y_rot)
        self.ignore_rotation_change = False
