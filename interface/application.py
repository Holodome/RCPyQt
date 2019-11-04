from PyQt5 import QtWidgets, uic

from rubiks_cube.rubiks_cube import RubiksCube
from .figure_view import FigureViewWidget


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.figure = None

        self.initUi()

        self.ignoreRotationChange: bool = False

    def initUi(self):
        uic.loadUi("ui.ui", self)

        self.view = FigureViewWidget(self)
        self.view.setGeometry(0, 0, 800, 800)
        # Цвет света
        self.s_LCr.valueChanged.connect(lambda: self.change_color(0))
        self.s_LCg.valueChanged.connect(lambda: self.change_color(1))
        self.s_LCb.valueChanged.connect(lambda: self.change_color(2))
        # Позиция света
        self.s_LPx.valueChanged.connect(lambda: self.change_light_position(0))
        self.s_LPy.valueChanged.connect(lambda: self.change_light_position(1))
        self.s_LPz.valueChanged.connect(lambda: self.change_light_position(2))
        # Параметры света
        self.s_R.valueChanged.connect(self.change_reflectivity)
        self.s_D.valueChanged.connect(self.change_diffuse)
        # Камера
        self.s_Cx.valueChanged.connect(lambda: self.change_camera_rotation(0))
        self.s_Cy.valueChanged.connect(lambda: self.change_camera_rotation(1))
        self.view.camera_callback = self.manual_camera_rotation_change_callback
        # Создание куба
        self.b_CreateCube.clicked.connect(self.create_cube)
        # Вращение куба
        self.b_TurnCube.clicked.connect(self.turn_cube)

        self.create_cube()

    def change_color(self, color_ind):
        value = self.sender().value() / 255
        self.view.light.color[color_ind] = value

    def change_light_position(self, pos_ind):
        value = self.sender().value() / 10
        self.view.light.position[pos_ind] = value

    def change_reflectivity(self):
        value = self.sender().value() / 100
        self.view.reflectivity = value

    def change_diffuse(self):
        value = self.sender().value() / 100
        self.view.diffuse_factor = value

    def change_camera_rotation(self, rot_ind):
        if self.ignoreRotationChange:
            return

        value = self.sender().value()
        if rot_ind == 0:
            self.view.camera.pitch = value
        elif rot_ind == 1:
            self.view.camera.angleAroundPlayer.target = value

    def manual_camera_rotation_change_callback(self, x_rot, y_rot):
        self.ignoreRotationChange = True
        self.s_Cx.setValue(x_rot)
        self.s_Cy.setValue(y_rot)
        self.ignoreRotationChange = False

    def create_cube(self):
        size = self.sb_SizeSelector.value()
        figure = RubiksCube(size)
        self.figure = figure
        self.view.figure = figure
        self.view.setFocus()

    def turn_cube(self):
        axis = self.c_AxisSelect.currentIndex()
        index = self.sb_IndexSelector.value()
        clockwise = self.cb_DirectionSelector.isChecked()
        if self.figure is not None:
            self.figure.turn_cube(index, axis, clockwise)
