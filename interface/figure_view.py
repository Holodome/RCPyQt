import time

import numpy as np
import pyrr as pr
from OpenGL.GL import *
from PyQt5 import QtCore, QtGui, QtOpenGL

from rendering import *
from rendering.cube_renderer import CubeRenderer
from rubiks_cube.cube_algorithms import CubeAlgorithms

ACTIVE_BUTTON = 1


class FigureViewWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        # Говорим Qt выбрать OpenGL 3.3 core
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
        self.colorFactor: float = 1.0  # Общий коофицент цвета

        self.figure = None
        # Обьект, отвечающий за автоматические операции над кубиком
        self.figureAlgorithms = CubeAlgorithms()
        # Харакетеристики мыши
        self.previousMousePos = [0, 0]
        self.mouseButtons = {}
        # Функция, вызываемая при смене позиции камеры, тк в основном окне есть соответствующие слайдеры
        self.cameraCallback = lambda x, y: None
        # Время последнего обновления (отрисовки)
        self.lastTime = time.time()

    def initializeGL(self) -> None:
        print(self._opengl_info())
        # Контекст инициализируется здесь
        self.renderer = CubeRenderer()

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)

    def paintGL(self) -> None:
        # Очистка окна происходит в любом случае
        self.clear()
        if self.figure is None:
            return
        # Обновление времени
        now = time.time()
        dt = now - self.lastTime
        self.lastTime = now
        # Произведение алгоритмов, затем обновление (вращение) фигуры
        self.figureAlgorithms.update(self.figure)
        self.figure.update(dt)
        # Получаем позицию мыши
        mouse_pos = self.mapFromGlobal(QtGui.QCursor.pos())
        mx = np.clip(mouse_pos.x(), 0, self.width())  # np.clip - clamp
        my = np.clip(mouse_pos.y(), 0, self.height())

        dx = self.previousMousePos[0] - mx
        dy = self.previousMousePos[1] - my

        self.previousMousePos = [mx, my]
        # Если нажата левая кнопка мыши
        if self.mouseButtons.get(ACTIVE_BUTTON):
            self.camera.calculate_angle_around_player(dx)
            self.camera.calculate_pitch(dy)
        self.camera.update()
        self.cameraCallback(self.camera.pitch, self.camera.yaw)
        # Отрисовка здесь
        self.renderer.render(self.figure, self.camera.projectionMatrix, self.camera.viewMatrix,
                             self.light.color, self.light.position, self.reflectivity, self.colorFactor)
        self.update()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        # Для дебага - меняет отрисовку на границы полигонов вместо заливки
        if event.key() == QtCore.Qt.Key_G:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_G:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        # Сохраняем состояние нажатой кнопки в словаре
        self.mouseButtons[event.button()] = True

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.mouseButtons[event.button()] = False

    def resizeGL(self, w: int, h: int) -> None:
        glViewport(0, 0, w, h)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        # На движение колесиком меняется зум камеры
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
        # Очистка экрана (цвет как у окна Qt)
        glClearColor(0.94117647058, 0.94117647058, 0.94117647058, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
