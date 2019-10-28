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
        # fmt.setProfile(QtOpenGL.QGLFormat.CoreProfile)
        fmt.setSampleBuffers(True)

        super().__init__(fmt, parent)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.camera = Camera()
        self.light = Light(pr.Vector3([0.0, 0.0, -10.0]), pr.Vector3([1.0, 1.0, 1.0]))
        self.cube = RubiksCube(3)

        self.previousMousePos = [0, 0]

        self.mouseButtons = [False for _ in range(7)]

    def initializeGL(self) -> None:
        self.resizeGL(self.width(), self.height())
        print(self.width(), self.height())
        self.renderer = CubeRenderer()

        glEnable(GL_DEPTH_TEST)
        # glEnable(GL_CULL_FACE)
        # glCullFace(GL_BACK)

    def paintGL(self) -> None:
        mouse_pos = self.mapFromGlobal(QtGui.QCursor.pos())
        mx = np.clip(mouse_pos.x(), 0, self.width())
        my = np.clip(mouse_pos.y(), 0, self.height())

        dx = self.previousMousePos[0] - mx
        dy = self.previousMousePos[1] - my

        self.previousMousePos = [mx, my]

        if self.mouseButtons[1]:
            self.camera.calculate_angle_around_player(dx)
            self.camera.calculate_pitch(dy)
        self.camera.move()

        self.clear()
        self.renderer.render(self.cube, self.camera, self.light)
        self.update()

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
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)

        try:
            self.view = CubeViewWidget(self)
            self.view.setGeometry(0, 0, 800, 800)
        except Exception as e:
            print(e)
