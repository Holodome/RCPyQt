import numpy as np
import pyrr as pr
from OpenGL.GL import *
from PyQt5 import QtCore, QtGui, QtOpenGL

from rendering import *
from rendering.cube_renderer import CubeRenderer


class FigureViewWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        fmt = QtOpenGL.QGLFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QtOpenGL.QGLFormat.CoreProfile)
        fmt.setSampleBuffers(True)

        super().__init__(fmt, parent)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.camera = Camera()
        self.light = Light(pr.Vector3([0.0, 0.0, -10.0]), pr.Vector3([1.0, 1.0, 1.0]))
        self.reflectivity: float = 0.5
        self.diffuse_factor: float = 1.0

        self.figure = None

        self.previousMousePos = [0, 0]
        self.mouseButtons = {}

        self.camera_callback = lambda x, y: None

    def initializeGL(self) -> None:
        print(self._opengl_info())
        # Контекст инициализируется здесь
        self.renderer = CubeRenderer()

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)

    def paintGL(self) -> None:
        self.clear()
        if self.figure is None:
            return
        self.figure.update()

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
        self.renderer.render(self.figure, self.camera.projectionMatrix, self.camera.viewMatrix,
                             self.light.color, self.light.position, self.reflectivity, self.diffuse_factor)
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
        glClearColor(0.94117647058, 0.94117647058, 0.94117647058, 1.0)
        # glClearColor(0.2, 0.2, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
