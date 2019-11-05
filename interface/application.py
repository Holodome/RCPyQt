import csv

from PyQt5 import QtWidgets

from rubiks_cube.cube_state import CubeState
from rubiks_cube.rubiks_cube import RubiksCube
from .__app import Ui_RubiksCube
from .figure_view import FigureViewWidget


class Application(QtWidgets.QMainWindow, Ui_RubiksCube):
    def __init__(self):
        super().__init__()

        self.figure = None
        self.setupUi(self)
        self.initUi()

        self.ignoreRotationChange: bool = False

    def initUi(self):
        self.setWindowTitle("Rubik's Cube")
        # Главынй виджет, отвечающий за отрисовку фигур
        self.view = FigureViewWidget(self)
        self.view.setGeometry(0, 0, 800, 800)
        # Большинство названий виджетов - первые буквы соответствующих слов
        # Цвет освещения
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
        self.view.cameraCallback = self.manual_camera_rotation_change_callback
        # Создание куба
        self.b_CreateCube.clicked.connect(self.create_cube)
        # Вращение куба
        self.b_TurnCube.clicked.connect(self.turn_cube)
        # Сохранение и загрузка состояния
        self.b_SF.clicked.connect(self.save_cube)
        self.b_LF.clicked.connect(self.load_cube)
        self.b_SS.clicked.connect(self.save_state)
        self.b_LS.clicked.connect(self.load_state)
        # Запутывание кубика и алгоритмы
        self.b_RS.clicked.connect(self.start_scrambling)
        self.b_DoAlg.clicked.connect(self.make_algorithm)

        # Все обьекты интерйеса, имеющие состояние собраны в одном списке для сохранения и загрузки
        self.state = [
            self.s_LCr,
            self.s_LCg,
            self.s_LCb,
            self.s_LPx,
            self.s_LPy,
            self.s_LPz,
            self.s_R,
            self.s_D,
            self.s_Cx,
            self.s_Cy,
        ]

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
        self.view.colorFactor = value

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
        self.set_figure(figure)
        self.view.setFocus()
        self.sb_IndexSelector.setMaximum(figure.size - 1)

    def turn_cube(self):
        axis = self.c_AxisSelect.currentIndex()
        index = self.sb_IndexSelector.value()
        clockwise = self.cb_DirectionSelector.isChecked()
        if self.figure is not None:
            self.figure.turn_cube(index, axis, clockwise)

    def save_cube(self):
        path = self.get_save_filepath()
        if path:
            CubeState.save(self.figure, path)

    def save_state(self):
        path = self.get_save_filepath()
        if path:
            with open(path, "w") as out:
                writer = csv.writer(out, delimiter=",")
                writer.writerow(list(map(lambda e: int(e.value()), self.state)))

    def load_cube(self):
        path = self.get_open_filepath()
        if path:
            figure = CubeState.load(path)
            if figure is not None:
                self.set_figure(figure)

    def load_state(self):
        path = self.get_open_filepath()
        if not path:
            return
        with open(path) as f:
            reader = csv.reader(f, delimiter=",")
            try:
                for el, value in zip(self.state, next(reader)):
                    el.setValue(int(value))
            except Exception:
                print("Incorrect format")

    def get_open_filepath(self):
        file = QtWidgets.QFileDialog.getOpenFileName(caption="Select save file", filter="CSV files (*.csv)")
        return file[0]

    def get_save_filepath(self):
        file = QtWidgets.QFileDialog.getSaveFileName(caption="Create new File", filter="CSV files (*.csv)")
        return file[0]

    def start_scrambling(self):
        times = self.sb_ShuffleSelector.value()
        self.view.figureAlgorithms.set_scramble(times)

    def set_figure(self, figure):
        self.figure = figure
        self.view.figure = figure
        self.view.figureAlgorithms.reset()

    def make_algorithm(self):
        alg_ind = self.c_AlgSelect.currentIndex()
        if alg_ind == 0:
            self.view.figureAlgorithms.makeCheckered = True
        elif alg_ind == 1:
            self.view.figureAlgorithms.makeCubeInCube = True
