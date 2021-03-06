# Loads the .ui file and is the entry point of the UI. It is the View of the program.

import sys, os

from PyQt5 import QtCore, QtGui, QtWidgets, uic

# the model and controller classes
from IanUiCtrl import IanUiController
from IanUiMod import IanUiModel

__version__ = 0.1
__author__ = 'Daragh Meehan & Eloise Milliken'

qtdesigner_file  = "IanLight.ui"
# loading the .ui file for use in Python
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtdesigner_file)


class IanUi(QtWidgets.QStackedWidget, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QStackedWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.setCurrentWidget(self.START)

    # generates a pop-up with an input message
    def popUp(self, string):
        widget = self.currentWidget()
        popUp = QtWidgets.QWidget(parent = widget)
        popUp.setGeometry(90, 30,560, 360)
        popUp.setStyleSheet("background-color: rgb(120, 120, 120);")
        label = QtWidgets.QLabel(parent = popUp)
        label.setGeometry(10, 10, 540, 340)
        label.setText(string)
        label.setWordWrap(True)
        label.setStyleSheet("background-color: rgb(255, 255, 255);font: 20 26pt montserrat; color: #444444;")
        label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        popButton = QtWidgets.QPushButton(parent = popUp)
        popButton.setGeometry(500, 5, 50, 50)
        popButton.setText("x")
        popButton.setStyleSheet("font: 30pt montserrat;")
        popButton.setFlat(True)
        popButton.clicked.connect(lambda: popUp.close())
        popUp.show()

# The entry point of the program. Initialises the model, view, and controller
def main():
    #os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/publish_initial_pos.py")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('plastique')
    model = IanUiModel()
    view = IanUi()
    view.show()
    IanUiController(model=model, view=view)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
