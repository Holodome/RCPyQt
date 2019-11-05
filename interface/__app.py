# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RubiksCube(object):
    def setupUi(self, RubiksCube):
        RubiksCube.setObjectName("RubiksCube")
        RubiksCube.resize(1191, 800)
        self.centralwidget = QtWidgets.QWidget(RubiksCube)
        self.centralwidget.setObjectName("centralwidget")
        self.s_Cx = QtWidgets.QSlider(self.centralwidget)
        self.s_Cx.setGeometry(QtCore.QRect(830, 40, 22, 160))
        self.s_Cx.setMinimum(-45)
        self.s_Cx.setMaximum(45)
        self.s_Cx.setOrientation(QtCore.Qt.Vertical)
        self.s_Cx.setObjectName("s_Cx")
        self.s_Cy = QtWidgets.QSlider(self.centralwidget)
        self.s_Cy.setGeometry(QtCore.QRect(870, 40, 22, 160))
        self.s_Cy.setMaximum(360)
        self.s_Cy.setOrientation(QtCore.Qt.Vertical)
        self.s_Cy.setObjectName("s_Cy")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(913, 10, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(820, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 210, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 210, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(820, 250, 361, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.c_AxisSelect = QtWidgets.QComboBox(self.centralwidget)
        self.c_AxisSelect.setGeometry(QtCore.QRect(958, 100, 51, 22))
        self.c_AxisSelect.setObjectName("c_AxisSelect")
        self.c_AxisSelect.addItem("")
        self.c_AxisSelect.addItem("")
        self.c_AxisSelect.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1000, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(940, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 1px solid red")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1020, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 1px solid red")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1100, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 1px solid red")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.sb_IndexSelector = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_IndexSelector.setGeometry(QtCore.QRect(1041, 100, 51, 22))
        self.sb_IndexSelector.setObjectName("sb_IndexSelector")
        self.cb_DirectionSelector = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_DirectionSelector.setGeometry(QtCore.QRect(1100, 100, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cb_DirectionSelector.setFont(font)
        self.cb_DirectionSelector.setObjectName("cb_DirectionSelector")
        self.b_TurnCube = QtWidgets.QPushButton(self.centralwidget)
        self.b_TurnCube.setGeometry(QtCore.QRect(1020, 170, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_TurnCube.setFont(font)
        self.b_TurnCube.setStyleSheet("background-color: rgb(255, 135, 45); border: 1px solid black")
        self.b_TurnCube.setObjectName("b_TurnCube")
        self.s_LCg = QtWidgets.QSlider(self.centralwidget)
        self.s_LCg.setGeometry(QtCore.QRect(880, 310, 22, 160))
        self.s_LCg.setMaximum(255)
        self.s_LCg.setProperty("value", 255)
        self.s_LCg.setOrientation(QtCore.Qt.Vertical)
        self.s_LCg.setObjectName("s_LCg")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(830, 280, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.s_LCr = QtWidgets.QSlider(self.centralwidget)
        self.s_LCr.setGeometry(QtCore.QRect(840, 310, 22, 160))
        self.s_LCr.setStyleSheet("")
        self.s_LCr.setMaximum(255)
        self.s_LCr.setProperty("value", 255)
        self.s_LCr.setOrientation(QtCore.Qt.Vertical)
        self.s_LCr.setObjectName("s_LCr")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(840, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background: #ff0000;")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(880, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background: #00ff00")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.s_LCb = QtWidgets.QSlider(self.centralwidget)
        self.s_LCb.setGeometry(QtCore.QRect(920, 310, 22, 160))
        self.s_LCb.setMaximum(255)
        self.s_LCb.setProperty("value", 255)
        self.s_LCb.setOrientation(QtCore.Qt.Vertical)
        self.s_LCb.setObjectName("s_LCb")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(920, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background: #0000ff")
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(970, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(960, 280, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1050, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.s_LPy = QtWidgets.QSlider(self.centralwidget)
        self.s_LPy.setGeometry(QtCore.QRect(1010, 310, 22, 160))
        self.s_LPy.setMinimum(-100)
        self.s_LPy.setMaximum(100)
        self.s_LPy.setOrientation(QtCore.Qt.Vertical)
        self.s_LPy.setObjectName("s_LPy")
        self.s_LPx = QtWidgets.QSlider(self.centralwidget)
        self.s_LPx.setGeometry(QtCore.QRect(970, 310, 22, 160))
        self.s_LPx.setMinimum(-100)
        self.s_LPx.setMaximum(100)
        self.s_LPx.setOrientation(QtCore.Qt.Vertical)
        self.s_LPx.setObjectName("s_LPx")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1010, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.s_LPz = QtWidgets.QSlider(self.centralwidget)
        self.s_LPz.setGeometry(QtCore.QRect(1050, 310, 22, 160))
        self.s_LPz.setMinimum(-100)
        self.s_LPz.setMaximum(100)
        self.s_LPz.setOrientation(QtCore.Qt.Vertical)
        self.s_LPz.setObjectName("s_LPz")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(940, 260, 20, 261))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(830, 510, 361, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1070, 260, 20, 261))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1090, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.s_R = QtWidgets.QSlider(self.centralwidget)
        self.s_R.setGeometry(QtCore.QRect(1100, 310, 22, 160))
        self.s_R.setMaximum(100)
        self.s_R.setProperty("value", 50)
        self.s_R.setOrientation(QtCore.Qt.Vertical)
        self.s_R.setObjectName("s_R")
        self.s_D = QtWidgets.QSlider(self.centralwidget)
        self.s_D.setGeometry(QtCore.QRect(1140, 310, 22, 160))
        self.s_D.setMaximum(100)
        self.s_D.setProperty("value", 100)
        self.s_D.setOrientation(QtCore.Qt.Vertical)
        self.s_D.setObjectName("s_D")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1100, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1140, 480, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.b_CreateCube = QtWidgets.QPushButton(self.centralwidget)
        self.b_CreateCube.setGeometry(QtCore.QRect(830, 610, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_CreateCube.setFont(font)
        self.b_CreateCube.setStyleSheet("background-color: rgb(255, 135, 45); border: 1px solid black")
        self.b_CreateCube.setObjectName("b_CreateCube")
        self.sb_SizeSelector = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_SizeSelector.setGeometry(QtCore.QRect(890, 570, 51, 22))
        self.sb_SizeSelector.setMinimum(1)
        self.sb_SizeSelector.setProperty("value", 3)
        self.sb_SizeSelector.setObjectName("sb_SizeSelector")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(830, 530, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(830, 570, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("border: 1px solid red")
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.b_SF = QtWidgets.QPushButton(self.centralwidget)
        self.b_SF.setGeometry(QtCore.QRect(970, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_SF.setFont(font)
        self.b_SF.setStyleSheet("background-color: red; border: 1px solid black")
        self.b_SF.setObjectName("b_SF")
        self.b_SS = QtWidgets.QPushButton(self.centralwidget)
        self.b_SS.setGeometry(QtCore.QRect(970, 540, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_SS.setFont(font)
        self.b_SS.setStyleSheet("background-color: red; border: 1px solid black")
        self.b_SS.setObjectName("b_SS")
        self.b_LF = QtWidgets.QPushButton(self.centralwidget)
        self.b_LF.setGeometry(QtCore.QRect(1080, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_LF.setFont(font)
        self.b_LF.setStyleSheet("background-color:  rgb(196, 255, 0); border: 1px solid black")
        self.b_LF.setObjectName("b_LF")
        self.b_LS = QtWidgets.QPushButton(self.centralwidget)
        self.b_LS.setGeometry(QtCore.QRect(1080, 540, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_LS.setFont(font)
        self.b_LS.setStyleSheet("background-color: rgb(196, 255, 0); border: 1px solid black")
        self.b_LS.setObjectName("b_LS")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(830, 650, 361, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(940, 510, 20, 151))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.b_RS = QtWidgets.QPushButton(self.centralwidget)
        self.b_RS.setGeometry(QtCore.QRect(830, 670, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_RS.setFont(font)
        self.b_RS.setStyleSheet("background-color: rgb(234, 234, 0); border: 1px solid black")
        self.b_RS.setObjectName("b_RS")
        self.sb_ShuffleSelector = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_ShuffleSelector.setGeometry(QtCore.QRect(890, 720, 41, 21))
        self.sb_ShuffleSelector.setMinimum(1)
        self.sb_ShuffleSelector.setMaximum(999)
        self.sb_ShuffleSelector.setProperty("value", 20)
        self.sb_ShuffleSelector.setObjectName("sb_ShuffleSelector")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(830, 720, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border: 1px solid red")
        self.label_21.setFrameShape(QtWidgets.QFrame.Box)
        self.label_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(940, 650, 20, 101))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.c_AlgSelect = QtWidgets.QComboBox(self.centralwidget)
        self.c_AlgSelect.setGeometry(QtCore.QRect(970, 680, 201, 22))
        self.c_AlgSelect.setObjectName("c_AlgSelect")
        self.c_AlgSelect.addItem("")
        self.c_AlgSelect.addItem("")
        self.b_DoAlg = QtWidgets.QPushButton(self.centralwidget)
        self.b_DoAlg.setGeometry(QtCore.QRect(970, 720, 75, 23))
        self.b_DoAlg.setObjectName("b_DoAlg")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1060, 720, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border: 1px solid red")
        self.label_22.setFrameShape(QtWidgets.QFrame.Box)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        RubiksCube.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RubiksCube)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 21))
        self.menubar.setObjectName("menubar")
        RubiksCube.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RubiksCube)
        self.statusbar.setObjectName("statusbar")
        RubiksCube.setStatusBar(self.statusbar)

        self.retranslateUi(RubiksCube)
        QtCore.QMetaObject.connectSlotsByName(RubiksCube)

    def retranslateUi(self, RubiksCube):
        _translate = QtCore.QCoreApplication.translate
        RubiksCube.setWindowTitle(_translate("RubiksCube", "MainWindow"))
        self.label.setText(_translate("RubiksCube", "Camera"))
        self.label_2.setText(_translate("RubiksCube", "X"))
        self.label_3.setText(_translate("RubiksCube", "Y"))
        self.c_AxisSelect.setItemText(0, _translate("RubiksCube", "X"))
        self.c_AxisSelect.setItemText(1, _translate("RubiksCube", "Y"))
        self.c_AxisSelect.setItemText(2, _translate("RubiksCube", "Z"))
        self.label_4.setText(_translate("RubiksCube", "Turn Cube"))
        self.label_5.setText(_translate("RubiksCube", "Axis"))
        self.label_6.setText(_translate("RubiksCube", "Index"))
        self.label_7.setText(_translate("RubiksCube", "Direction"))
        self.cb_DirectionSelector.setText(_translate("RubiksCube", "Clockwise"))
        self.b_TurnCube.setText(_translate("RubiksCube", "Turn"))
        self.label_8.setText(_translate("RubiksCube", "Light Color"))
        self.label_9.setText(_translate("RubiksCube", "R"))
        self.label_10.setText(_translate("RubiksCube", "G"))
        self.label_11.setText(_translate("RubiksCube", "B"))
        self.label_12.setText(_translate("RubiksCube", "X"))
        self.label_13.setText(_translate("RubiksCube", "Light Position"))
        self.label_14.setText(_translate("RubiksCube", "Z"))
        self.label_15.setText(_translate("RubiksCube", "Y"))
        self.label_16.setText(_translate("RubiksCube", "Light Chars"))
        self.label_17.setText(_translate("RubiksCube", "R"))
        self.label_18.setText(_translate("RubiksCube", "D"))
        self.b_CreateCube.setText(_translate("RubiksCube", "Create"))
        self.label_19.setText(_translate("RubiksCube", "Create Cube"))
        self.label_20.setText(_translate("RubiksCube", "Size"))
        self.b_SF.setText(_translate("RubiksCube", "Save Figure"))
        self.b_SS.setText(_translate("RubiksCube", "Save Settings"))
        self.b_LF.setText(_translate("RubiksCube", "Load Figure"))
        self.b_LS.setText(_translate("RubiksCube", "Load Settings"))
        self.b_RS.setText(_translate("RubiksCube", "Random Shuffle"))
        self.label_21.setText(_translate("RubiksCube", "Times"))
        self.c_AlgSelect.setItemText(0, _translate("RubiksCube", "Checkered"))
        self.c_AlgSelect.setItemText(1, _translate("RubiksCube", "Cube In Cube"))
        self.b_DoAlg.setText(_translate("RubiksCube", "Do"))
        self.label_22.setText(_translate("RubiksCube", "Algorithms"))
