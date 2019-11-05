# Fix qt import error
# Include this file before import PyQt5

import sys

from PyQt5.QtWidgets import QApplication

from interface.application import Application


def main():
    # PyQt5 отключает сообщения об ошибках
    sys.excepthook = lambda cls, exception, traceback: sys.__excepthook__(cls, exception, traceback)

    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
