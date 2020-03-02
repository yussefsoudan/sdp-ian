# Loads the .ui file and is the entry point of the UI. It is the View of the program.

import sys, os

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest, uic

# the model and controller classes
from IanUiCtrl import IanUiController
from IanUiMod import IanUiModel

__version__ = 0.1
__author__ = 'Daragh Meehan & Eloise Milliken'

qtdesigner_file  = "the.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtdesigner_file)


class IanUi(QtWidgets.QStackedWidget, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QStackedWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.setCurrentWidget(self.START)


def main():
    os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/publish_initial_pos.py")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('plastique')
    model = IanUiModel()
    view = IanUi()
    view.show()
    IanUiController(model=model, view=view)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
