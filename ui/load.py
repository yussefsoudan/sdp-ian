import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


qtcreator_file  = "the.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QStackedWidget, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QStackedWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)



        self.start.clicked.connect(lambda: self.setCurrentWidget(self.SCAN))
        self.next.clicked.connect(lambda: self.setCurrentWidget(self.SUCCESS))
        self.next2.clicked.connect(lambda: self.setCurrentWidget(self.INFO))
        self.go_somewhere.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.gate.clicked.connect(lambda: self.setCurrentWidget(self.CONFIRM_DEST))
        self.shop.clicked.connect(lambda: self.setCurrentWidget(self.SHOPS))
        self.toilet.clicked.connect(lambda: self.setCurrentWidget(self.CONFIRM_DEST))
        self.food.clicked.connect(lambda: self.setCurrentWidget(self.FOOD))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
